#!/usr/bin/env python3
"""Validador universal del contrato técnico de los temas."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from compilar_tema import load

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_ASSET_STATES = {"approved_internal", "integrated_webp", "published"}
FACT_FIELDS = {
    "id", "oposicion", "tema", "bloque", "bloque_titulo", "parte",
    "parte_titulo", "punto", "enunciado_atomico", "fuente",
    "estado_revision", "content_version", "riesgo_examen", "risk",
    "preguntas", "covered", "anchor_score",
}
QUESTION_FIELDS = {
    "id", "fact_id", "oposicion", "tema", "bloque", "punto", "subpunto",
    "parte", "parte_titulo", "concepto", "norma", "articulo",
    "riesgo_examen", "dificultad", "tipo", "enunciado", "opciones",
    "respuesta_correcta", "explicacion", "retroalimentacion",
    "estado_revision", "version_normativa", "caracter",
    "referencia_oficial", "relaciones", "equivalencias", "content_version",
}
TOPIC_INDEX_FIELDS = {
    "number", "slug", "title", "content_version", "editorial_status",
    "publication_status", "manifest", "parte", "atestado", "question_bank",
    "evaluation_plan", "assets", "teaching_materials", "visual_version",
    "visual_assets", "visual_planned", "atomic_facts", "question_count",
    "official_exam_index", "official_exam_mapped", "official_exam_verified",
    "ha_caido_active",
}
KNOWLEDGE_FIELDS = {
    "schema_version", "opposition", "opposition_display_name", "topic",
    "topic_number", "slug", "title", "content_version",
    "pedagogical_version", "visual_version", "editorial_status",
    "publication_status", "normative_status", "source_file", "source_rights",
    "outputs", "semantic_blocks", "atomic_facts", "master_statements",
    "coverage_file", "official_references", "official_exam_items",
    "official_exam_index", "layers", "atestado_style", "question_bank",
    "evaluations", "assets", "teaching_materials", "review",
}
BANK_MANIFEST_FIELDS = {
    "schema_version", "content_version", "oposicion", "tema", "estado",
    "publicacion", "total_preguntas", "total_hechos", "hechos_cubiertos",
    "cobertura_por_hechos", "distribucion_respuestas",
    "distribucion_dificultad", "distribucion_tipo", "preguntas_por_bloque",
    "preguntas_por_parte", "caracter", "fuente_conocimiento", "cobertura",
    "evaluation_plan", "official_exam_index", "retroalimentacion",
    "generacion_de_tests", "publication_gate", "quality_gate",
}
OFFICIAL_INDEX_FIELDS = {
    "schema_version", "oposicion", "tema", "titulo", "generated_at",
    "mapping_method", "mapping_status", "answer_status", "display_policy",
    "aviso", "total_referencias", "con_bloque_asignado",
    "con_respuesta_verificada", "por_bloque", "por_promocion",
    "retroalimentacion", "questions",
}
EVALUATION_FIELDS = {
    "schema_version", "content_version", "opposition", "topic_number",
    "topic_title", "id_prefix", "status", "bank", "output",
    "coverage_tests", "part_tests", "final_tests",
}
ASSET_FIELDS = {
    "schema_version", "opposition", "topic", "content_version",
    "visual_version", "status", "totals", "integration_status",
    "integrated_at", "resources", "planned_resources",
}
ASSET_RESOURCE_FIELDS = {
    "id", "file", "title", "type", "placement", "status", "block",
    "documents", "description", "source_content_version",
    "required_format", "max_bytes",
}
MATERIAL_FIELDS = {
    "schema_version", "opposition", "topic", "content_version",
    "source_version", "status", "storage_policy", "rights_policy",
    "audio_note", "display_policy", "storage_root", "categories", "scopes",
    "nomenclature", "parts", "resources",
}
MATERIAL_PART_FIELDS = {"id", "number", "title", "blocks", "anchor_blocks"}
MATERIAL_RESOURCE_FIELDS = {
    "id", "category", "scope", "part_number", "blocks", "anchor_blocks",
    "title", "filename", "mime_type", "file_size_bytes", "ownership",
    "status", "source_content_version", "tool", "duration_seconds",
    "storage", "resource_type",
}
MATERIAL_STORAGE_FIELDS = {
    "type", "provider", "asset_key", "drive_file_id", "url",
}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def add(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def exact_keys(errors: list[str], data: dict, fields: set[str], label: str) -> None:
    missing = fields - data.keys()
    extra = data.keys() - fields
    if missing:
        errors.append(f"{label}: faltan claves {sorted(missing)}")
    if extra:
        errors.append(f"{label}: sobran claves {sorted(extra)}")


def validate_topic(opposition: str, topic: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    number = int(topic["number"])
    code = f"tema-{number:02d}"
    label = f"{opposition}/{code}"
    exact_keys(errors, topic, TOPIC_INDEX_FIELDS, f"{label}/temario.json")

    paths = {
        "knowledge": ROOT / topic["manifest"],
        "parte": ROOT / topic["parte"],
        "atestado": ROOT / topic["atestado"],
        "bank": ROOT / topic["question_bank"],
        "bank_manifest": ROOT / f"banco-preguntas/{opposition}/{code}/manifest.json",
        "coverage": ROOT / f"conocimiento/{opposition}/{code}/cobertura.json",
        "official": ROOT / topic["official_exam_index"],
        "evaluation": ROOT / topic["evaluation_plan"],
        "assets": ROOT / topic["assets"],
        "materials": ROOT / topic["teaching_materials"],
    }
    for name, path in paths.items():
        add(errors, path.exists(), f"{label}: falta {name}: {path.relative_to(ROOT)}")
    if errors:
        return errors, warnings

    knowledge = read_json(paths["knowledge"])
    coverage = read_json(paths["coverage"])
    bank_manifest = read_json(paths["bank_manifest"])
    official = read_json(paths["official"])
    evaluation = read_json(paths["evaluation"])
    assets = read_json(paths["assets"])
    materials = read_json(paths["materials"])
    exact_keys(errors, knowledge, KNOWLEDGE_FIELDS, f"{label}/manifest")
    exact_keys(errors, bank_manifest, BANK_MANIFEST_FIELDS, f"{label}/banco-manifest")
    exact_keys(errors, official, OFFICIAL_INDEX_FIELDS, f"{label}/indice-oficiales")
    exact_keys(errors, evaluation, EVALUATION_FIELDS, f"{label}/evaluaciones")
    exact_keys(errors, assets, ASSET_FIELDS, f"{label}/assets")
    exact_keys(errors, materials, MATERIAL_FIELDS, f"{label}/materiales")

    add(errors, knowledge["schema_version"] == "2.0.0", f"{label}: manifest fuera de contrato 2.0.0")
    add(errors, coverage.get("schema_version") == "2.0.0", f"{label}: cobertura fuera de contrato 2.0.0")
    add(errors, bank_manifest["schema_version"] == "2.0.0", f"{label}: banco fuera de contrato 2.0.0")
    add(errors, official["schema_version"] == "2.0.0", f"{label}: índice oficial fuera de contrato 2.0.0")
    add(errors, evaluation["schema_version"] == "2.0.0", f"{label}: evaluación fuera de contrato 2.0.0")
    add(errors, assets["schema_version"] == "2.0.0", f"{label}: assets fuera de contrato 2.0.0")
    add(errors, materials["schema_version"] == "2.1.0", f"{label}: materiales fuera de contrato 2.1.0")

    try:
        _, blocks, layers = load(opposition, number)
    except Exception as exc:
        errors.append(f"{label}: fuente maestra no compilable: {exc}")
        return errors, warnings
    add(errors, len(blocks) == knowledge["semantic_blocks"], f"{label}: número de bloques incoherente")
    add(errors, len(layers) == 6, f"{label}: no contiene las seis capas")

    facts = coverage.get("facts", [])
    for fact in facts:
        exact_keys(errors, fact, FACT_FIELDS, f"{label}/{fact.get('id', 'fact-sin-id')}")
    fact_ids = [fact.get("id") for fact in facts]
    add(errors, len(fact_ids) == len(set(fact_ids)), f"{label}: IDs de hechos duplicados")
    add(errors, knowledge["atomic_facts"] == len(facts), f"{label}: atomic_facts incoherente")
    add(errors, coverage["total_atomic_facts"] == len(facts), f"{label}: total_atomic_facts incoherente")
    add(errors, topic["atomic_facts"] == len(facts), f"{label}: contador de hechos en temario.json incoherente")
    catalog_ids = {
        source["id"] for source in read_json(ROOT / "fuentes/catalogo.json").get("sources", [])
    }
    used_sources = set(knowledge.get("official_references", [])) | {
        fact.get("fuente") for fact in facts
    }
    add(
        errors,
        used_sources <= catalog_ids,
        f"{label}: fuentes ausentes del catálogo {sorted(used_sources - catalog_ids)}",
    )

    master = (ROOT / knowledge["source_file"]).read_text(encoding="utf-8")
    parte = paths["parte"].read_text(encoding="utf-8")
    atestado = paths["atestado"].read_text(encoding="utf-8")
    master_markers = re.findall(r"<!-- FACT:([A-Z0-9-]+) -->", master)
    atestado_markers = re.findall(r"<!-- FACT:([A-Z0-9-]+) -->", atestado)
    parte_markers = re.findall(r"<!-- FACT:([A-Z0-9-]+) -->", parte)
    add(errors, Counter(master_markers) == Counter(fact_ids), f"{label}: anclas FACT incorrectas en master")
    add(errors, Counter(atestado_markers) == Counter(fact_ids), f"{label}: anclas FACT incorrectas en Atestado")
    add(errors, not parte_markers, f"{label}: El Parte no debe portar anclas atómicas")
    add(errors, all((fact.get("anchor_score") or 0) >= 0.12 for fact in facts), f"{label}: hay hechos sin anclaje textual fiable")

    questions = [
        json.loads(line) for line in paths["bank"].read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    question_ids = []
    fact_set = set(fact_ids)
    for question in questions:
        question_ids.append(question.get("id"))
        exact_keys(errors, question, QUESTION_FIELDS, f"{label}/{question.get('id', 'pregunta-sin-id')}")
        add(errors, question.get("fact_id") in fact_set, f"{label}/{question.get('id')}: hecho inexistente")
        options = question.get("opciones", {})
        add(errors, set(options) == {"A", "B", "C"}, f"{label}/{question.get('id')}: opciones inválidas")
        add(errors, question.get("respuesta_correcta") in options, f"{label}/{question.get('id')}: respuesta inválida")
        feedback = question.get("retroalimentacion", {})
        add(errors, set(feedback) == {"acierto", "fallo"}, f"{label}/{question.get('id')}: feedback no homologado")
        for branch in ("acierto", "fallo"):
            add(errors, set(feedback.get(branch, {})) == {"humor", "explicacion"}, f"{label}/{question.get('id')}: rama {branch} inválida")
    add(errors, len(question_ids) == len(set(question_ids)), f"{label}: IDs de preguntas duplicados")
    add(errors, bank_manifest["total_preguntas"] == len(questions), f"{label}: total_preguntas incoherente")
    add(errors, topic["question_count"] == len(questions), f"{label}: question_count incoherente")
    add(errors, coverage["total_questions"] == len(questions), f"{label}: total_questions de cobertura incoherente")
    distribution = Counter(question["respuesta_correcta"] for question in questions)
    add(errors, bank_manifest["distribucion_respuestas"] == {
        key: distribution.get(key, 0) for key in ("A", "B", "C")
    }, f"{label}: distribución declarada incoherente")
    gate = bank_manifest["quality_gate"]
    if gate.get("status") != "passed":
        warnings.append(f"{label}: banco bloqueado ({', '.join(gate.get('reasons', []))})")
    else:
        by_fact = Counter(question["fact_id"] for question in questions)
        add(errors, all(
            by_fact[fact["id"]] >= 2 for fact in facts if fact["riesgo_examen"] == 5
        ), f"{label}: puerta aprobada con hechos de riesgo 5 sin doble formulación")
        if questions:
            add(errors, max(distribution.values()) - min(distribution.values()) <= 1, f"{label}: puerta aprobada con distribución desequilibrada")

    add(errors, official["total_referencias"] == len(official["questions"]), f"{label}: total_referencias incoherente")
    add(errors, official["con_respuesta_verificada"] <= official["total_referencias"], f"{label}: verificados imposibles")
    add(errors, topic["official_exam_mapped"] == official["con_bloque_asignado"],
        f"{label}: official_exam_mapped en temario.json incoherente")
    add(errors, topic["official_exam_verified"] == official["con_respuesta_verificada"],
        f"{label}: official_exam_verified en temario.json incoherente")
    add(errors, topic["content_version"] == knowledge["content_version"],
        f"{label}: content_version en temario.json incoherente")
    add(errors, topic["editorial_status"] == knowledge["editorial_status"],
        f"{label}: editorial_status en temario.json incoherente")
    add(errors, topic["publication_status"] == knowledge["publication_status"],
        f"{label}: publication_status en temario.json incoherente")
    add(errors, topic["visual_version"] == assets["visual_version"],
        f"{label}: visual_version en temario.json incoherente")
    add(errors, evaluation["bank"] == topic["question_bank"], f"{label}: plan apunta a otro banco")
    add(errors, "full_tests" not in evaluation, f"{label}: usa full_tests obsoleto")

    asset_root = paths["assets"].parent
    resource_files = []
    for resource in assets["resources"]:
        exact_keys(errors, resource, ASSET_RESOURCE_FIELDS, f"{label}/asset/{resource.get('id')}")
        resource_files.append(resource["file"])
        target = asset_root / resource["file"]
        if resource["status"] in ACTIVE_ASSET_STATES:
            add(errors, target.exists(), f"{label}: falta asset integrado {resource['file']}")
            if target.exists():
                add(errors, target.suffix.lower() == ".webp", f"{label}: asset no WEBP {resource['file']}")
                add(errors, target.stat().st_size <= resource["max_bytes"], f"{label}: asset supera límite {resource['file']}")
    # Dos recursos con el mismo contenido byte a byte significan que uno de
    # los dos nunca llegó a producirse: se copió el otro con su nombre. El
    # alumno ve la misma imagen dos veces en el mismo bloque.
    huellas: dict[str, list[str]] = {}
    for path in sorted(asset_root.glob("*.webp")):
        huellas.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(), []).append(path.name)
    for repetidos in huellas.values():
        add(errors, len(repetidos) == 1,
            f"{label}: imágenes idénticas entre sí {sorted(repetidos)}")

    actual_webp = {path.name for path in asset_root.glob("*.webp")}
    add(errors, actual_webp <= set(resource_files), f"{label}: hay WEBP no inventariados {sorted(actual_webp - set(resource_files))}")
    integrated = sum(resource["status"] in ACTIVE_ASSET_STATES for resource in assets["resources"])
    planned = len(assets["resources"]) - integrated
    add(errors, assets["totals"] == {"resources": len(resources := assets["resources"]), "integrated": integrated, "planned": planned}, f"{label}: totales visuales incoherentes")
    add(errors, topic["visual_assets"] == integrated and topic["visual_planned"] == planned, f"{label}: contadores visuales globales incoherentes")

    materials_root = paths["materials"].parent
    for relative in (
        "audios/README.md", "videos/README.md", "presentaciones/README.md",
        "infografias/README.md", "produccion/briefing.md",
        "produccion/fuentes.md", "produccion/prompts.md",
    ):
        add(errors, (materials_root / relative).exists(), f"{label}: falta scaffold de materiales {relative}")
    for part in materials["parts"]:
        exact_keys(errors, part, MATERIAL_PART_FIELDS, f"{label}/materiales/parte-{part.get('number')}")
        add(errors, bool(part.get("anchor_blocks")), f"{label}: parte multimedia sin anchor_blocks")
    for resource in materials["resources"]:
        exact_keys(errors, resource, MATERIAL_RESOURCE_FIELDS, f"{label}/material/{resource.get('id')}")
        exact_keys(errors, resource.get("storage", {}), MATERIAL_STORAGE_FIELDS, f"{label}/material/{resource.get('id')}/storage")

    return errors, warnings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--oposicion")
    parser.add_argument("--tema", type=int)
    args = parser.parse_args(argv)
    project = read_json(ROOT / "temario.json")
    errors: list[str] = []
    warnings: list[str] = []
    selected = []
    for opposition, info in project.get("oppositions", {}).items():
        for topic in info.get("topics", []):
            if args.oposicion and opposition != args.oposicion:
                continue
            if args.tema and int(topic["number"]) != args.tema:
                continue
            selected.append((opposition, topic))
    for opposition, topic in selected:
        topic_errors, topic_warnings = validate_topic(opposition, topic)
        errors.extend(topic_errors)
        warnings.extend(topic_warnings)
        if not topic_errors:
            print(
                f"OK contrato: {opposition}/tema-{int(topic['number']):02d}: "
                f"{topic['atomic_facts']} hechos; {topic['question_count']} preguntas; "
                f"{topic['visual_assets']} assets integrados"
            )
    for warning in warnings:
        print(f"AVISO: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"CONTRATO CORRECTO: {len(selected)} temas homologados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
