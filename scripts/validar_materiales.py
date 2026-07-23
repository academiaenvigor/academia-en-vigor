
#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_CATEGORIES = {'infografias', 'presentaciones', 'audios', 'videos'}
ALLOWED_STATUS = {'planned', 'in_production', 'pending_review', 'approved_internal', 'published', 'retired'}
ALLOWED_OWNERSHIP = {'own', 'licensed', 'authorized'}
ALLOWED_SCOPE = {'tema', 'parte', 'bloque'}
ALLOWED_TIER = {'gratis', 'mensual', 'trimestral', 'completa'}
# Un recurso aún no producido no puede tener URL todavía
STATUS_SIN_URL = {'planned', 'in_production'}
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
            if resource.get('scope') not in ALLOWED_SCOPE:
                errors.append(f'{path.relative_to(ROOT)}: ámbito inválido en {rid}')
            access_tier = resource.get('access_tier')
            if access_tier is not None and access_tier not in ALLOWED_TIER:
                errors.append(f'{path.relative_to(ROOT)}: plan de acceso inválido en {rid}')
            if resource.get('scope') == 'parte' and not resource.get('part_number'):
                errors.append(f'{path.relative_to(ROOT)}: recurso de parte sin número de parte en {rid}')
            if resource.get('scope') == 'bloque' and not resource.get('blocks'):
                errors.append(f'{path.relative_to(ROOT)}: recurso de bloque sin bloque asignado en {rid}')
            storage = resource.get('storage', {})
            storage_type = storage.get('type')
            if storage_type == 'external':
                if not storage.get('asset_key'):
                    errors.append(f'{path.relative_to(ROOT)}: falta asset_key en {rid}')
                if not storage.get('url') and resource.get('status') not in STATUS_SIN_URL:
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
