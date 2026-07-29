#!/usr/bin/env python3
"""Sincroniza los contadores de `temario.json` con las fuentes reales.

`temario.json` es un índice derivado: ningún contador suyo es dato primario.
Este script los recalcula desde los manifiestos, coberturas, bancos, índices
oficiales y manifiestos visuales de cada tema.

Sustituye a la lógica que vivía dentro de `homologar_temas_01_06.py`, que solo
cubría los temas 1 a 6. Este recorre todos los temas registrados, sea cual sea
la oposición.

    python scripts/sincronizar_temario.py --check   # no escribe; sale 1 si hay desvíos
    python scripts/sincronizar_temario.py --write   # corrige el índice
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "temario.json"

# Estados de asset que cuentan como recurso realmente integrado.
ACTIVE_ASSET_STATES = {"approved_internal", "integrated_webp", "published"}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def derived_values(opposition: str, topic: dict) -> dict:
    """Calcula el valor que debería tener cada campo derivado del índice."""
    number = int(topic["number"])
    code = f"tema-{number:02d}"

    knowledge = read_json(ROOT / topic["manifest"])
    coverage = read_json(ROOT / f"conocimiento/{opposition}/{code}/cobertura.json")
    official = read_json(ROOT / topic["official_exam_index"])
    assets = read_json(ROOT / topic["assets"])

    bank = ROOT / topic["question_bank"]
    questions = sum(
        1 for line in bank.read_text(encoding="utf-8").splitlines() if line.strip()
    )

    integrated = sum(
        resource["status"] in ACTIVE_ASSET_STATES for resource in assets["resources"]
    )
    planned = len(assets["resources"]) - integrated

    return {
        "content_version": knowledge["content_version"],
        "editorial_status": knowledge["editorial_status"],
        "publication_status": knowledge["publication_status"],
        "visual_version": assets["visual_version"],
        "visual_assets": integrated,
        "visual_planned": planned,
        "atomic_facts": len(coverage["facts"]),
        "question_count": questions,
        "official_exam_mapped": official["con_bloque_asignado"],
        "official_exam_verified": official["con_respuesta_verificada"],
        # `ha_caido_active` NO se deriva aquí a propósito. Marcar una aparición
        # como "ha caído" es una decisión editorial: exige que el bloque tenga
        # un callout :::ha-caido escrito y que la respuesta pueda mostrarse sin
        # presentarla como plantilla oficial (contrato único, §Antecedentes
        # oficiales). Se respeta el valor que ya tenga el índice.
    }


def sync(write: bool) -> int:
    data = read_json(INDEX)
    drift: list[str] = []

    for opposition, info in data.get("oppositions", {}).items():
        for topic in info.get("topics", []):
            label = f"{opposition}/tema-{int(topic['number']):02d}"
            for field, expected in derived_values(opposition, topic).items():
                current = topic.get(field)
                if current != expected:
                    drift.append(f"{label}: {field}: {current!r} -> {expected!r}")
                    topic[field] = expected

    if not drift:
        print("temario.json sincronizado: 0 desvíos")
        return 0

    for line in drift:
        print(("CORREGIDO " if write else "DESVÍO ") + line)

    if write:
        INDEX.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"\n{len(drift)} campos corregidos en temario.json")
        return 0

    print(f"\n{len(drift)} desvíos. Ejecuta: python scripts/sincronizar_temario.py --write")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="solo informa")
    group.add_argument("--write", action="store_true", help="corrige el índice")
    args = parser.parse_args()
    return sync(write=args.write)


if __name__ == "__main__":
    raise SystemExit(main())
