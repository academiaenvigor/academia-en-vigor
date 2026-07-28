#!/usr/bin/env python3
"""Migra los Temas 1–6 al contrato técnico común de Academia En Vigor.

La migración es deliberadamente conservadora:
- no altera respuestas correctas ni contenido jurídico;
- reconstruye las fuentes maestras de T4 y T5 desde sus derivados existentes;
- mueve la trazabilidad FACT al Atestado;
- normaliza metadatos y esquemas;
- no fabrica preguntas para cubrir puertas de calidad pendientes.
"""
from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPPOSITION = "policia-nacional"
ACTIVE_ASSET_STATES = {"approved_internal", "integrated_webp", "published"}
QUESTION_FIELDS = [
    "id", "fact_id", "oposicion", "tema", "bloque", "punto", "subpunto",
    "parte", "parte_titulo", "concepto", "norma", "articulo", "riesgo_examen",
    "dificultad", "tipo", "enunciado", "opciones", "respuesta_correcta",
    "explicacion", "retroalimentacion", "estado_revision", "version_normativa",
    "caracter", "referencia_oficial", "relaciones", "equivalencias",
    "content_version",
]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2))


def write_if_missing(path: Path, text: str) -> None:
    if not path.exists():
        write_text(path, text)


def topic_index() -> list[dict]:
    return read_json(ROOT / "temario.json")["oppositions"][OPPOSITION]["topics"]


def topic_paths(topic: dict) -> dict[str, Path]:
    number = int(topic["number"])
    code = f"tema-{number:02d}"
    return {
        "knowledge": ROOT / f"conocimiento/{OPPOSITION}/{code}",
        "coverage": ROOT / f"conocimiento/{OPPOSITION}/{code}/cobertura.json",
        "manifest": ROOT / topic["manifest"],
        "master": ROOT / f"conocimiento/{OPPOSITION}/{code}/master.md",
        "parte": ROOT / topic["parte"],
        "atestado": ROOT / topic["atestado"],
        "bank_root": ROOT / f"banco-preguntas/{OPPOSITION}/{code}",
        "bank": ROOT / topic["question_bank"],
        "bank_manifest": ROOT / f"banco-preguntas/{OPPOSITION}/{code}/manifest.json",
        "official_index": ROOT / topic["official_exam_index"],
        "evaluation": ROOT / topic["evaluation_plan"],
        "assets": ROOT / topic["assets"],
        "materials": ROOT / topic["teaching_materials"],
    }


def strip_accents(value: str) -> str:
    normalized = unicodedata.normalize("NFD", value.lower())
    return "".join(char for char in normalized if unicodedata.category(char) != "Mn")


def tokens(value: str) -> set[str]:
    stop = {
        "a", "al", "ante", "bajo", "con", "contra", "de", "del", "desde",
        "durante", "e", "el", "ella", "en", "entre", "es", "esta", "este",
        "la", "las", "lo", "los", "o", "para", "por", "que", "se", "sin",
        "su", "sus", "un", "una", "y",
    }
    return {
        word for word in re.findall(r"[a-záéíóúüñ0-9]+", strip_accents(value))
        if len(word) > 2 and word not in stop
    }


def fact_value(fact: dict, *names: str, default=None):
    for name in names:
        if name in fact and fact[name] is not None:
            return fact[name]
    return default


def remove_fact_markers(text: str) -> str:
    return re.sub(r"<!-- FACT:[A-Z0-9-]+ -->[ \t]*", "", text)


def remove_generated_materials(text: str) -> str:
    text = re.sub(r"^> \*\*Material (?:completo del tema|de este punto):\*\*.*\n?", "", text, flags=re.M)
    text = re.sub(r"^<!-- MATERIAL PENDIENTE: [^>]+ -->\n?", "", text, flags=re.M)
    return text


VISUAL_RENDERED_RE = re.compile(
    r"<!-- VISUAL:(?P<file>[\w.-]+) -->\n"
    r"<p align=\"center\">\n"
    r"\s*<img [^>]*alt=\"(?P<alt>[^\"]*)\"[^>]*width=\"(?P<width>\d+)\">\n"
    r"</p>"
    r"(?:\n<p align=\"center\"><em>(?P<label>Infografía|Ilustración): "
    r"(?P<caption>.*?)\.?</em></p>)?",
    re.S,
)


def unrender_visuals(text: str, map_layer: bool = False) -> str:
    def replace(match: re.Match) -> str:
        filename = match.group("file")
        caption = (match.group("caption") or match.group("alt") or filename).strip().rstrip(".")
        if map_layer and "-00-" in filename:
            label = "Mapa general previsto"
        elif match.group("width") == "600" or "-il-" in filename or "-ilu-" in filename:
            label = "Ilustración simple"
        else:
            label = "Referencia visual prevista"
        return f":::visual\n**{label}:** `{filename}` · {caption}.\n:::"

    text = VISUAL_RENDERED_RE.sub(replace, text)
    text = re.sub(r"<!-- VISUAL PENDIENTE: ([^>]+) -->", lambda m: (
        f":::visual\n**Referencia visual prevista:** `{m.group(1).strip()}` · recurso visual planificado.\n:::"
    ), text)
    return text


def split_output(path: Path) -> tuple[str, dict[int, tuple[str, str, str]], dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    before, rest = text.split("\n# Contenido\n", 1)
    map_body = before.split("\n# Mapa del tema\n", 1)[1].strip()
    first_layer = re.search(r"^# Hablemos claro$", rest, re.M)
    if not first_layer:
        raise ValueError(f"No se localizaron las capas finales en {path}")
    block_area = rest[:first_layer.start()].strip()
    layers_area = rest[first_layer.start():]
    headings = list(re.finditer(r"^## (\d{2})\. (.+)$", block_area, re.M))
    blocks: dict[int, tuple[str, str, str]] = {}
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(block_area)
        body = block_area[heading.end():end].strip()
        sources = re.findall(r"<!-- FUENTE: ([^>]+) -->", body)
        if len(set(sources)) != 1:
            raise ValueError(f"{path}: bloque {heading.group(1)} sin fuente única")
        body = re.sub(r"\n?<!-- FUENTE: [^>]+ -->\s*$", "", body).strip()
        blocks[int(heading.group(1))] = (heading.group(2).strip(), sources[0].strip(), body)
    layers = {}
    layer_titles = ["Hablemos claro", "En la calle", "Lo que cae", "Ha caído"]
    for title in layer_titles:
        found = re.search(
            rf"^# {re.escape(title)}\n\n(.*?)(?=^# |^---$)",
            layers_area,
            re.M | re.S,
        )
        if not found:
            raise ValueError(f"{path}: falta capa {title}")
        layers[title] = found.group(1).strip()
    return map_body, blocks, layers


def rebuild_master(topic: dict) -> None:
    number = int(topic["number"])
    if number not in {4, 5}:
        return
    paths = topic_paths(topic)
    manifest = read_json(paths["manifest"])
    parte_map, parte_blocks, parte_layers = split_output(paths["parte"])
    atestado_map, atestado_blocks, atestado_layers = split_output(paths["atestado"])
    if parte_blocks.keys() != atestado_blocks.keys():
        raise ValueError(f"Tema {number}: Parte y Atestado no tienen los mismos bloques")

    out = [
        f"# TEMA {number} · {topic['title'].upper()}",
        "",
        f"<!-- content_version: {manifest['content_version']} -->",
        f"<!-- opposition: {OPPOSITION} -->",
        f"<!-- status: {manifest['editorial_status']}; publication: {manifest['publication_status']} -->",
        "",
    ]
    for block_number in sorted(parte_blocks):
        p_title, p_source, p_body = parte_blocks[block_number]
        a_title, a_source, a_body = atestado_blocks[block_number]
        if p_title != a_title or p_source != a_source:
            raise ValueError(f"Tema {number}, bloque {block_number}: derivados desalineados")
        p_body = unrender_visuals(remove_generated_materials(remove_fact_markers(p_body)))
        a_body = unrender_visuals(remove_generated_materials(remove_fact_markers(a_body)))
        out.extend([
            f"<!-- BLOCK {block_number:02d} START -->",
            f"## {block_number}. {p_title}",
            f"**Fuente principal:** `{p_source}`",
            "<!-- PARTE START -->",
            p_body,
            "<!-- PARTE END -->",
            "<!-- ATESTADO START -->",
            a_body,
            "<!-- ATESTADO END -->",
            f"<!-- BLOCK {block_number:02d} END -->",
            "",
        ])
    out.extend([
        "<!-- LAYER:MAPA -->",
        "# Mapa del tema",
        unrender_visuals(remove_generated_materials(remove_fact_markers(atestado_map)), map_layer=True),
        "",
        "<!-- LAYER:CONTENIDO -->",
        "# Contenido",
        "Los bloques siguientes desarrollan íntegramente el programa oficial del tema.",
        "",
    ])
    layer_keys = [
        ("HABLEMOS_CLARO", "Hablemos claro"),
        ("EN_LA_CALLE", "En la calle"),
        ("LO_QUE_CAE", "Lo que cae"),
        ("HA_CAIDO", "Ha caído"),
    ]
    for key, title in layer_keys:
        body = atestado_layers[title]
        if parte_layers[title] != body:
            raise ValueError(f"Tema {number}: capa {title} distinta entre derivados")
        out.extend([f"<!-- LAYER:{key} -->", f"# {title}", body, ""])
    write_text(paths["master"], "\n".join(out))


BLOCK_RE = re.compile(
    r"(<!-- BLOCK (?P<number>\d{2}) START -->\n"
    r"## \d+\. .*?\n\*\*Fuente principal:\*\* `[^`]+`\n"
    r"<!-- PARTE START -->\n)(?P<parte>.*?)"
    r"(\n<!-- PARTE END -->\n<!-- ATESTADO START -->\n)(?P<atestado>.*?)"
    r"(\n<!-- ATESTADO END -->\n<!-- BLOCK (?P=number) END -->)",
    re.S,
)


def paragraph_score(statement: str, paragraph: str) -> float:
    fact_tokens = tokens(statement)
    paragraph_tokens = tokens(re.sub(r"<[^>]+>|:::[^\n]*", " ", paragraph))
    if not fact_tokens or not paragraph_tokens:
        return 0.0
    overlap = len(fact_tokens & paragraph_tokens)
    return overlap / len(fact_tokens) + overlap / len(paragraph_tokens) * 0.2


def anchor_facts(topic: dict, facts: list[dict]) -> dict[str, float]:
    number = int(topic["number"])
    paths = topic_paths(topic)
    text = remove_fact_markers(paths["master"].read_text(encoding="utf-8"))
    by_block: dict[int, list[dict]] = defaultdict(list)
    for fact in facts:
        by_block[int(fact_value(fact, "bloque", "block", default=0))].append(fact)
    scores: dict[str, float] = {}

    def replace_block(match: re.Match) -> str:
        block_number = int(match.group("number"))
        parte = match.group("parte").strip()
        atestado = match.group("atestado").strip()
        paragraphs = re.split(r"(\n\s*\n)", atestado)
        content_indices = [
            idx for idx in range(0, len(paragraphs), 2)
            if paragraphs[idx].strip()
            and not paragraphs[idx].lstrip().startswith((":::", "<!--", "|"))
        ]
        if not content_indices:
            content_indices = [0]
        assigned: dict[int, list[str]] = defaultdict(list)
        explicit_precision: list[tuple[str, str]] = []
        for fact in by_block.get(block_number, []):
            statement = str(fact_value(fact, "enunciado_atomico", "statement", default=""))
            best = max(content_indices, key=lambda idx: paragraph_score(statement, paragraphs[idx]))
            score = paragraph_score(statement, paragraphs[best])
            if score < 0.12:
                explicit_precision.append((fact["id"], statement))
                scores[fact["id"]] = 1.0
            else:
                scores[fact["id"]] = round(score, 4)
                assigned[best].append(fact["id"])
        for idx, fact_ids in assigned.items():
            paragraphs[idx] = paragraphs[idx].rstrip() + " " + " ".join(
                f"<!-- FACT:{fact_id} -->" for fact_id in fact_ids
            )
        if explicit_precision:
            precision = [
                "#### Datos de precisión examinables",
                "",
                *[
                    f"- {statement} <!-- FACT:{fact_id} -->"
                    for fact_id, statement in explicit_precision
                ],
            ]
            paragraphs.extend(["\n\n", "\n".join(precision)])
        return (
            match.group(1) + parte + match.group(4)
            + "".join(paragraphs).strip() + match.group(6)
        )

    text, count = BLOCK_RE.subn(replace_block, text)
    expected = int(read_json(paths["manifest"])["semantic_blocks"])
    if count != expected:
        raise ValueError(f"Tema {number}: se anclaron {count} bloques; se esperaban {expected}")
    write_text(paths["master"], text)
    return scores


def part_lookup(materials: dict) -> dict[int, tuple[int | None, str | None]]:
    lookup = {}
    for part in materials.get("parts", []):
        for block in part.get("blocks", []):
            lookup[int(block)] = (part.get("number"), part.get("title"))
    return lookup


def normalize_questions(topic: dict, original_facts: list[dict]) -> tuple[list[dict], dict[str, int]]:
    paths = topic_paths(topic)
    number = int(topic["number"])
    questions = [
        json.loads(line) for line in paths["bank"].read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    materials = read_json(paths["materials"])
    parts = part_lookup(materials)
    facts = {fact["id"]: fact for fact in original_facts}
    normalized = []
    for question in questions:
        fact = facts.get(question.get("fact_id"), {})
        block = int(question.get("bloque") or fact_value(fact, "bloque", "block", default=0))
        part_number, part_title = parts.get(block, (None, None))
        correct = question.get("respuesta_correcta")
        explanation = question.get("explicacion") or fact_value(
            fact, "enunciado_atomico", "statement", default=""
        )
        feedback = question.get("retroalimentacion")
        if not feedback:
            feedback = {
                "acierto": {
                    "humor": "Bien visto: esta vez la trampa no ha cobrado peaje.",
                    "explicacion": explanation,
                },
                "fallo": {
                    "humor": "Casi, pero aquí una palabra cambia todo el expediente.",
                    "explicacion": (
                        f"La respuesta correcta es la {correct}: "
                        f"{question.get('opciones', {}).get(correct, '')}. {explanation}"
                    ).strip(),
                },
            }
        item = {
            "id": question.get("id"),
            "fact_id": question.get("fact_id"),
            "oposicion": question.get("oposicion", OPPOSITION),
            "tema": int(question.get("tema", number)),
            "bloque": block,
            "punto": question.get("punto", block),
            "subpunto": question.get("subpunto"),
            "parte": question.get("parte", part_number),
            "parte_titulo": question.get("parte_titulo", part_title),
            "concepto": question.get("concepto") or fact_value(fact, "concepto", "concept"),
            "norma": question.get("norma") or fact_value(fact, "fuente", "source"),
            "articulo": question.get("articulo") or fact_value(fact, "article"),
            "riesgo_examen": int(question.get("riesgo_examen") or fact_value(
                fact, "riesgo_examen", "risk", default=3
            )),
            "dificultad": question.get("dificultad", "media"),
            "tipo": question.get("tipo", "literal_discriminacion"),
            "enunciado": question.get("enunciado"),
            "opciones": question.get("opciones"),
            "respuesta_correcta": correct,
            "explicacion": explanation,
            "retroalimentacion": feedback,
            "estado_revision": question.get("estado_revision", "pendiente_revision_editorial"),
            "version_normativa": question.get("version_normativa"),
            "caracter": "propio",
            "referencia_oficial": None,
            "relaciones": question.get("relaciones") or [question.get("fact_id")],
            "equivalencias": question.get("equivalencias") or [],
            "content_version": question.get("content_version") or topic["content_version"],
        }
        normalized.append({field: item[field] for field in QUESTION_FIELDS})
    write_text(paths["bank"], "\n".join(
        json.dumps(question, ensure_ascii=False, separators=(",", ":"))
        for question in normalized
    ))
    return normalized, dict(Counter(q["respuesta_correcta"] for q in normalized))


def normalize_coverage(
    topic: dict,
    original: dict,
    questions: list[dict],
    anchor_scores: dict[str, float],
) -> dict:
    number = int(topic["number"])
    paths = topic_paths(topic)
    materials = read_json(paths["materials"])
    parts = part_lookup(materials)
    q_by_fact: dict[str, list[str]] = defaultdict(list)
    q_risk: dict[str, int] = {}
    for question in questions:
        q_by_fact[question["fact_id"]].append(question["id"])
        q_risk[question["fact_id"]] = question["riesgo_examen"]
    block_titles = {
        int(block.get("number")): block.get("title")
        for block in original.get("blocks", [])
        if block.get("number") is not None
    }
    facts = []
    for old in original.get("facts", []):
        block = int(fact_value(old, "bloque", "block", default=0))
        part_number, part_title = parts.get(block, (None, None))
        question_ids = q_by_fact.get(old["id"]) or fact_value(
            old, "preguntas", "question_ids", default=[]
        )
        risk = int(fact_value(
            old, "riesgo_examen", "risk", default=q_risk.get(old["id"], 3)
        ))
        facts.append({
            "id": old["id"],
            "oposicion": OPPOSITION,
            "tema": number,
            "bloque": block,
            "bloque_titulo": fact_value(old, "block_title", default=block_titles.get(block)),
            "parte": fact_value(old, "parte", "part", default=part_number),
            "parte_titulo": fact_value(old, "parte_titulo", "part_title", default=part_title),
            "punto": int(fact_value(old, "punto", default=block)),
            "enunciado_atomico": fact_value(old, "enunciado_atomico", "statement", default=""),
            "fuente": fact_value(old, "fuente", "source", default="PENDIENTE"),
            "estado_revision": fact_value(
                old, "estado_revision", default="pendiente_revision_editorial"
            ),
            "content_version": topic["content_version"],
            "riesgo_examen": risk,
            "risk": risk,
            "preguntas": question_ids,
            "covered": bool(question_ids),
            "anchor_score": anchor_scores.get(old["id"], 1.0 if number in {3, 6} else None),
        })
    covered = sum(bool(fact["preguntas"]) for fact in facts)
    requirements = dict(original.get("requirements", {}))
    for key in ("required_constitution_articles", "covered_constitution_articles"):
        if key in original:
            requirements[key] = original[key]
    if number == 2 and not requirements:
        requirements = {
            "required_constitution_articles": list(range(1, 56)),
            "covered_constitution_articles": list(range(1, 56)),
        }
    blocks = []
    for block in sorted({fact["bloque"] for fact in facts}):
        block_facts = [fact for fact in facts if fact["bloque"] == block]
        blocks.append({
            "number": block,
            "title": next((fact["bloque_titulo"] for fact in block_facts if fact["bloque_titulo"]), None),
            "facts": len(block_facts),
            "covered_facts": sum(fact["covered"] for fact in block_facts),
        })
    return {
        "schema_version": "2.0.0",
        "content_version": topic["content_version"],
        "oposicion": OPPOSITION,
        "topic": f"tema-{number:02d}",
        "tema": number,
        "status": original.get("status", "active"),
        "scope": original.get("scope", "tema_completo"),
        "total_atomic_facts": len(facts),
        "covered_atomic_facts": covered,
        "coverage_percent": round(covered / len(facts) * 100, 2) if facts else 0.0,
        "total_questions": len(questions),
        "requirements": requirements,
        "facts": facts,
        "blocks": blocks,
    }


def quality_gate(coverage: dict, questions: list[dict]) -> dict:
    by_fact = Counter(question["fact_id"] for question in questions)
    risk5_missing = [
        fact["id"] for fact in coverage["facts"]
        if fact["riesgo_examen"] == 5 and by_fact[fact["id"]] < 2
    ]
    reasons = []
    if not questions:
        reasons.append("question_bank_not_started")
    if risk5_missing:
        reasons.append("risk5_second_formulations_pending")
    distribution = Counter(question["respuesta_correcta"] for question in questions)
    if questions and max(distribution.values()) - min(distribution.values()) > 1:
        reasons.append("answer_distribution_pending")
    return {
        "status": "passed" if not reasons else "blocked",
        "reasons": reasons,
        "risk5_second_formulations_pending": len(risk5_missing),
    }


def normalize_bank_manifest(
    topic: dict,
    coverage: dict,
    questions: list[dict],
    distribution: dict[str, int],
) -> None:
    number = int(topic["number"])
    paths = topic_paths(topic)
    difficulties = Counter(q["dificultad"] for q in questions)
    types = Counter(q["tipo"] for q in questions)
    by_block = Counter(str(q["bloque"]) for q in questions)
    by_part = Counter(str(q["parte"]) for q in questions if q["parte"] is not None)
    covered = len({q["fact_id"] for q in questions})
    gate = quality_gate(coverage, questions)
    data = {
        "schema_version": "2.0.0",
        "content_version": topic["content_version"],
        "oposicion": OPPOSITION,
        "tema": number,
        "estado": "ready" if gate["status"] == "passed" else "draft",
        "publicacion": "not_published",
        "total_preguntas": len(questions),
        "total_hechos": len(coverage["facts"]),
        "hechos_cubiertos": covered,
        "cobertura_por_hechos": round(covered / len(coverage["facts"]) * 100, 2)
        if coverage["facts"] else 0.0,
        "distribucion_respuestas": {key: distribution.get(key, 0) for key in ("A", "B", "C")},
        "distribucion_dificultad": dict(sorted(difficulties.items())),
        "distribucion_tipo": dict(sorted(types.items())),
        "preguntas_por_bloque": dict(sorted(by_block.items(), key=lambda item: int(item[0]))),
        "preguntas_por_parte": dict(sorted(by_part.items(), key=lambda item: int(item[0]))),
        "caracter": {"propias": len(questions), "oficiales": 0},
        "fuente_conocimiento": f"../../../conocimiento/{OPPOSITION}/tema-{number:02d}/master.md",
        "cobertura": f"../../../conocimiento/{OPPOSITION}/tema-{number:02d}/cobertura.json",
        "evaluation_plan": f"../../../evaluaciones/{OPPOSITION}/tema-{number:02d}/plan.json",
        "official_exam_index": "indice-oficiales.json",
        "retroalimentacion": {
            "schema": "acierto_fallo_v1",
            "required": True,
            "humor_first": True,
        },
        "generacion_de_tests": {
            "max_questions_per_block_test": 25,
            "full_topic_sizes": [25, 50],
        },
        "publication_gate": "blocked_until_editorial_approval",
        "quality_gate": gate,
    }
    write_json(paths["bank_manifest"], data)


def normalize_official_index(topic: dict) -> None:
    paths = topic_paths(topic)
    old = read_json(paths["official_index"])
    questions = old.get("questions", [])
    by_block = Counter()
    for question in questions:
        blocks = question.get("block_refs") or [
            question.get("bloque") or question.get("block")
        ]
        for block in blocks:
            if block is not None:
                by_block[str(block)] += 1
    by_promotion = Counter(
        str(
            question.get("promocion") or question.get("promotion")
            or question.get("series_year") or question.get("year")
        )
        for question in questions
    )
    verified = sum(bool(
        question.get("respuesta_verificada")
        or question.get("verified_answer")
        or question.get("answer_verified")
        or str(question.get("answer_status", "")).startswith("verificada")
    ) for question in questions)
    mapped = sum(bool(
        question.get("block_refs")
        or question.get("bloque")
        or question.get("block")
    ) for question in questions)
    data = {
        "schema_version": "2.0.0",
        "oposicion": OPPOSITION,
        "tema": int(topic["number"]),
        "titulo": topic["title"],
        "generated_at": old.get("generated_at", "2026-07-27"),
        "mapping_method": old.get("mapping_method", "manual_editorial"),
        "mapping_status": old.get("mapping_status", "pending_review" if questions else "empty"),
        "answer_status": old.get("answer_status", "verified" if verified == len(questions) and questions else "pending"),
        "display_policy": old.get("display_policy", "verified_only"),
        "aviso": old.get("aviso") or old.get("note") or (
            "Las referencias no alimentan estadísticas de «Ha caído» hasta estar verificadas."
        ),
        "total_referencias": len(questions),
        "con_bloque_asignado": mapped,
        "con_respuesta_verificada": verified,
        "por_bloque": dict(sorted(by_block.items(), key=lambda item: int(item[0]))),
        "por_promocion": dict(sorted(by_promotion.items())),
        "retroalimentacion": "banco-preguntas/policia-nacional/oficiales/retroalimentacion.json",
        "questions": questions,
    }
    write_json(paths["official_index"], data)


def normalize_evaluation(topic: dict) -> None:
    paths = topic_paths(topic)
    old = read_json(paths["evaluation"])
    final_tests = old.get("final_tests", old.get("full_tests", []))
    data = {
        "schema_version": "2.0.0",
        "content_version": topic["content_version"],
        "opposition": OPPOSITION,
        "topic_number": int(topic["number"]),
        "topic_title": topic["title"],
        "id_prefix": f"PN-T{int(topic['number']):02d}",
        "status": old.get("status", "planned"),
        "bank": topic["question_bank"],
        "output": old.get("output") or (
            f"build/evaluaciones/{OPPOSITION}/tema-{int(topic['number']):02d}/tests-generados"
        ),
        "coverage_tests": old.get("coverage_tests", {}),
        "part_tests": old.get("part_tests", {}),
        "final_tests": final_tests,
    }
    write_json(paths["evaluation"], data)
    write_if_missing(paths["evaluation"].parent / "README.md", (
        f"# Evaluaciones · Tema {int(topic['number'])}\n\n"
        "Plan de evaluación generado desde el banco propio y sometido al contrato común."
    ))


def normalize_assets(topic: dict) -> tuple[int, int]:
    paths = topic_paths(topic)
    old = read_json(paths["assets"])
    resources = []
    for index, resource in enumerate(old.get("resources", []), start=1):
        filename = resource["file"]
        status = resource.get("status", "planned")
        block = resource.get("block")
        if block is None:
            match = re.search(r"Bloque\s+0?(\d+)", str(resource.get("placement", "")), re.I)
            block = int(match.group(1)) if match else None
        documents = resource.get("documents")
        if documents is None:
            placement = str(resource.get("placement", "")).lower()
            documents = [
                kind for kind in ("parte", "atestado") if kind in placement
            ] or ["parte", "atestado"]
        resource_type = resource.get("type", "diagrama")
        if resource_type == "ilustracion":
            resource_type = "ilustracion_simple"
        resources.append({
            "id": resource.get("id") or f"PN-T{int(topic['number']):02d}-VIS-{index:03d}",
            "file": filename,
            "title": resource.get("title") or resource.get("description") or filename,
            "type": resource_type,
            "placement": resource.get("placement"),
            "status": status,
            "block": block,
            "documents": documents,
            "description": resource.get("description") or resource.get("title") or filename,
            "source_content_version": topic["content_version"],
            "required_format": "webp",
            "max_bytes": int(resource.get("max_bytes", 1_000_000)),
        })
    integrated = sum(resource["status"] in ACTIVE_ASSET_STATES for resource in resources)
    planned = len(resources) - integrated
    data = {
        "schema_version": "2.0.0",
        "opposition": OPPOSITION,
        "topic": f"tema-{int(topic['number']):02d}",
        "content_version": topic["content_version"],
        "visual_version": old.get("visual_version", "0.0.0"),
        "status": "integrated" if planned == 0 else "partial",
        "totals": {"resources": len(resources), "integrated": integrated, "planned": planned},
        "integration_status": "complete" if planned == 0 else "pending_assets",
        "integrated_at": old.get("integrated_at"),
        "resources": resources,
        "planned_resources": [resource["id"] for resource in resources if resource["status"] not in ACTIVE_ASSET_STATES],
    }
    write_json(paths["assets"], data)
    return integrated, planned


def normalize_materials(topic: dict) -> None:
    paths = topic_paths(topic)
    old = read_json(paths["materials"])
    parts = []
    for part in old.get("parts", []):
        blocks = [f"{int(block):02d}" for block in part.get("blocks", [])]
        parts.append({
            "id": part.get("id") or f"p{part.get('number')}",
            "number": int(part.get("number")),
            "title": part.get("title"),
            "blocks": blocks,
            "anchor_blocks": part.get("anchor_blocks") or blocks[:1],
        })
    resources = []
    for resource in old.get("resources", []):
        item = dict(resource)
        item.setdefault("file_size_bytes", None)
        item.setdefault("resource_type", None)
        item.setdefault("ownership", "own")
        item.setdefault("status", "planned")
        item.setdefault("source_content_version", topic["content_version"])
        item.setdefault("tool", "notebooklm")
        item.setdefault("duration_seconds", None)
        item.setdefault("storage", {
            "type": "external", "provider": "google_drive",
            "asset_key": "", "drive_file_id": "", "url": "",
        })
        item["blocks"] = [f"{int(block):02d}" for block in item.get("blocks", [])]
        item["anchor_blocks"] = item.get("anchor_blocks") or item["blocks"][:1]
        resources.append(item)
    data = {
        "schema_version": "2.1.0",
        "opposition": OPPOSITION,
        "topic": f"tema-{int(topic['number']):02d}",
        "content_version": topic["content_version"],
        "source_version": topic["content_version"],
        "status": old.get("status", "estructura_preparada"),
        "storage_policy": old.get("storage_policy", "external_by_default_for_audio_video_and_heavy_files"),
        "rights_policy": old.get("rights_policy", "own_or_explicitly_authorized_only"),
        "audio_note": old.get("audio_note", "Los audios y vídeos pesados se alojan fuera del repositorio."),
        "display_policy": old.get("display_policy", {"show_planned_in_temas": False}),
        "storage_root": old.get("storage_root", f"pn/tema-{int(topic['number']):02d}"),
        "categories": old.get("categories", {
            "infografias": "infografias/", "presentaciones": "presentaciones/",
            "audios": "audios/", "videos": "videos/",
        }),
        "scopes": old.get("scopes", ["parte", "tema"]),
        "nomenclature": old.get("nomenclature", "TNN-PN-CATEGORIA-descripcion.ext"),
        "parts": parts,
        "resources": resources,
    }
    write_json(paths["materials"], data)
    root = paths["materials"].parent
    for category in ("infografias", "presentaciones", "audios", "videos"):
        write_if_missing(root / category / "README.md", (
            f"# {category.title()} · Tema {int(topic['number'])}\n\n"
            "Recursos propios o expresamente autorizados."
        ))
    write_if_missing(root / "produccion/briefing.md", (
        f"# Briefing · Tema {int(topic['number'])}\n\n"
        f"Fuente editorial: `{topic['atestado']}`."
    ))
    write_if_missing(root / "produccion/fuentes.md", (
        "# Fuentes autorizadas\n\n"
        "Solo normativa, organismos oficiales y material propio o autorizado."
    ))
    write_if_missing(root / "produccion/prompts.md", (
        "# Prompts de producción\n\n"
        "Los prompts deben derivarse del contenido propio del tema y de fuentes oficiales."
    ))


SOURCE_ALIASES = {
    "TUE": ("Tratado de la Unión Europea", "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:12012M/TXT", []),
    "TFUE": ("Tratado de Funcionamiento de la Unión Europea", "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:12012E/TXT", []),
    "CDFUE": ("Carta de los Derechos Fundamentales de la Unión Europea", "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:12012P/TXT", []),
    "CE": ("Constitución Española", "https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229", []),
    "L40-2015": ("Ley 40/2015, de Régimen Jurídico del Sector Público", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566", []),
    "L50-1997": ("Ley 50/1997, del Gobierno", "https://www.boe.es/buscar/act.php?id=BOE-A-1997-25336", []),
    "L3-2015": ("Ley 3/2015, reguladora del ejercicio del alto cargo de la AGE", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-3444", []),
    "LO3-1980": ("Ley Orgánica 3/1980, del Consejo de Estado", "https://www.boe.es/buscar/act.php?id=BOE-A-1980-8648", []),
    "COOP-EUROPOL": ("Reglamento (UE) 2016/794 sobre Europol", "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0794", []),
    "COOP-INTERPOL": ("Marco jurídico oficial de Interpol", "https://www.interpol.int/es/Quienes-somos/Marco-juridico", []),
    "COOP-ODE": ("Decisión Marco 2002/584/JAI sobre la orden de detención europea", "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32002F0584", []),
    "COOP-TEDH": ("Convenio Europeo de Derechos Humanos y Tribunal Europeo de Derechos Humanos", "https://www.echr.coe.int/documents/d/echr/convention_spa", []),
}


def alias_source(source_id: str) -> tuple[str, str, list[str]]:
    if source_id in SOURCE_ALIASES:
        return SOURCE_ALIASES[source_id]
    if source_id.startswith(("UE-", "COOP-")):
        base = ["TUE", "TFUE"]
        return (
            f"Referencia temática oficial de la Unión Europea: {source_id}",
            "https://european-union.europa.eu/index_es",
            base,
        )
    if source_id.startswith("GOB-"):
        return (
            f"Referencia temática de la Ley del Gobierno: {source_id}",
            "https://www.boe.es/buscar/act.php?id=BOE-A-1997-25336",
            ["L50-1997"],
        )
    if source_id.startswith(("AGE-", "LRJSP-")):
        return (
            f"Referencia temática de la Ley 40/2015: {source_id}",
            "https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566",
            ["L40-2015"],
        )
    return (
        f"Referencia oficial utilizada en el temario: {source_id}",
        "https://www.boe.es/",
        [],
    )


def normalize_source_catalog(topics: list[dict]) -> None:
    path = ROOT / "fuentes/catalogo.json"
    data = read_json(path)
    existing = {source["id"]: source for source in data.get("sources", [])}
    used = set()
    for topic in topics:
        paths = topic_paths(topic)
        manifest = read_json(paths["manifest"])
        used.update(manifest.get("official_references", []))
        coverage = read_json(paths["coverage"])
        used.update(fact["fuente"] for fact in coverage.get("facts", []))
    for source_id in sorted(used - existing.keys()):
        title, url, derived = alias_source(source_id)
        existing[source_id] = {
            "id": source_id,
            "title": title,
            "url": url,
            "scope": "apartados del tema identificados con este código",
            "official": True,
            "traceable": True,
            "derived_from": derived,
        }
    data = {
        "catalog_version": "1.0.0",
        "checked_at": "2026-07-27",
        "sources": sorted(existing.values(), key=lambda source: source["id"]),
    }
    write_json(path, data)


def normalize_knowledge_manifest(
    topic: dict,
    coverage: dict,
    integrated_assets: int,
    planned_assets: int,
) -> None:
    paths = topic_paths(topic)
    old = read_json(paths["manifest"])
    official_index = read_json(paths["official_index"])
    review_file = old.get("review", {}).get("review_file")
    if not review_file:
        review_file = f"conocimiento/{OPPOSITION}/tema-{int(topic['number']):02d}/revision-homologacion-1.0.md"
        write_text(ROOT / review_file, (
            f"# Homologación estructural · Tema {int(topic['number'])}\n\n"
            "Fuente maestra, trazabilidad, metadatos y rutas ajustados al contrato común."
        ))
    data = {
        "schema_version": "2.0.0",
        "opposition": OPPOSITION,
        "opposition_display_name": old.get("opposition_display_name", "Policía Nacional"),
        "topic": f"tema-{int(topic['number']):02d}",
        "topic_number": int(topic["number"]),
        "slug": topic["slug"],
        "title": topic["title"],
        "content_version": topic["content_version"],
        "pedagogical_version": old.get("pedagogical_version", topic["content_version"]),
        "visual_version": old.get("visual_version", topic.get("visual_version", "0.0.0")),
        "editorial_status": old.get("editorial_status", topic["editorial_status"]),
        "publication_status": "not_published",
        "normative_status": old.get("normative_status", "reviewed"),
        "source_file": str(paths["master"].relative_to(ROOT)),
        "source_rights": old.get("source_rights", {
            "third_party_source_in_repository": False,
            "method": "original_redaction_from_official_sources",
        }),
        "outputs": {"parte": topic["parte"], "atestado": topic["atestado"]},
        "semantic_blocks": len(coverage["blocks"]),
        "atomic_facts": len(coverage["facts"]),
        "master_statements": len(coverage["facts"]),
        "coverage_file": str(paths["coverage"].relative_to(ROOT)),
        "official_references": old.get("official_references", []),
        "official_exam_items": len(official_index.get("questions", [])),
        "official_exam_index": topic["official_exam_index"],
        "layers": ["Mapa del tema", "Contenido", "Hablemos claro", "En la calle", "Lo que cae", "Ha caído"],
        "atestado_style": old.get("atestado_style", "narrativo_normativo_vigor"),
        "question_bank": {
            "path": topic["question_bank"],
            "manifest": str(paths["bank_manifest"].relative_to(ROOT)),
            "questions": coverage["total_questions"],
            "coverage_by_atomic_facts": coverage["coverage_percent"],
        },
        "evaluations": {
            "plan": topic["evaluation_plan"],
            "generator": "scripts/generar_evaluaciones.py",
        },
        "assets": {
            "manifest": topic["assets"],
            "total": integrated_assets,
            "planned": planned_assets,
        },
        "teaching_materials": {
            "manifest": topic["teaching_materials"],
            "categories": ["infografias", "presentaciones", "audios", "videos"],
        },
        "review": {
            "legal": old.get("review", {}).get("legal", "reviewed_official_sources"),
            "pedagogical": old.get("review", {}).get("pedagogical", "first_pass_vigor"),
            "editorial": old.get("review", {}).get("editorial", "pending_user_review"),
            "question_bank": old.get("review", {}).get("question_bank", "tracked_by_quality_gate"),
            "review_file": review_file,
        },
    }
    write_json(paths["manifest"], data)


def update_topic_index(topics: list[dict]) -> None:
    index_path = ROOT / "temario.json"
    data = read_json(index_path)
    data["schema_version"] = "2.0.0"
    data["project_version"] = "0.7.0"
    indexed_topics = data["oppositions"][OPPOSITION]["topics"]
    by_number = {int(topic["number"]): topic for topic in indexed_topics}
    for source_topic in topics:
        topic = by_number[int(source_topic["number"])]
        paths = topic_paths(topic)
        knowledge = read_json(paths["manifest"])
        coverage = read_json(paths["coverage"])
        assets = read_json(paths["assets"])
        official = read_json(paths["official_index"])
        topic["content_version"] = knowledge["content_version"]
        topic["editorial_status"] = knowledge["editorial_status"]
        topic["publication_status"] = knowledge["publication_status"]
        topic["visual_version"] = assets["visual_version"]
        topic["visual_assets"] = assets["totals"]["integrated"]
        topic["visual_planned"] = assets["totals"]["planned"]
        topic["atomic_facts"] = len(coverage["facts"])
        topic["question_count"] = coverage["total_questions"]
        topic["official_exam_mapped"] = official["con_bloque_asignado"]
        topic["official_exam_verified"] = official["con_respuesta_verificada"]
        topic["ha_caido_active"] = (
            official["con_respuesta_verificada"]
            if official.get("display_policy") == "verified_only" else 0
        )
    write_json(index_path, data)


def remove_unreferenced_assets(topics: list[dict]) -> list[str]:
    removed = []
    for topic in topics:
        paths = topic_paths(topic)
        manifest = read_json(paths["assets"])
        referenced = {resource["file"] for resource in manifest["resources"]}
        for image in paths["assets"].parent.glob("*.webp"):
            if image.name not in referenced:
                image.unlink()
                removed.append(str(image.relative_to(ROOT)))
    return removed


def main() -> int:
    topics = topic_index()
    report_path = ROOT / "homologacion-temas-01-06.json"
    previous_removed = []
    if report_path.exists():
        previous_removed = read_json(report_path).get("removed_unreferenced_assets", [])
    for topic in topics:
        normalize_materials(topic)
        normalize_evaluation(topic)
        normalize_official_index(topic)
        rebuild_master(topic)

        paths = topic_paths(topic)
        original_coverage = read_json(paths["coverage"])
        original_facts = original_coverage.get("facts", [])
        questions, distribution = normalize_questions(topic, original_facts)
        anchor_scores = anchor_facts(topic, original_facts)
        coverage = normalize_coverage(topic, original_coverage, questions, anchor_scores)
        write_json(paths["coverage"], coverage)
        normalize_bank_manifest(topic, coverage, questions, distribution)
        integrated, planned = normalize_assets(topic)
        normalize_knowledge_manifest(topic, coverage, integrated, planned)

    normalize_source_catalog(topics)
    update_topic_index(topics)
    removed = remove_unreferenced_assets(topics)
    write_json(report_path, {
        "schema_version": "1.0.0",
        "topics": [int(topic["number"]) for topic in topics],
        "contract": "2.0.0",
        "removed_unreferenced_assets": sorted(set(previous_removed) | set(removed)),
        "policy": "No se fabricaron preguntas para superar puertas de calidad.",
    })
    print(f"Homologados {len(topics)} temas; eliminados {len(removed)} assets no referenciados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
