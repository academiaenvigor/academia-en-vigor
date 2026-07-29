#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Mapeo revisado pregunta a pregunta. No convierte las respuestas revisadas
# por la academia en una plantilla oficial.
MAPPINGS = {
    "of-pn-p33-a-q017": ([10], "historical_rule_changed"),
    "of-pn-p33-a-q019": ([11], "historical_rule_changed"),
    "of-pn-p34-a-q037": ([26], "current"),
    "of-pn-p34-a-q042": ([14], "current"),
    "of-pn-p34-a-q043": ([25], "current"),
    "of-pn-p34-a-q046": ([19], "current"),
    "of-pn-p35-a-q043": ([9], "historical_rule_changed"),
    "of-pn-p35-a-q064": ([25], "current"),
    "of-pn-p35-a-q079": ([27], "current"),
    "of-pn-p35-a-q100": ([25], "current"),
    "of-pn-p36-a-q055": ([9], "current"),
    "of-pn-p36-a-q068": ([24], "current"),
    "of-pn-p37-a-q015": ([4, 5], "current"),
    "of-pn-p37-a-q032": ([27], "current"),
    "of-pn-p37-a-q034": ([5], "current"),
    "of-pn-p37-a-q053": ([10], "historical_rule_changed"),
    "of-pn-p37-a-q098": ([28], "current"),
    "of-pn-p38-a-q020": ([14, 24], "current"),
    "of-pn-p39-a-q076": ([25, 26], "current"),
    "of-pn-p39-a-q079": ([4], "current"),
    "of-pn-p40-a-q003": ([25], "current"),
    "of-pn-p40-a-q009": ([18], "current"),
    "of-pn-p40-a-q051": ([16], "current"),
    "of-pn-p40-a-q069": ([5], "current"),
    "of-pn-p40-a-q079": ([26], "current"),
    "of-pn-p41-a-q010": ([9], "current"),
    "of-pn-p41-a-q038": ([21], "current"),
    "of-pn-p41-a-q049": ([4], "current"),
    "of-pn-p41-a-q051": ([5], "current"),
    "of-pn-p41-a-q052": ([26], "current"),
    "of-pn-p41-a-q058": ([25], "current"),
    "of-pn-p41-a-q059": ([11], "current"),
    "of-pn-p41-a-q095": ([10], "current"),
    "of-pn-p41-a-q100": ([3], "current"),
    "of-pn-p42-a-q018": ([26], "current"),
    "of-pn-p42-a-q022": ([10], "current"),
    "of-pn-p42-a-q023": ([25], "current"),
    "of-pn-p42-a-q026": ([19], "current"),
    "of-pn-p42-a-q043": ([13], "current"),
    "of-pn-p42-a-q065": ([17], "current"),
    "of-pn-p42-a-q081": ([14], "current"),
    "of-pn-p42-a-q087": ([12], "current"),
}


def load_questions():
    result = {}
    base = ROOT / "banco-preguntas/policia-nacional/oficiales"
    for path in sorted(base.glob("P*/preguntas.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                question = json.loads(line)
                result[question["id"]] = question
    return result


def main():
    bank = load_questions()
    missing = sorted(set(MAPPINGS) - set(bank))
    if missing:
        raise SystemExit(f"IDs inexistentes: {missing}")

    questions = []
    by_block = Counter()
    by_year = Counter()
    verified = 0
    for qid, (blocks, rule_status) in MAPPINGS.items():
        source = bank[qid]
        answer = source.get("verified_answer_option_id")
        if answer:
            verified += 1
        year = int(source["exam"]["series_year"])
        by_year[year] += 1
        for block in blocks:
            by_block[block] += 1
        questions.append({
            "question_id": qid,
            "exam_id": source["exam_id"],
            "series_year": year,
            "question_number": int(source["exam"]["question_number"]),
            "block_refs": blocks,
            "appearance_status": "editorially_mapped",
            "answer_status": "verificada_por_autor_no_plantilla_oficial" if answer else "sin_respuesta_verificada",
            "rule_status_2026": rule_status,
        })

    output = {
        "schema_version": "2.0.0",
        "oposicion": "policia-nacional",
        "tema": 8,
        "titulo": "La Dirección General de la Policía y la Policía Nacional",
        "generated_at": "2026-07-29",
        "mapping_method": "manual_editorial_review",
        "mapping_status": "reviewed",
        "answer_status": "verificada_por_autor_no_plantilla_oficial",
        "display_policy": {
            "show_reviewed_appearances": True,
            "show_answer": False,
            "never_present_as_official_plantilla": True,
        },
        "aviso": (
            "Las referencias acreditan que el concepto apareció en un examen histórico. "
            "Las respuestas están revisadas por la academia, pero no proceden de una plantilla oficial final."
        ),
        "total_referencias": len(questions),
        "con_bloque_asignado": len(questions),
        "con_respuesta_verificada": verified,
        "por_bloque": {str(k): by_block[k] for k in sorted(by_block)},
        "por_promocion": {str(k): by_year[k] for k in sorted(by_year)},
        "retroalimentacion": "banco-preguntas/policia-nacional/oficiales/retroalimentacion.json",
        "questions": questions,
    }
    path = ROOT / "banco-preguntas/policia-nacional/tema-08/indice-oficiales.json"
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {len(questions)} referencias; {verified} respuestas revisadas; {len(by_block)} bloques")


if __name__ == "__main__":
    main()
