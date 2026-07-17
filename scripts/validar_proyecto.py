#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    "README.md",
    "temario.json",
    "editorial/00-codigo-vigor.md",
    "editorial/01-manual-editorial.md",
    "editorial/02-estandar-tecnico.md",
    "fuentes/catalogo.json",
    "conocimiento/policia-nacional/tema-03/master.md",
    "conocimiento/policia-nacional/tema-03/manifest.json",
    "conocimiento/policia-nacional/tema-03/cobertura.json",
    "temas/policia-nacional/parte/tema-03-constitucion-espanola-ii.md",
    "temas/policia-nacional/atestado/tema-03-constitucion-espanola-ii.md",
    "banco-preguntas/policia-nacional/tema-03/preguntas.jsonl",
    "evaluaciones/policia-nacional/tema-03/plan.json",
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"Falta {rel}")

for rel in ["temario.json", "fuentes/catalogo.json", "conocimiento/policia-nacional/tema-03/manifest.json", "conocimiento/policia-nacional/tema-03/cobertura.json", "banco-preguntas/policia-nacional/tema-03/manifest.json", "evaluaciones/policia-nacional/tema-03/plan.json"]:
    try:
        json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"JSON inválido {rel}: {exc}")


if errors:
    print("\n".join(errors))
    raise SystemExit(1)
print("OK: estructura, JSON y archivos canónicos validados")
