#!/usr/bin/env python3
"""Migra los callouts en formato antiguo (blockquote) a la sintaxis `:::`.

Antes del contrato 2.0.0 los avisos pedagógicos se escribían como citas:

    > **Hablemos claro:** texto
    > 🎯 **LO QUE CAE**
    > texto

`explorador.html` compensa parte de eso en tiempo de ejecución con
`normalizarBloquesAntiguos()`, pero solo reconoce las etiquetas en minúscula y
terminadas en dos puntos. Todo lo demás se renderiza como cita plana, queda
fuera de los filtros del explorador y no cuenta como capa del tema.

La conversión es puramente sintáctica: no altera el texto del cuerpo.

    python scripts/migrar_callouts.py --check
    python scripts/migrar_callouts.py --write
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Etiqueta antigua -> tipo VIGOR del contrato.
ETIQUETAS = {
    "hablemos claro": "hablemos-claro",
    "en la calle": "en-la-calle",
    "lo que cae": "lo-que-cae",
    "perla vigor": "perla-vigor",
    "trampa": "trampa",
    "no confundas": "trampa",
    "alerta del vigía": "trampa",
    "ha caído": "ha-caido",
    # Tema 3. "Ejemplo mental" plantea un supuesto para aplicar la regla
    # recién explicada, que es la función de «En la calle» en el contrato.
    "ejemplo mental": "en-la-calle",
}

# > [emoji] **ETIQUETA** o **ETIQUETA:** — con o sin texto en la misma línea.
CABECERA = re.compile(
    r"^>\s*(?:[^\w\s>]{1,3}\s*)?\*\*\s*(?P<etiqueta>[^*:]{2,45}?)\s*:?\s*\*\*\s*:?\s*(?P<inline>.*)$"
)
CONTINUACION = re.compile(r"^>\s?(?P<texto>.*)$")


def convertir(texto: str) -> tuple[str, int]:
    """Devuelve el texto migrado y cuántos callouts se han convertido."""
    lineas = texto.split("\n")
    salida: list[str] = []
    convertidos = 0
    i = 0

    while i < len(lineas):
        match = CABECERA.match(lineas[i])
        tipo = ETIQUETAS.get(match.group("etiqueta").strip().lower()) if match else None

        if tipo is None:
            salida.append(lineas[i])
            i += 1
            continue

        cuerpo: list[str] = []
        if match.group("inline").strip():
            cuerpo.append(match.group("inline").strip())

        i += 1
        while i < len(lineas):
            siguiente = CONTINUACION.match(lineas[i])
            # Una nueva cabecera cierra el callout anterior.
            if siguiente is None or CABECERA.match(lineas[i]):
                break
            if siguiente.group("texto").strip():
                cuerpo.append(siguiente.group("texto").rstrip())
            i += 1

        salida.extend([f":::{tipo}", *cuerpo, ":::"])
        convertidos += 1

    return "\n".join(salida), convertidos


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    parser.add_argument("--oposicion", default="policia-nacional")
    args = parser.parse_args()

    total = 0
    for master in sorted((ROOT / "conocimiento" / args.oposicion).glob("tema-*/master.md")):
        original = master.read_text(encoding="utf-8")
        migrado, convertidos = convertir(original)
        if not convertidos:
            continue
        total += convertidos
        print(f"{master.relative_to(ROOT)}: {convertidos} callouts antiguos")
        if args.write:
            master.write_text(migrado, encoding="utf-8")

    if not total:
        print("No quedan callouts en formato antiguo")
        return 0
    if args.write:
        print(f"\n{total} callouts migrados. Recompila: python scripts/compilar_tema.py --all --write")
        return 0
    print(f"\n{total} callouts pendientes de migrar")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
