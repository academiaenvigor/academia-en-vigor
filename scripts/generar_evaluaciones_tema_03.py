#!/usr/bin/env python3
"""Genera evaluaciones reproducibles del Tema 3 en build/."""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "evaluaciones/policia-nacional/tema-03/plan.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_questions(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def balanced(items):
    groups = {letter: [q for q in items if q["respuesta_correcta"] == letter] for letter in "ABC"}
    output = []
    while any(groups.values()):
        for letter in "ABC":
            if groups[letter]:
                output.append(groups[letter].pop(0))
    return output


def public_test(test_id, title, blocks, items, test_type, version):
    return {
        "id": test_id,
        "titulo": title,
        "content_version": version,
        "bank_version": version,
        "tipo": test_type,
        "ambito": {"bloques": blocks},
        "numero_preguntas": len(items),
        "preguntas": [
            {key: q[key] for key in ("id", "fact_id", "bloque", "concepto", "articulo", "tipo", "dificultad", "enunciado", "opciones")}
            for q in items
        ],
        "soluciones": [
            {key: q[key] for key in ("id", "respuesta_correcta", "explicacion", "fact_id", "articulo")}
            for q in items
        ],
        "estado": "generado_validado",
        "publicacion": "not_published",
    }


def select_round_robin(questions, blocks, count, offset=0):
    pools = {block: balanced([q for q in questions if q["bloque"] == block]) for block in blocks}
    positions = {block: offset % len(pools[block]) for block in blocks}
    selected, used_facts = [], set()
    while len(selected) < count:
        added = False
        for block in blocks:
            pool = pools[block]
            for _ in range(len(pool)):
                question = pool[positions[block] % len(pool)]
                positions[block] += 1
                if question["fact_id"] not in used_facts:
                    selected.append(question)
                    used_facts.add(question["fact_id"])
                    added = True
                    break
            if len(selected) >= count:
                break
        if not added:
            break
    if len(selected) != count:
        raise RuntimeError(f"No se pudieron seleccionar {count} hechos únicos para {blocks}")
    return balanced(selected)


def main():
    plan = read_json(PLAN_PATH)
    version = plan["content_version"]
    bank_path = ROOT / plan["bank"]
    out = ROOT / plan["output"]
    questions = load_questions(bank_path)
    if out.exists():
        shutil.rmtree(out)

    catalogue, coverage_ids = [], []
    max_size = plan["coverage_tests"]["max_questions_per_test"]
    for block in plan["coverage_tests"]["blocks"]:
        number, title = block["number"], block["title"]
        pool = balanced([q for q in questions if q["bloque"] == number])
        for index in range(0, len(pool), max_size):
            chunk = pool[index:index + max_size]
            variant = chr(ord("A") + index // max_size)
            test_id = f"PN-T03-B{number:02d}-{variant}"
            relative = Path("por-bloques") / f"{test_id}.json"
            write_json(out / relative, public_test(test_id, f"Tema 3 · Bloque {number}: {title} · Test {variant}", [number], chunk, "cobertura_bloque", version))
            catalogue.append({"id": test_id, "ruta": relative.as_posix(), "tipo": "cobertura_bloque", "preguntas": len(chunk), "bloques": [number]})
            coverage_ids.extend(q["id"] for q in chunk)

    part_plan = plan["part_tests"]
    for part in part_plan["parts"]:
        for variant in part_plan["variants"]:
            items = select_round_robin(questions, part["blocks"], part_plan["questions_per_test"], variant["offset"])
            test_id = f"PN-T03-{part['code']}-{variant['id']}"
            relative = Path("por-partes") / f"{test_id}.json"
            write_json(out / relative, public_test(test_id, f"Tema 3 · Parte {part['code'][-1]} · {part['title']} · Test {variant['id']}", part["blocks"], items, "test_parte", version))
            catalogue.append({"id": test_id, "ruta": relative.as_posix(), "tipo": "test_parte", "preguntas": len(items), "bloques": part["blocks"]})

    for final in plan["final_tests"]:
        items = select_round_robin(questions, list(range(1, 26)), final["questions"], final["offset"])
        test_id = f"PN-T03-FINAL-{final['questions']}-{final['variant']}"
        relative = Path("finales") / f"{test_id}.json"
        write_json(out / relative, public_test(test_id, f"Tema 3 · Test final {final['variant']} · {final['questions']} preguntas", list(range(1, 26)), items, "test_final", version))
        catalogue.append({"id": test_id, "ruta": relative.as_posix(), "tipo": "test_final", "preguntas": len(items), "bloques": list(range(1, 26))})

    if Counter(coverage_ids) != Counter(q["id"] for q in questions):
        raise RuntimeError("Los tests de cobertura no contienen exactamente una vez todas las preguntas")

    write_json(out / "catalogo.json", {
        "content_version": version,
        "total_tests": len(catalogue),
        "tests_cobertura_bloque": sum(e["tipo"] == "cobertura_bloque" for e in catalogue),
        "tests_por_partes": sum(e["tipo"] == "test_parte" for e in catalogue),
        "tests_finales": sum(e["tipo"] == "test_final" for e in catalogue),
        "regla_cobertura": "Cada pregunta del banco aparece exactamente una vez en el conjunto de tests de cobertura por bloque.",
        "tests": catalogue,
    })
    print(f"OK: {len(catalogue)} tests generados; {len(coverage_ids)} preguntas cubiertas una vez")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
