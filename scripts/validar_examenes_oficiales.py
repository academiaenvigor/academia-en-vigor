#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

ID_RE = re.compile(r"^of-pn-p\d+-[a-z]-q\d{3}$")
EXAM_ID_RE = re.compile(r"^of-pn-p\d+-[a-z]$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    repo_root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    data_root = repo_root / "banco-preguntas" / "policia-nacional" / "oficiales"
    index_path = data_root / "manifest.json"
    errors: list[str] = []
    warnings: list[str] = []

    if not index_path.exists():
        print(f"ERROR: no existe {index_path}")
        return 1

    index = json.loads(index_path.read_text(encoding="utf-8"))
    seen_ids: set[str] = set()
    total_normalised = 0
    exam_fingerprints: dict[str, set[str]] = {}

    for exam in index.get("exams", []):
        metadata_path = repo_root / exam["metadata_path"]
        if not metadata_path.exists():
            fail(errors, f"Falta metadata: {exam['metadata_path']}")
            continue

        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        if metadata.get("id") != exam.get("id"):
            fail(errors, f"ID incoherente entre índice y metadata: {exam.get('id')}")

        questions_path = exam.get("questions_path")
        if questions_path is None:
            if exam.get("normalisation_status") != "source_only_pending_normalisation":
                warnings.append(f"{exam['id']}: sin preguntas normalizadas")
            continue

        q_path = repo_root / questions_path
        if not q_path.exists():
            fail(errors, f"Falta archivo de preguntas: {questions_path}")
            continue

        records = [
            json.loads(line)
            for line in q_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        total_normalised += len(records)

        def normalise_text(value: str) -> str:
            value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
            return re.sub(r"[^a-z0-9]+", " ", value).strip()

        fingerprints: set[str] = set()
        for record in records:
            option_text = " | ".join(option.get("text", "") for option in record.get("options", []))
            canonical = normalise_text(record.get("prompt", "") + " | " + option_text)
            fingerprints.add(hashlib.sha256(canonical.encode("utf-8")).hexdigest())
        exam_fingerprints[exam["id"]] = fingerprints

        expected = metadata.get("expected_questions")
        if expected is not None and len(records) != expected:
            fail(errors, f"{exam['id']}: {len(records)} preguntas; se esperaban {expected}")

        numbers: set[int] = set()
        for record in records:
            qid = record.get("id")
            if not isinstance(qid, str) or not ID_RE.match(qid):
                fail(errors, f"ID inválido: {qid}")
            elif qid in seen_ids:
                fail(errors, f"ID duplicado: {qid}")
            else:
                seen_ids.add(qid)

            exam_id = record.get("exam_id")
            if exam_id != exam["id"] or not EXAM_ID_RE.match(exam_id or ""):
                fail(errors, f"{qid}: exam_id inválido o incoherente")

            q_number = record.get("exam", {}).get("question_number")
            if not isinstance(q_number, int) or q_number < 1:
                fail(errors, f"{qid}: número de pregunta inválido")
            elif q_number in numbers:
                fail(errors, f"{exam['id']}: número duplicado {q_number}")
            else:
                numbers.add(q_number)

            options = record.get("options", [])
            if len(options) != 3:
                fail(errors, f"{qid}: debe tener exactamente tres opciones")
            option_ids = [option.get("id") for option in options]
            if len(set(option_ids)) != len(option_ids):
                fail(errors, f"{qid}: opciones con IDs duplicados")

            for answer_field in ("proposed_answer_option_id", "official_answer_option_id"):
                answer_id = record.get(answer_field)
                if answer_id is not None and answer_id not in option_ids:
                    fail(errors, f"{qid}: {answer_field} no referencia una opción válida")

            if "feedback_secondary" in record:
                fail(errors, f"{qid}: contiene feedback secundario de terceros")
            rights = record.get("rights_and_sources", {})
            if rights.get("third_party_files_included") or rights.get("third_party_commentary_included"):
                fail(errors, f"{qid}: marca contenido de terceros como incluido")

            status = record.get("status")
            counts = record.get("counts_for_ha_caido")
            official_answer = record.get("official_answer_option_id")
            official_key = record.get("origin", {}).get("official_final_answer_key")

            if status == "quarantine" and counts:
                fail(errors, f"{qid}: una pregunta en cuarentena no puede alimentar Ha caído")
            if status == "verified":
                if not official_answer:
                    fail(errors, f"{qid}: verificada sin respuesta oficial")
                if not official_key:
                    fail(errors, f"{qid}: verificada sin plantilla definitiva")
            if counts and status != "verified":
                fail(errors, f"{qid}: Ha caído exige estado verified")


    # Repositorio publicable: no debe contener originales, marcas de agua ni comentarios de terceros.
    forbidden_exts = {".pdf", ".doc", ".docx", ".odt"}
    forbidden_dirs = [repo_root / "fuentes-privadas", repo_root / "originales", repo_root / "escaneos", repo_root / "descargas"]
    for forbidden_dir in forbidden_dirs:
        if forbidden_dir.exists():
            for path in forbidden_dir.rglob("*"):
                if path.is_file():
                    fail(errors, f"Archivo de fuente privada no permitido en repositorio: {path.relative_to(repo_root)}")
    for path in repo_root.rglob("*"):
        if path.is_file() and path.suffix.lower() in forbidden_exts:
            fail(errors, f"Documento binario no permitido en este paquete publicable: {path.relative_to(repo_root)}")

    duplicate_exam_pairs: list[tuple[str, str, float]] = []
    exam_ids = sorted(exam_fingerprints)
    for i, first_id in enumerate(exam_ids):
        for second_id in exam_ids[i + 1:]:
            first = exam_fingerprints[first_id]
            second = exam_fingerprints[second_id]
            if not first or not second:
                continue
            overlap = len(first & second) / min(len(first), len(second))
            if overlap >= 0.90:
                duplicate_exam_pairs.append((first_id, second_id, overlap))
                fail(errors, f"Conjuntos de preguntas duplicados: {first_id} y {second_id} ({overlap:.1%})")

    topic_files = sorted((repo_root / "banco-preguntas" / "policia-nacional").glob("tema-*/indice-oficiales.json"))
    for topic_file in topic_files:
        topic = json.loads(topic_file.read_text(encoding="utf-8"))
        for item in topic.get("questions", []):
            qid = item.get("question_id")
            if qid not in seen_ids:
                fail(errors, f"{topic_file.name}: referencia pregunta inexistente {qid}")
            for fact_id in item.get("fact_refs", []):
                if not re.match(r"^PN-T\d{2}-F\d{3}$", fact_id):
                    fail(errors, f"{topic_file.name}: fact_id con formato inválido {fact_id}")
            if item.get("counts_for_ha_caido") and item.get("verification_status") != "verified":
                fail(errors, f"{topic_file.name}: referencia no verificada contabilizada en Ha caído")

    print(f"Exámenes inventariados: {len(index.get('exams', []))}")
    print(f"Preguntas normalizadas: {total_normalised}")
    print(f"IDs únicos: {len(seen_ids)}")
    print(f"Pares de exámenes duplicados: {len(duplicate_exam_pairs)}")
    print(f"Advertencias: {len(warnings)}")
    for warning in warnings:
        print(f"ADVERTENCIA: {warning}")

    if errors:
        print(f"Errores: {len(errors)}")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("VALIDACIÓN CORRECTA")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
