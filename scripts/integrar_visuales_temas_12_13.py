#!/usr/bin/env python3
"""Integra los PNG maestros de los Temas 12 y 13 como WEBP optimizados."""
from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
MAX_BYTES = 1_000_000
TARGET_BYTES = 950_000
INTEGRATED_AT = "2026-07-30"


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def save_webp(source: Path, destination: Path) -> tuple[int, int, int]:
    with Image.open(source) as original:
        image = original.convert("RGB")
    if image.width > 1800:
        height = round(image.height * 1800 / image.width)
        image = image.resize((1800, height), Image.Resampling.LANCZOS)
    temporary = Path(tempfile.gettempdir()) / "vigor-t12-t13-webp" / destination.name
    temporary.parent.mkdir(parents=True, exist_ok=True)
    quality = 84
    while True:
        image.save(temporary, "WEBP", quality=quality, method=6, optimize=True)
        size = temporary.stat().st_size
        if 0 < size <= TARGET_BYTES:
            with Image.open(temporary) as check:
                check.verify()
            destination.write_bytes(temporary.read_bytes())
            return size, image.width, image.height
        if quality > 58:
            quality -= 4
        elif image.width > 1280:
            width = max(1280, round(image.width * 0.9))
            image = image.resize(
                (width, round(image.height * width / image.width)),
                Image.Resampling.LANCZOS,
            )
            quality = 72
        else:
            raise RuntimeError(f"No se pudo optimizar {destination.name}")


def integrate_topic(topic: int, source_dir: Path) -> dict:
    assets = ROOT / f"assets/policia-nacional/tema-{topic:02d}"
    manifest_path = assets / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected = {Path(item["file"]).with_suffix(".png").name for item in manifest["resources"]}
    present = {path.name for path in source_dir.glob("*.png")}
    if expected != present:
        missing = sorted(expected - present)
        extra = sorted(present - expected)
        raise RuntimeError(f"Tema {topic}: PNG no coincidentes; faltan={missing}; sobran={extra}")

    sizes = []
    for resource in manifest["resources"]:
        png = source_dir / Path(resource["file"]).with_suffix(".png").name
        webp = assets / resource["file"]
        size, _, _ = save_webp(png, webp)
        if size > MAX_BYTES:
            raise RuntimeError(f"{webp.name} supera el límite")
        resource["status"] = "integrated_webp"
        sizes.append(size)

    total = len(manifest["resources"])
    manifest.update(
        {
            "visual_version": "1.0.0",
            "status": "integrated",
            "totals": {"resources": total, "integrated": total, "planned": 0},
            "integration_status": "complete",
            "integrated_at": INTEGRATED_AT,
        }
    )
    write_json(manifest_path, manifest)

    knowledge_path = ROOT / f"conocimiento/policia-nacional/tema-{topic:02d}/manifest.json"
    knowledge = json.loads(knowledge_path.read_text(encoding="utf-8"))
    knowledge["assets"].update({"total": total, "planned": 0})
    knowledge["visual_version"] = "1.0.0"
    write_json(knowledge_path, knowledge)

    project_path = ROOT / "temario.json"
    project = json.loads(project_path.read_text(encoding="utf-8"))
    project_topic = next(
        item
        for item in project["oppositions"]["policia-nacional"]["topics"]
        if int(item["number"]) == topic
    )
    project_topic.update(
        {"visual_version": "1.0.0", "visual_assets": total, "visual_planned": 0}
    )
    write_json(project_path, project)
    return {"topic": topic, "total": total, "bytes": sum(sizes), "max_bytes": max(sizes)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-12",
        type=Path,
        default=WORKSPACE / "tema-12-imagenes-png",
    )
    parser.add_argument(
        "--source-13",
        type=Path,
        default=WORKSPACE / "tema-13-imagenes-png",
    )
    args = parser.parse_args()
    for result in (
        integrate_topic(12, args.source_12.resolve()),
        integrate_topic(13, args.source_13.resolve()),
    ):
        print(
            f"Tema {result['topic']}: {result['total']} WEBP, "
            f"{result['bytes'] / 1_000_000:.2f} MB, "
            f"máximo {result['max_bytes'] / 1000:.0f} kB"
        )


if __name__ == "__main__":
    main()
