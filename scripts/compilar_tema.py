
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOCK_RE = re.compile(
    r'<!-- BLOCK (\d{2}) START -->\n## \d+\. (.*?)\n\*\*Fuente principal:\*\* `([^`]+)`\n'
    r'<!-- PARTE START -->\n(.*?)\n<!-- PARTE END -->\n'
    r'<!-- ATESTADO START -->\n(.*?)\n<!-- ATESTADO END -->\n<!-- BLOCK \1 END -->',
    re.S,
)
LAYERS = ['MAPA', 'CONTENIDO', 'HABLEMOS_CLARO', 'EN_LA_CALLE', 'LO_QUE_CAE', 'HA_CAIDO']
VIGOR_BLOCKS = {
    'hablemos-claro', 'en-la-calle', 'lo-que-cae', 'perla-vigor',
    'trampa', 'ha-caido', 'visual',
}
FACT_PREFIX_RE = re.compile(
    r'<!-- FACT:(?P<fact_id>[A-Z0-9-]+) -->\s*'
    r'(?P<body>.*?)(?=\s*<!-- FACT:|\Z)',
    re.S,
)


def normalize_fact_markers(text: str) -> str:
    """Mueve cada ancla FACT al final del hecho para no romper Markdown."""
    paragraphs = re.split(r'(\n\s*\n)', text)
    for index in range(0, len(paragraphs), 2):
        paragraph = paragraphs[index]
        if '<!-- FACT:' not in paragraph:
            continue
        paragraphs[index] = FACT_PREFIX_RE.sub(
            lambda match: (
                f'{match.group("body").rstrip()} '
                f'<!-- FACT:{match.group("fact_id")} -->'
            ),
            paragraph,
        )
    return ''.join(paragraphs)


def validate_vigor_blocks(text: str, source_file: str) -> None:
    """Valida los contenedores :::tipo ... ::: sin interpretar su contenido."""
    opened: tuple[str, int] | None = None
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith(':::'):
            continue
        if line != line.lstrip():
            raise ValueError(f'{source_file}:{line_number}: la marca VIGOR debe empezar en la primera columna')
        if stripped == ':::':
            if opened is None:
                raise ValueError(f'{source_file}:{line_number}: cierre VIGOR sin apertura')
            opened = None
            continue
        kind = stripped[3:].strip()
        if kind not in VIGOR_BLOCKS:
            raise ValueError(f'{source_file}:{line_number}: bloque VIGOR desconocido: {kind}')
        if opened is not None:
            previous_kind, previous_line = opened
            raise ValueError(
                f'{source_file}:{line_number}: no se permiten bloques VIGOR anidados; '
                f'{previous_kind} comenzó en la línea {previous_line}'
            )
        opened = (kind, line_number)
    if opened is not None:
        kind, line_number = opened
        raise ValueError(f'{source_file}:{line_number}: bloque VIGOR {kind} sin cierre')


def manifest_path(opposition: str, topic: int) -> Path:
    return ROOT / f'conocimiento/{opposition}/tema-{topic:02d}/manifest.json'


def load(opposition: str, topic: int):
    path = manifest_path(opposition, topic)
    manifest = json.loads(path.read_text(encoding='utf-8'))
    text = (ROOT / manifest['source_file']).read_text(encoding='utf-8')
    validate_vigor_blocks(text, manifest['source_file'])
    blocks = [
        {'number': n, 'title': t, 'source': s, 'parte': p.strip(), 'atestado': a.strip()}
        for n, t, s, p, a in BLOCK_RE.findall(text)
    ]
    layers = {}
    for key in LAYERS:
        match = re.search(rf'<!-- LAYER:{key} -->\n# ([^\n]+)\n(.*?)(?=\n<!-- LAYER:|\Z)', text, re.S)
        if not match:
            raise ValueError(f'Falta capa {key} en {manifest["source_file"]}')
        layers[key] = (match.group(1), match.group(2).strip())
    return manifest, blocks, layers




def alt_desde_nombre(archivo: str) -> str:
    """Genera un texto alternativo legible a partir del nombre del archivo."""
    base = archivo.rsplit('.', 1)[0]
    partes = [p for p in base.split('-') if not re.fullmatch(r't\d+|il|ilu|\d+', p)]
    return ' '.join(partes).replace('_', ' ').capitalize() or 'Esquema del tema'


VISUAL_BLOCK_RE = re.compile(r':::visual\n(.*?)\n:::', re.S)
VISUAL_REF_RE = re.compile(
    r'\*\*(?P<tipo>Referencia visual prevista|Ilustración simple|Mapa general previsto):\*\*\s*'
    r'`(?P<archivo>[\w\-]+\.(?:webp|png|svg|jpe?g))`(?P<resto>[^\n]*)',
    re.I,
)


def render_visuals(text: str, opposition: str, topic: int) -> str:
    """Convierte los bloques :::visual en imágenes reales si el archivo existe.

    Si el archivo aún no se ha generado, deja un comentario invisible en lugar
    de un aviso editorial: el alumno nunca ve marcadores de producción.
    """
    assets_dir = ROOT / 'assets' / opposition / f'tema-{topic:02d}'
    rel_base = f'../../../assets/{opposition}/tema-{topic:02d}'

    def render_block(match: re.Match) -> str:
        piezas = []
        for ref in VISUAL_REF_RE.finditer(match.group(1)):
            archivo = ref.group('archivo')
            tipo = ref.group('tipo')
            pie = ref.group('resto').strip(' .·')
            if not (assets_dir / archivo).exists():
                piezas.append(f'<!-- VISUAL PENDIENTE: {archivo} -->')
                continue
            ancho = 600 if tipo == 'Ilustración simple' else 820
            alt = pie or alt_desde_nombre(archivo)
            bloque = (
                f'<!-- VISUAL:{archivo} -->\n'
                f'<p align="center">\n'
                f'  <img src="{rel_base}/{archivo}" alt="{alt}" width="{ancho}">\n'
                f'</p>'
            )
            if pie:
                etiqueta = 'Ilustración' if tipo == 'Ilustración simple' else 'Infografía'
                bloque += f'\n<p align="center"><em>{etiqueta}: {pie}.</em></p>'
            piezas.append(bloque)
        return '\n\n'.join(piezas)

    return VISUAL_BLOCK_RE.sub(render_block, text)



ICONOS_MATERIAL = {
    'audios': '🎧', 'videos': '🎬', 'presentaciones': '📊', 'infografias': '🖼',
}
ETIQUETAS_MATERIAL = {
    'audios': 'Audio', 'videos': 'Vídeo',
    'presentaciones': 'Presentación', 'infografias': 'Infografía',
}
MATERIAL_DISPONIBLE = {'approved_internal', 'published'}


def cargar_materiales(opposition: str, topic: int) -> dict:
    """Lee el manifest de materiales y lo indexa por bloque y por tema."""
    ruta = ROOT / 'materiales-didacticos' / opposition / f'tema-{topic:02d}' / 'manifest.json'
    if not ruta.exists():
        return {'por_bloque': {}, 'general': [], 'mostrar_planificados': False}
    data = json.loads(ruta.read_text(encoding='utf-8'))
    mostrar = bool(data.get('display_policy', {}).get('show_planned_in_temas'))
    por_bloque, general = {}, []
    for recurso in data.get('resources', []):
        if recurso.get('scope') == 'tema':
            general.append(recurso)
        for bloque in recurso.get('blocks', []):
            por_bloque.setdefault(str(bloque), []).append(recurso)
    return {'por_bloque': por_bloque, 'general': general, 'mostrar_planificados': mostrar}


def tira_materiales(recursos: list, mostrar_planificados: bool, titulo: str) -> str:
    """Genera la tira de accesos al material didáctico de un punto o del tema.

    La infografía no se incluye: ya se muestra incrustada en el propio texto.
    """
    piezas = []
    for recurso in recursos:
        categoria = recurso.get('category')
        if categoria == 'infografias':
            continue
        icono = ICONOS_MATERIAL.get(categoria, '📎')
        etiqueta = ETIQUETAS_MATERIAL.get(categoria, 'Material')
        segundos = recurso.get('duration_seconds')
        duracion = f' · {round(segundos / 60)} min' if segundos else ''
        url = (recurso.get('storage') or {}).get('url') or ''
        disponible = recurso.get('status') in MATERIAL_DISPONIBLE and url
        if disponible:
            piezas.append(f'[{icono} {etiqueta}{duracion}]({url})')
        elif mostrar_planificados:
            piezas.append(f'{icono} {etiqueta} *(en producción)*')
        else:
            piezas.append(f'<!-- MATERIAL PENDIENTE: {recurso.get("id")} -->')
    visibles = [x for x in piezas if not x.startswith('<!--')]
    if not visibles:
        return '\n'.join(piezas)
    return f'> **{titulo}:** ' + ' · '.join(visibles)


def render(kind: str, manifest: dict, blocks: list[dict], layers: dict,
           opposition: str = 'policia-nacional', topic: int | None = None) -> str:
    number = int(manifest.get('topic_number') or str(manifest['topic']).split('-')[-1])
    title = manifest['title']
    opposition_display = manifest.get('opposition_display_name', 'Policía Nacional')
    output = [
        f'# TEMA {number} · {title.upper()}\n\n'
        f'**{opposition_display} · Método VIGOR · {kind.upper()}**\n'
        f'**Versión de contenido:** {manifest["content_version"]}\n'
        f'**Estado editorial:** {manifest["editorial_status"]} · **Publicación:** {manifest["publication_status"]}\n'
    ]
    materiales_mapa = cargar_materiales(opposition, topic or number)
    tira_general = tira_materiales(materiales_mapa['general'],
                                   materiales_mapa['mostrar_planificados'],
                                   'Material completo del tema')
    output.append(f'# {layers["MAPA"][0]}\n\n'
                  f'{render_visuals(layers["MAPA"][1], opposition, topic or number)}\n'
                  + (f'\n{tira_general}\n' if tira_general else ''))
    output.append('# Contenido\n')
    materiales = cargar_materiales(opposition, topic or number)
    for block in blocks:
        body = normalize_fact_markers(block[kind])
        body = render_visuals(body, opposition, topic or number)
        output.append(
            f'## {block["number"]}. {block["title"]}\n\n{body}\n\n'
            + (tira + '\n\n' if (tira := tira_materiales(
                materiales['por_bloque'].get(str(block['number']), []),
                materiales['mostrar_planificados'], 'Material de este punto')) else '')
            + f'<!-- FUENTE: {block["source"]} -->\n'
        )
    for key in LAYERS[2:]:
        layer_title, body = layers[key]
        output.append(f'# {layer_title}\n\n{body}\n')
    output.append(
        f'---\n\n*Academia En Vigor · El temario que nunca duerme · Tema {number} · '
        f'v{manifest["content_version"]} · Documento interno no publicado.*\n'
    )
    return '\n'.join(output)


def topics_from_index() -> list[tuple[str, int]]:
    data = json.loads((ROOT / 'temario.json').read_text(encoding='utf-8'))
    items = []
    for opposition, info in data.get('oppositions', {}).items():
        for topic in info.get('topics', []):
            items.append((opposition, int(topic['number'])))
    return items


def process(opposition: str, topic: int, write: bool, check: bool) -> list[str]:
    manifest, blocks, layers = load(opposition, topic)
    expected_blocks = manifest.get('semantic_blocks')
    if expected_blocks is not None and len(blocks) != expected_blocks:
        raise ValueError(f'{opposition}/tema-{topic:02d}: {len(blocks)} bloques; se esperaban {expected_blocks}')
    outdated = []
    for kind, relative in manifest['outputs'].items():
        target = ROOT / relative
        expected = render(kind, manifest, blocks, layers, opposition, topic)
        if write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(expected, encoding='utf-8')
        if check and (not target.exists() or target.read_text(encoding='utf-8') != expected):
            outdated.append(relative)
    print(f'OK: {opposition}/tema-{topic:02d}: {len(blocks)} bloques')
    return outdated


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--oposicion', default='policia-nacional')
    parser.add_argument('--tema', type=int, default=3)
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()

    selected = topics_from_index() if args.all else [(args.oposicion, args.tema)]
    outdated = []
    for opposition, topic in selected:
        outdated.extend(process(opposition, topic, args.write, args.check))
    if outdated:
        print('Derivados desactualizados:', *outdated, sep='\n- ')
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
