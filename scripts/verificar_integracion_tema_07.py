#!/usr/bin/env python3
"""Comprueba que el Tema 7 esté correctamente registrado para explorador.html."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMARIO = ROOT / "temario.json"


def cargar_json(ruta: Path):
    with ruta.open(encoding="utf-8") as archivo:
        return json.load(archivo)


def main() -> None:
    temario = cargar_json(TEMARIO)
    topics = temario["oppositions"]["policia-nacional"]["topics"]
    coincidencias = [topic for topic in topics if topic["number"] == 7]
    if len(coincidencias) != 1:
        raise SystemExit("ERROR: temario.json debe contener exactamente un Tema 7.")

    topic = coincidencias[0]
    stem = f"tema-07-{topic['slug']}.md"
    esperadas = {
        "parte": f"temas/policia-nacional/parte/{stem}",
        "atestado": f"temas/policia-nacional/atestado/{stem}",
    }
    for clave, ruta_esperada in esperadas.items():
        if topic[clave] != ruta_esperada:
            raise SystemExit(
                f"ERROR: la ruta {clave!r} no coincide con el slug: {topic[clave]}"
            )

    claves_de_ruta = (
        "manifest",
        "parte",
        "atestado",
        "question_bank",
        "evaluation_plan",
        "assets",
        "teaching_materials",
        "official_exam_index",
    )
    for clave in claves_de_ruta:
        ruta = ROOT / topic[clave]
        if not ruta.is_file():
            raise SystemExit(f"ERROR: falta {topic[clave]}")
        if ruta.suffix == ".json":
            cargar_json(ruta)

    print("OK: Tema 7 registrado y todas las rutas del explorador son válidas.")


if __name__ == "__main__":
    main()
