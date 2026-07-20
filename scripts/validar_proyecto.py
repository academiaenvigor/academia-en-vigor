
#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

required_root = [
    'README.md', 'COPYRIGHT.md', 'SECURITY.md', 'temario.json',
    'editorial/00-codigo-vigor.md', 'editorial/01-manual-editorial.md', 'editorial/02-estandar-tecnico.md',
    'fuentes/catalogo.json', 'scripts/compilar_tema.py', 'scripts/validar_bancos.py',
    'scripts/validar_examenes_oficiales.py', 'scripts/validar_materiales.py', 'scripts/validar_derechos.py',
    'banco-preguntas/policia-nacional/oficiales/manifest.json',
]
for relative in required_root:
    if not (ROOT / relative).exists():
        errors.append(f'Falta {relative}')

try:
    project = json.loads((ROOT / 'temario.json').read_text(encoding='utf-8'))
except Exception as exc:
    errors.append(f'temario.json inválido: {exc}')
    project = {}

for opposition, info in project.get('oppositions', {}).items():
    for topic in info.get('topics', []):
        paths = [
            topic.get('manifest'), topic.get('parte'), topic.get('atestado'), topic.get('question_bank'),
            topic.get('evaluation_plan'), topic.get('assets'), topic.get('teaching_materials'), topic.get('official_exam_index'),
        ]
        for relative in paths:
            if not relative or not (ROOT / relative).exists():
                errors.append(f'{opposition}/tema-{int(topic["number"]):02d}: falta {relative}')
        for relative in paths:
            if relative and relative.endswith('.json') and (ROOT / relative).exists():
                try:
                    json.loads((ROOT / relative).read_text(encoding='utf-8'))
                except Exception as exc:
                    errors.append(f'JSON inválido {relative}: {exc}')

assets_root = ROOT / 'assets'
for manifest_path in assets_root.glob('*/tema-*/manifest.json'):
    data = json.loads(manifest_path.read_text(encoding='utf-8'))
    topic_root = manifest_path.parent
    for resource in data.get('resources', []):
        target = topic_root / resource['file']
        if not target.exists():
            errors.append(f'Falta asset {target.relative_to(ROOT)}')

if errors:
    print('\n'.join(f'ERROR: {error}' for error in errors))
    raise SystemExit(1)

for script in ('validar_derechos.py', 'validar_examenes_oficiales.py', 'validar_materiales.py'):
    result = subprocess.run([sys.executable, str(ROOT / 'scripts' / script), str(ROOT)] if script == 'validar_examenes_oficiales.py' else [sys.executable, str(ROOT / 'scripts' / script)], cwd=ROOT)
    if result.returncode:
        raise SystemExit(result.returncode)

result = subprocess.run([sys.executable, str(ROOT / 'scripts/validar_bancos.py'), '--all'], cwd=ROOT)
if result.returncode:
    raise SystemExit(result.returncode)

print('OK: estructura VIGOR, bancos, materiales, derechos y exámenes oficiales validados')
