#!/usr/bin/env python3
"""Compila las vistas Parte y Atestado desde el master canónico del Tema 7."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "conocimiento/policia-nacional/tema-07/manifest.json"
MASTER_PATH = ROOT / "conocimiento/policia-nacional/tema-07/master.md"

OPEN_RE = re.compile(r"^<!-- vigor:block (?P<meta>\{.*\}) -->$")
CLOSE = "<!-- vigor:end -->"

BLOCK_ORDER = [
    "pn-t07-meta-parte",
    "pn-t07-meta-atestado",
    "pn-t07-mapa-comun",
    "pn-t07-mapa-ampliacion",
    "pn-t07-parte1-titulo",
    "pn-t07-competencias",
    "pn-t07-competencias-hc",
    "pn-t07-ministro",
    "pn-t07-mando-tres-niveles",
    "pn-t07-mando-caso",
    "pn-t07-organigrama-2026",
    "pn-t07-organigrama-explicacion",
    "pn-t07-reforma-2026",
    "pn-t07-parte1-recuperacion",
    "pn-t07-parte2-titulo",
    "pn-t07-ses-posicion",
    "pn-t07-ses-funciones",
    "pn-t07-ses-funciones-explicacion",
    "pn-t07-ses-funciones-trampas",
    "pn-t07-ses-caso",
    "pn-t07-parte3-titulo",
    "pn-t07-estructura-ses-resumen",
    "pn-t07-gabinete-ses",
    "pn-t07-citco-nucleo",
    "pn-t07-citco-ampliacion",
    "pn-t07-citco-trampas",
    "pn-t07-comite",
    "pn-t07-subdirecciones-ses",
    "pn-t07-subdirecciones-ses-parte",
    "pn-t07-subdirecciones-expansion",
    "pn-t07-gerencia",
    "pn-t07-parte3-recuperacion",
    "pn-t07-parte4-titulo",
    "pn-t07-cuatro-dg-resumen",
    "pn-t07-dgp-dggc-ampliacion",
    "pn-t07-dgrie",
    "pn-t07-dgrie-parte",
    "pn-t07-dgrie-trampas",
    "pn-t07-dgce-nucleo",
    "pn-t07-dgce-parte",
    "pn-t07-dgce-ampliacion",
    "pn-t07-dgce-trampas",
    "pn-t07-dgce-caso",
    "pn-t07-parte4-recuperacion",
    "pn-t07-parte5-titulo",
    "pn-t07-disposiciones-esenciales",
    "pn-t07-disposiciones-ampliacion",
    "pn-t07-cierre-titulo",
    "pn-t07-ultima-vuelta",
    "pn-t07-trampas-finales",
    "pn-t07-ha-caido",
    "pn-t07-mini-test-parte",
    "pn-t07-recuperacion-atestado",
    "pn-t07-recursos",
]


def parse_blocks(text: str) -> list[tuple[dict, str]]:
    blocks: list[tuple[dict, str]] = []
    current_meta: dict | None = None
    current_lines: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        match = OPEN_RE.match(line)
        if match:
            if current_meta is not None:
                raise ValueError(f"Bloque anidado en línea {line_number}")
            current_meta = json.loads(match.group("meta"))
            current_lines = []
            continue
        if line == CLOSE:
            if current_meta is None:
                raise ValueError(f"Cierre sin apertura en línea {line_number}")
            blocks.append((current_meta, "\n".join(current_lines).rstrip() + "\n"))
            current_meta = None
            current_lines = []
            continue
        if current_meta is not None:
            current_lines.append(line)
        elif line.strip():
            raise ValueError(
                f"Contenido fuera de bloque en línea {line_number}: {line[:80]}"
            )
    if current_meta is not None:
        raise ValueError("Bloque sin cerrar al final del archivo")
    return blocks


def sort_blocks(blocks: list[tuple[dict, str]]) -> list[tuple[dict, str]]:
    declared = {meta["id"] for meta, _ in blocks}
    expected = set(BLOCK_ORDER)
    if declared != expected:
        missing = sorted(expected - declared)
        extra = sorted(declared - expected)
        raise ValueError(f"Mapa de orden incoherente. Faltan={missing}; sobran={extra}")
    order = {block_id: index for index, block_id in enumerate(BLOCK_ORDER)}
    return sorted(blocks, key=lambda block: order[block[0]["id"]])


def canonical_master(blocks: list[tuple[dict, str]]) -> str:
    """Normaliza también el orden físico del maestro para facilitar su revisión."""
    serialized: list[str] = []
    for meta, content in blocks:
        marker = json.dumps(meta, ensure_ascii=False, separators=(",", ":"))
        serialized.extend(
            [
                f"<!-- vigor:block {marker} -->",
                content.rstrip(),
                CLOSE,
                "",
            ]
        )
    return "\n".join(serialized).rstrip() + "\n"


def compile_view(blocks: list[tuple[dict, str]], view: str, header: str) -> str:
    selected: list[str] = [header.rstrip(), ""]
    seen_ids: set[str] = set()
    for meta, content in blocks:
        block_id = meta["id"]
        if block_id in seen_ids:
            raise ValueError(f"Identificador de bloque duplicado: {block_id}")
        seen_ids.add(block_id)
        if view in meta["views"]:
            selected.append(content.rstrip())
            selected.append("")
    return "\n".join(selected).rstrip() + "\n"


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    blocks = sort_blocks(parse_blocks(MASTER_PATH.read_text(encoding="utf-8")))
    MASTER_PATH.write_text(canonical_master(blocks), encoding="utf-8")
    base_header = (
        "<!-- Archivo generado. No editar cambios sustantivos aquí. -->\n"
        "<!-- Fuente: conocimiento/policia-nacional/tema-07/ -->\n"
        f"<!-- Tema: {manifest['id']} · Contenido: {manifest['content_version']} "
        f"· Corte normativo: {manifest['normative_cutoff']} -->"
    )
    for view in ("parte", "atestado"):
        output_path = ROOT / manifest["outputs"][view]
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            compile_view(blocks, view, base_header), encoding="utf-8"
        )
        print(output_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
