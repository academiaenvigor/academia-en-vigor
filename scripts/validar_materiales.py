
#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_CATEGORIES = {'infografias', 'presentaciones', 'audios', 'videos'}
ALLOWED_STATUS = {'planned', 'in_production', 'pending_review', 'approved_internal', 'published', 'retired'}
ALLOWED_OWNERSHIP = {'own', 'licensed', 'authorized'}
LOCAL_ALLOWED = {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.md', '.json'}


def main() -> int:
    errors = []
    manifests = sorted((ROOT / 'materiales-didacticos').glob('*/tema-*/manifest.json'))
    for path in manifests:
        data = json.loads(path.read_text(encoding='utf-8'))
        resources = data.get('resources', [])
        for resource in resources:
            rid = resource.get('id', '<sin-id>')
            category = resource.get('category')
            if category not in ALLOWED_CATEGORIES:
                errors.append(f'{path.relative_to(ROOT)}: categoría inválida en {rid}')
            if resource.get('status') not in ALLOWED_STATUS:
                errors.append(f'{path.relative_to(ROOT)}: estado inválido en {rid}')
            if resource.get('ownership') not in ALLOWED_OWNERSHIP:
                errors.append(f'{path.relative_to(ROOT)}: autoría o permiso no acreditado en {rid}')
            if not resource.get('source_content_version'):
                errors.append(f'{path.relative_to(ROOT)}: falta versión fuente en {rid}')
            storage = resource.get('storage', {})
            storage_type = storage.get('type')
            if storage_type == 'external':
                if not storage.get('url'):
                    errors.append(f'{path.relative_to(ROOT)}: falta URL externa en {rid}')
            elif storage_type == 'local':
                relative = storage.get('path')
                if not relative:
                    errors.append(f'{path.relative_to(ROOT)}: falta ruta local en {rid}')
                    continue
                target = path.parent / relative
                if not target.exists():
                    errors.append(f'{path.relative_to(ROOT)}: no existe {relative} para {rid}')
                if target.suffix.lower() not in LOCAL_ALLOWED:
                    errors.append(f'{path.relative_to(ROOT)}: extensión local no permitida en {rid}')
                if category in {'audios', 'videos'}:
                    errors.append(f'{path.relative_to(ROOT)}: audio/vídeo debe almacenarse externamente ({rid})')
            else:
                errors.append(f'{path.relative_to(ROOT)}: almacenamiento inválido en {rid}')
        print(f'OK materiales: {path.relative_to(ROOT)}: {len(resources)} recursos')
    if errors:
        print('\n'.join(f'ERROR: {error}' for error in errors))
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
