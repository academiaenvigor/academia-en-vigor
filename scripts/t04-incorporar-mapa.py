#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "master": ROOT / "conocimiento/policia-nacional/tema-04/master.md",
    "atestado": ROOT / "temas/policia-nacional/atestado/tema-04-union-europea.md",
    "parte": ROOT / "temas/policia-nacional/parte/tema-04-union-europea.md",
}

BLOCK = """<!-- VISUAL:t04-00-mapa-general.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-04/t04-00-mapa-general.webp" alt="Mapa general del Tema 4 · La Unión Europea" width="820">
</p>
"""

def insert_before_content(text: str) -> str:
    if "t04-00-mapa-general.webp" in text:
        return text
    marker = "\n# Contenido\n"
    if marker not in text:
        raise RuntimeError("No se encontró '# Contenido' en el archivo.")
    return text.replace(marker, "\n" + BLOCK.rstrip() + "\n\n# Contenido\n", 1)

def patch_master(text: str) -> str:
    if "t04-00-mapa-general.webp" in text:
        return text

    notice = "> Estas cifras caducan. Comprobarlas antes de cada convocatoria."
    if notice in text:
        return text.replace(notice, notice + "\n\n" + BLOCK.rstrip(), 1)

    marker = "\n---\n"
    if marker in text:
        return text.replace(marker, "\n\n" + BLOCK.rstrip() + "\n\n---\n", 1)

    raise RuntimeError("No se encontró un punto seguro para insertar el mapa en master.md.")

for key, path in FILES.items():
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo esperado: {path.relative_to(ROOT)}")

    original = path.read_text(encoding="utf-8")
    updated = patch_master(original) if key == "master" else insert_before_content(original)

    if updated != original:
        path.write_text(updated, encoding="utf-8")
        print(f"Actualizado: {path.relative_to(ROOT)}")
    else:
        print(f"Ya estaba correcto: {path.relative_to(ROOT)}")
