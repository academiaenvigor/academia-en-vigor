#!/usr/bin/env python3
"""Inserta una vez cada ancla FACT del Tema 8 en su bloque maestro."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "conocimiento/policia-nacional/tema-08/master.md"
COVERAGE = ROOT / "conocimiento/policia-nacional/tema-08/cobertura.json"


def main() -> None:
    coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
    by_block: dict[int, list[str]] = defaultdict(list)
    for fact in coverage["facts"]:
        by_block[int(fact["bloque"])].append(fact["id"])

    text = MASTER.read_text(encoding="utf-8")
    text = re.sub(r"^<!-- FACT:PN-T08-F\d{3} -->\n?", "", text, flags=re.MULTILINE)

    for block in range(1, 29):
        end = f"<!-- ATESTADO END -->\n<!-- BLOCK {block:02d} END -->"
        anchors = "\n".join(f"<!-- FACT:{fact_id} -->" for fact_id in by_block[block])
        replacement = f"{anchors}\n<!-- ATESTADO END -->\n<!-- BLOCK {block:02d} END -->"
        if text.count(end) != 1:
            raise SystemExit(f"Marcador de bloque ausente o duplicado: {end}")
        text = text.replace(end, replacement)

    MASTER.write_text(text, encoding="utf-8")
    print(f"OK: {sum(map(len, by_block.values()))} anclas FACT insertadas")


if __name__ == "__main__":
    main()
