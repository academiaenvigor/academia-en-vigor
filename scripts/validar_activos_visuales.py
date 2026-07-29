#!/usr/bin/env python3
"""Valida que manifiestos y documentos publicados usen los mismos visuales."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISUAL_RE = re.compile(r'<!-- VISUAL:(?P<file>[^ ]+) -->')
VALID_TYPES = {'infografia', 'ilustracion_simple'}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    project = json.loads((root / 'temario.json').read_text(encoding='utf-8'))

    for opposition, info in project.get('oppositions', {}).items():
        for topic in info.get('topics', []):
            number = int(topic['number'])
            asset_manifest_path = root / topic['assets']
            asset_manifest = json.loads(asset_manifest_path.read_text(encoding='utf-8'))
            resources = asset_manifest.get('resources', [])
            filenames = [resource.get('file') for resource in resources]

            duplicates = [
                filename for filename, count in Counter(filenames).items()
                if filename and count > 1
            ]
            for filename in duplicates:
                errors.append(
                    f'{opposition}/tema-{number:02d}: asset duplicado en manifest: {filename}'
                )

            for resource in resources:
                filename = resource.get('file', '')
                if resource.get('type') not in VALID_TYPES:
                    errors.append(
                        f'{opposition}/tema-{number:02d}: tipo visual no canónico '
                        f'en {filename}: {resource.get("type")}'
                    )
                if not resource.get('documents'):
                    errors.append(
                        f'{opposition}/tema-{number:02d}: {filename} sin documents'
                    )

            for document in ('parte', 'atestado'):
                output_path = root / topic[document]
                refs = VISUAL_RE.findall(output_path.read_text(encoding='utf-8'))
                repeated = [
                    filename for filename, count in Counter(refs).items() if count > 1
                ]
                for filename in repeated:
                    errors.append(
                        f'{opposition}/tema-{number:02d}/{document}: '
                        f'referencia visual repetida: {filename}'
                    )

                expected = {
                    resource['file']
                    for resource in resources
                    if document in resource.get('documents', [])
                }
                actual = set(refs)
                for filename in sorted(expected - actual):
                    errors.append(
                        f'{opposition}/tema-{number:02d}/{document}: '
                        f'falta recurso declarado: {filename}'
                    )
                for filename in sorted(actual - expected):
                    errors.append(
                        f'{opposition}/tema-{number:02d}/{document}: '
                        f'recurso no declarado para el documento: {filename}'
                    )

    return errors


if __name__ == '__main__':
    failures = validate()
    if failures:
        print('\n'.join(f'ERROR: {failure}' for failure in failures))
        raise SystemExit(1)
    print('OK: activos visuales sin repeticiones y sincronizados con sus manifiestos')
