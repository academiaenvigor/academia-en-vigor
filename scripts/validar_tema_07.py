#!/usr/bin/env python3
"""Validaciones editoriales y de sincronización para el Tema 7."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "conocimiento/policia-nacional/tema-07/manifest.json"
ASSET_MANIFEST = ROOT / "assets/policia-nacional/tema-07/manifest.json"
ASSET_DIR = ASSET_MANIFEST.parent
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

    asset_manifest = json.loads(ASSET_MANIFEST.read_text(encoding="utf-8"))
    resources = asset_manifest["resources"]
    filenames = [resource["file"] for resource in resources]
    require(asset_manifest["visual_version"] == "1.0.0", "Versión visual incorrecta")
    require(asset_manifest["status"] == "integrated", "Serie visual no integrada")
    require(asset_manifest["totals"]["resources"] == 13, "Total visual incorrecto")
    require(asset_manifest["totals"]["infographics"] == 7, "Total de infografías incorrecto")
    require(asset_manifest["totals"]["illustrations"] == 6, "Total de ilustraciones incorrecto")
    require(asset_manifest["totals"]["planned"] == 0, "Quedan recursos visuales pendientes")
    require(len(resources) == 13, "El manifiesto no contiene 13 recursos")
    require(len(set(filenames)) == 13, "Hay nombres visuales duplicados")

    for resource in resources:
        path = ASSET_DIR / resource["file"]
        require(path.is_file(), f"Falta el recurso visual: {resource['file']}")
        require(resource["status"] == "integrated_webp", f"Recurso no integrado: {resource['file']}")
        require(path.stat().st_size <= resource["max_bytes"], f"Recurso demasiado pesado: {resource['file']}")
        require(resource["file"] in parte, f"Falta la referencia en El Parte: {resource['file']}")
        require(resource["file"] in atestado, f"Falta la referencia en El Atestado: {resource['file']}")
        header = path.read_bytes()[:12]
        require(
            header[:4] == b"RIFF" and header[8:12] == b"WEBP",
            f"Formato incorrecto: {resource['file']}",
        )

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
