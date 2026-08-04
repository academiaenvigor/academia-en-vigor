#!/usr/bin/env python3
"""Integra en el manifest de assets las visuales ya subidas a disco.

Sustituye a los antiguos integrar_visuales_tema_08.py e
integrar_visuales_temas_12_13.py, que eran de un solo uso.

Marca como `integrated_webp` todo recurso cuyo .webp exista ya en la carpeta
del tema, recalcula los totales y deja el manifest listo para que
compilar_tema.py inserte las imágenes en parte y atestado.

Uso:
    python scripts/integrar_visuales.py --tema 23
    python scripts/integrar_visuales.py --oposicion guardia-civil --tema 4
    python scripts/integrar_visuales.py --all          # todas las oposiciones
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def integrar(opposition: str, topic: int, fecha: str) -> tuple[int, int, int] | None:
    code = f'tema-{topic:02d}'
    manifest_path = ROOT / 'assets' / opposition / code / 'manifest.json'
    if not manifest_path.exists():
        return None

    data = json.loads(manifest_path.read_text(encoding='utf-8'))
    base = manifest_path.parent
    integrados = 0
    nuevos: list[str] = []

    # Estados que ya cuentan como visual viva: no se tocan, porque los temas
    # cerrados usan convenios propios (p. ej. recursos solo en atestado).
    ya_integrados = {'approved_internal', 'integrated_webp', 'published'}

    for resource in data.get('resources', []):
        if not (base / resource['file']).exists():
            continue
        integrados += 1
        if resource.get('status') in ya_integrados:
            continue
        resource['status'] = 'integrated_webp'
        resource['documents'] = ['parte', 'atestado']
        resource['required_format'] = 'webp'
        resource['description'] = resource.get('description', '').replace(
            'Referencia visual pendiente: ', ''
        )
        nuevos.append(resource['file'])

    total = len(data.get('resources', []))
    pendientes = total - integrados
    data['totals'] = {
        'resources': total,
        'integrated': integrados,
        'planned': pendientes,
    }
    completo = pendientes == 0 and total > 0
    data['status'] = 'integrated' if completo else ('partial' if integrados else 'planned')
    data['integration_status'] = 'complete' if completo else ('partial' if integrados else 'planned')
    if nuevos:
        data['integrated_at'] = fecha
        data['visual_version'] = data.get('visual_version', '1.0.0')
    if completo:
        data['planned_resources'] = []

    manifest_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )
    return integrados, total, len(nuevos)


def temas_del_indice() -> list[tuple[str, int]]:
    index = json.loads((ROOT / 'temario.json').read_text(encoding='utf-8'))
    return [
        (opposition, int(topic['number']))
        for opposition, info in index.get('oppositions', {}).items()
        for topic in info.get('topics', [])
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--oposicion', default='policia-nacional')
    parser.add_argument('--tema', type=int)
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--fecha', default=dt.date.today().isoformat())
    args = parser.parse_args()

    if not args.all and args.tema is None:
        parser.error('indica --tema N o usa --all')

    seleccion = temas_del_indice() if args.all else [(args.oposicion, args.tema)]
    cambiados = 0
    for opposition, topic in seleccion:
        resultado = integrar(opposition, topic, args.fecha)
        if resultado is None:
            print(f'AVISO: {opposition}/tema-{topic:02d}: sin manifest de assets')
            continue
        integrados, total, nuevos = resultado
        if nuevos:
            cambiados += 1
            estado = 'completo' if integrados == total else 'parcial'
            print(f'{opposition}/tema-{topic:02d}: {nuevos} nuevas · {integrados}/{total} integradas ({estado})')

    print(f'\n{cambiados} tema(s) con visuales integradas.')
    print('Siguiente paso:')
    print('  python scripts/sincronizar_temario.py --write')
    print('  python scripts/compilar_tema.py --all --write')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
