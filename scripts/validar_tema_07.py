#!/usr/bin/env python3
"""Validaciones editoriales y de sincronización para el Tema 7."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "conocimiento/policia-nacional/tema-07/manifest.json"
PARTE = ROOT / "temas/policia-nacional/parte/tema-07-ministerio-interior-secretaria-estado-seguridad.md"
ATESTADO = ROOT / "temas/policia-nacional/atestado/tema-07-ministerio-interior-secretaria-estado-seguridad.md"

REQUIRED_BOTH = [
    "Secretaría General de Protección Civil y Emergencias",
    "Dirección General de Ejecución Penal y Reinserción Social",
    "Dirección General de Relaciones Internacionales y Extranjería",
    "Dirección General de Coordinación y Estudios",
    "Unidad Nacional de Retirada de Contenidos Ilícitos en Internet",
    "informes **anuales**",
    "Subdirección General de Sistemas de Información y Comunicaciones para la Seguridad",
    "Oficina Nacional de Garantías de los Derechos Humanos",
    "27 de abril de 2026",
    "💡 **HABLEMOS CLARO**",
    "🚔 **EN LA CALLE**",
    "🎯 **LO QUE CAE**",
    "📅 Ha caído",
]

FORBIDDEN = [
    "EN CRISTIANO",
    "El temario que nunca descansa",
    "Dirección General de Protección Civil y Emergencias depende de la Subsecretaría",
    "informes semestrales sobre la situación",
    "Oficina Nacional de Garantía de los Derechos Humanos",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/compilar_tema_07.py")],
        cwd=ROOT,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    require(manifest["normative_cutoff"] == "2026-07-28", "Corte normativo incorrecto")
    require(manifest["number"] == 7, "Número de tema incorrecto")

    parte = PARTE.read_text(encoding="utf-8")
    atestado = ATESTADO.read_text(encoding="utf-8")
    for phrase in REQUIRED_BOTH:
        require(phrase in parte, f"Falta en El Parte: {phrase}")
        require(phrase in atestado, f"Falta en El Atestado: {phrase}")
    for phrase in FORBIDDEN:
        require(phrase not in parte, f"Contenido prohibido en El Parte: {phrase}")
        require(phrase not in atestado, f"Contenido prohibido en El Atestado: {phrase}")

    parte_words = len(parte.split())
    atestado_words = len(atestado.split())
    require(parte_words < atestado_words, "El Parte no es más breve que El Atestado")
    require(atestado_words / parte_words >= 1.30, "Diferencia insuficiente entre vistas")

    print(
        f"OK · Parte {parte_words} palabras · Atestado {atestado_words} palabras · "
        f"ratio {atestado_words / parte_words:.2f}"
    )


if __name__ == "__main__":
    main()
