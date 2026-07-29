#!/usr/bin/env python3
"""Marca como integrados los visuales finales del Tema 8."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-07-29"
VERSION = "1.0.0"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def integrate_assets() -> None:
    path = ROOT / "assets/policia-nacional/tema-08/manifest.json"
    data = load(path)
    data["content_version"] = VERSION
    data["visual_version"] = VERSION
    data["status"] = "integrated"
    data["totals"] = {"resources": 23, "integrated": 23, "planned": 0}
    data["integration_status"] = "complete"
    data["integrated_at"] = TODAY
    data["planned_resources"] = []

    for resource in data["resources"]:
        target = path.parent / resource["file"]
        if not target.is_file() or target.stat().st_size == 0:
            raise SystemExit(f"Falta el visual final: {target}")
        if target.stat().st_size > resource["max_bytes"]:
            raise SystemExit(f"Visual demasiado pesado: {target}")
        resource["status"] = "integrated_webp"
        resource["source_content_version"] = VERSION
        resource.pop("bytes", None)

    save(path, data)


def integrate_topic_manifest() -> None:
    path = ROOT / "conocimiento/policia-nacional/tema-08/manifest.json"
    data = load(path)
    data["visual_version"] = VERSION
    data["assets"]["total"] = 23
    data["assets"]["planned"] = 0
    data["review"]["visual"] = "complete_23_of_23"
    save(path, data)


def integrate_materials() -> None:
    path = ROOT / "materiales-didacticos/policia-nacional/tema-08/manifest.json"
    data = load(path)
    data["content_version"] = VERSION
    data["source_version"] = VERSION
    for resource in data["resources"]:
        resource["source_content_version"] = VERSION
    save(path, data)


def integrate_catalog() -> None:
    path = ROOT / "temario.json"
    data = load(path)
    topics = data["oppositions"]["policia-nacional"]["topics"]
    topic = next(item for item in topics if item["number"] == 8)
    topic["visual_version"] = VERSION
    topic["visual_assets"] = 23
    topic["visual_planned"] = 0
    topic["official_exam_mapped"] = 42
    topic["official_exam_verified"] = 42
    topic["ha_caido_active"] = 1
    save(path, data)


def main() -> None:
    integrate_assets()
    integrate_topic_manifest()
    integrate_materials()
    integrate_catalog()
    print("OK: 23 visuales integrados; Tema 8 actualizado a versión visual 1.0.0")


if __name__ == "__main__":
    main()
