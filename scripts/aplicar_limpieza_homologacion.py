#!/usr/bin/env python3
"""Elimina únicamente los assets obsoletos declarados por la homologación."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "ELIMINAR_ARCHIVOS_OBSOLETOS.txt"


def main() -> int:
    removed = 0
    for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
        relative = raw.strip()
        if not relative.startswith("assets/") or not relative.endswith(".webp"):
            continue
        target = (ROOT / relative).resolve()
        if ROOT not in target.parents:
            raise SystemExit(f"Ruta rechazada: {relative}")
        if target.exists():
            target.unlink()
            removed += 1
    print(f"Assets obsoletos eliminados: {removed}")
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts/validar_proyecto.py")],
        cwd=ROOT,
    ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
