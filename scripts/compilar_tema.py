
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


def manifest_path(opposition: str, topic: int) -> Path:
    return ROOT / f'conocimiento/{opposition}/tema-{topic:02d}/manifest.json'


def load(opposition: str, topic: int):
    path = manifest_path(opposition, topic)
    manifest = json.loads(path.read_text(encoding='utf-8'))
    text = (ROOT / manifest['source_file']).read_text(encoding='utf-8')
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


def render(kind: str, manifest: dict, blocks: list[dict], layers: dict) -> str:
    number = int(manifest.get('topic_number') or str(manifest['topic']).split('-')[-1])
    title = manifest['title']
    opposition_display = manifest.get('opposition_display_name', 'Policía Nacional')
    output = [
        f'# TEMA {number} · {title.upper()}\n\n'
        f'**{opposition_display} · Método VIGOR · {kind.upper()}**\n'
        f'**Versión de contenido:** {manifest["content_version"]}\n'
        f'**Estado editorial:** {manifest["editorial_status"]} · **Publicación:** {manifest["publication_status"]}\n'
    ]
    output.append(f'# {layers["MAPA"][0]}\n\n{layers["MAPA"][1]}\n')
    output.append('# Contenido\n')
    for block in blocks:
        output.append(
            f'## {block["number"]}. {block["title"]}\n\n{block[kind]}\n\n'
            f'*Referencia principal: `{block["source"]}`.*\n'
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
        expected = render(kind, manifest, blocks, layers)
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
