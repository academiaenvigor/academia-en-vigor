
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(path: Path, content: str = ''):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + '\n', encoding='utf-8')


def write_json(path: Path, data):
    write(path, json.dumps(data, ensure_ascii=False, indent=2))


def display_name(opposition: str) -> str:
    return {'policia-nacional': 'Policía Nacional', 'guardia-civil': 'Guardia Civil'}.get(opposition, opposition.replace('-', ' ').title())


def prefix(opposition: str) -> str:
    return {'policia-nacional': 'PN', 'guardia-civil': 'GC'}.get(opposition, opposition[:2].upper())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--oposicion', required=True)
    parser.add_argument('--tema', type=int, required=True)
    parser.add_argument('--titulo', required=True)
    parser.add_argument('--slug', required=True)
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()

    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.slug):
        raise SystemExit('El slug solo puede contener minúsculas, números y guiones.')
    nn = f'{args.tema:02d}'
    code = f'tema-{nn}'
    knowledge = ROOT / f'conocimiento/{args.oposicion}/{code}'
    manifest_path = knowledge / 'manifest.json'
    if manifest_path.exists() and not args.force:
        raise SystemExit(f'Ya existe {manifest_path.relative_to(ROOT)}')

    opp_display = display_name(args.oposicion)
    id_prefix = f'{prefix(args.oposicion)}-T{nn}'
    source = f'conocimiento/{args.oposicion}/{code}/master.md'
    parte = f'temas/{args.oposicion}/parte/{code}-{args.slug}.md'
    atestado = f'temas/{args.oposicion}/atestado/{code}-{args.slug}.md'
    bank = f'banco-preguntas/{args.oposicion}/{code}/preguntas.jsonl'
    coverage = f'conocimiento/{args.oposicion}/{code}/cobertura.json'
    eval_plan = f'evaluaciones/{args.oposicion}/{code}/plan.json'
    asset_manifest = f'assets/{args.oposicion}/{code}/manifest.json'
    materials_manifest = f'materiales-didacticos/{args.oposicion}/{code}/manifest.json'
    official_index = f'banco-preguntas/{args.oposicion}/{code}/indice-oficiales.json'

    master = f"""# TEMA {args.tema} · {args.titulo.upper()}

<!-- content_version: 0.1.0 -->
<!-- opposition: {args.oposicion} -->
<!-- status: draft; publication: not_published -->

<!-- BLOCK 01 START -->
## 1. Bloque pendiente
**Fuente principal:** `PENDIENTE`
<!-- PARTE START -->
Contenido esencial pendiente.

:::perla-vigor
Perla pendiente.
:::

:::visual
**Referencia visual prevista:** `t{nn}-01-pendiente.png` · descripción pendiente.
:::
<!-- PARTE END -->
<!-- ATESTADO START -->
Desarrollo normativo y pedagógico pendiente.

:::hablemos-claro
Explicación directa pendiente.
:::

:::en-la-calle
Aplicación práctica pendiente.
:::

:::lo-que-cae
Prioridad de examen pendiente.
:::

:::visual
**Referencia visual prevista:** `t{nn}-01-pendiente.png` · descripción pendiente.
:::
<!-- ATESTADO END -->
<!-- BLOCK 01 END -->

<!-- LAYER:MAPA -->
# Mapa del tema

:::visual
**Mapa general previsto:** `t{nn}-01-mapa-general.png` · recorrido completo del tema.
:::

<!-- LAYER:CONTENIDO -->
# Contenido
Pendiente.

<!-- LAYER:HABLEMOS_CLARO -->
# Hablemos claro

:::hablemos-claro
Pendiente.
:::

<!-- LAYER:EN_LA_CALLE -->
# En la calle

:::en-la-calle
Pendiente.
:::

<!-- LAYER:LO_QUE_CAE -->
# Lo que cae

:::lo-que-cae
Pendiente.
:::

<!-- LAYER:HA_CAIDO -->
# Ha caído

:::ha-caido
No hay referencias oficiales activas hasta completar la verificación y el mapeo.
:::
"""
    write(ROOT / source, master)

    manifest = {
        'schema_version': '1.3.0',
        'opposition': args.oposicion,
        'opposition_display_name': opp_display,
        'topic': code,
        'topic_number': args.tema,
        'slug': args.slug,
        'title': args.titulo,
        'content_version': '0.1.0',
        'editorial_status': 'draft',
        'publication_status': 'not_published',
        'normative_status': 'pending_review',
        'source_file': source,
        'outputs': {'parte': parte, 'atestado': atestado},
        'semantic_blocks': 1,
        'atomic_facts': 0,
        'coverage_file': coverage,
        'official_references': [],
        'official_exam_items': [],
        'official_exam_index': official_index,
        'layers': ['Mapa del tema', 'Contenido', 'Hablemos claro', 'En la calle', 'Lo que cae', 'Ha caído'],
        'question_bank': {'path': bank, 'manifest': f'banco-preguntas/{args.oposicion}/{code}/manifest.json', 'questions': 0, 'coverage_by_atomic_facts': 0.0},
        'evaluations': {'plan': eval_plan, 'generator': 'scripts/generar_evaluaciones.py'},
        'assets': {'manifest': asset_manifest, 'total': 0},
        'teaching_materials': {'manifest': materials_manifest, 'categories': ['infografias', 'presentaciones', 'audios', 'videos']},
    }
    write_json(manifest_path, manifest)
    write_json(ROOT / coverage, {'schema_version': '1.0.0', 'content_version': '0.1.0', 'topic': code, 'facts': []})
    write(knowledge / 'revision-0.1.md', f'# Revisión inicial · Tema {args.tema}\n\nEstado: borrador.\n')

    write(ROOT / parte, '')
    write(ROOT / atestado, '')

    bank_root = ROOT / f'banco-preguntas/{args.oposicion}/{code}'
    write(bank_root / 'preguntas.jsonl', '')
    write_json(bank_root / 'manifest.json', {
        'schema_version': '1.3.0', 'content_version': '0.1.0', 'oposicion': args.oposicion,
        'tema': args.tema, 'estado': 'draft', 'publicacion': 'not_published', 'total_preguntas': 0,
        'total_hechos': 0, 'hechos_cubiertos': 0, 'cobertura_por_hechos': 0.0,
        'distribucion_respuestas': {'A': 0, 'B': 0, 'C': 0}, 'caracter': {'propias': 0, 'oficiales': 0},
        'fuente_conocimiento': f'../../../{source}', 'cobertura': f'../../../{coverage}',
        'evaluation_plan': f'../../../{eval_plan}', 'official_exam_index': 'indice-oficiales.json',
    })
    write_json(bank_root / 'indice-oficiales.json', {
        'schema_version': '1.1.0', 'profile_id': prefix(args.oposicion).lower(), 'theme_id': f'{prefix(args.oposicion).lower()}-t{nn}',
        'theme_number': args.tema, 'theme_title': args.titulo, 'questions': [],
        'statistics': {'mapped_questions': 0, 'verified_questions': 0, 'active_ha_caido': 0},
    })
    write(bank_root / 'README.md', f'# Banco propio · Tema {args.tema}\n')

    write_json(ROOT / eval_plan, {
        'schema_version': '1.1.0', 'content_version': '0.1.0', 'opposition': args.oposicion,
        'topic_number': args.tema, 'topic_title': args.titulo, 'id_prefix': id_prefix,
        'bank': bank, 'output': f'build/evaluaciones/{args.oposicion}/{code}/tests-generados',
        'coverage_tests': {'description': 'Pendiente', 'max_questions_per_test': 25, 'blocks': [{'number': 1, 'title': 'Bloque pendiente'}]},
        'part_tests': {'questions_per_test': 25, 'variants': [], 'parts': []}, 'final_tests': [],
    })
    write(ROOT / f'evaluaciones/{args.oposicion}/{code}/README.md', f'# Evaluaciones · Tema {args.tema}\n')

    write_json(ROOT / asset_manifest, {
        'schema_version': '1.1.0', 'opposition': args.oposicion, 'topic': code,
        'content_version': '0.1.0', 'visual_version': '0.0.0', 'resources': [],
    })
    write(ROOT / f'assets/{args.oposicion}/{code}/README.md', f'# Assets · Tema {args.tema}\n')

    materials_root = ROOT / f'materiales-didacticos/{args.oposicion}/{code}'
    write_json(ROOT / materials_manifest, {
        'schema_version': '1.2.0', 'opposition': args.oposicion, 'topic': code,
        'content_version': '0.1.0', 'source_version': '0.1.0', 'status': 'estructura_preparada',
        'categories': {'infografias': 'infografias/', 'presentaciones': 'presentaciones/', 'audios': 'audios/', 'videos': 'videos/'},
        'production': {'briefing': 'produccion/briefing.md', 'sources': 'produccion/fuentes.md', 'prompts': 'produccion/prompts.md'},
        'storage_policy': 'external_by_default_for_audio_video_and_heavy_files',
        'rights_policy': 'own_or_explicitly_authorized_only', 'resources': [],
    })
    for category in ('infografias', 'presentaciones', 'audios', 'videos'):
        write(materials_root / category / 'README.md', f'# {category.title()} · Tema {args.tema}\n')
    write(materials_root / 'produccion/briefing.md', f'# Briefing · Tema {args.tema}\n\nFuente: `{atestado}`.\n')
    write(materials_root / 'produccion/fuentes.md', '# Fuentes autorizadas\n\nPendiente.\n')
    write(materials_root / 'produccion/prompts.md', '# Prompts de producción\n\nPendiente.\n')

    index_path = ROOT / 'temario.json'
    index = json.loads(index_path.read_text(encoding='utf-8'))
    opposition = index.setdefault('oppositions', {}).setdefault(args.oposicion, {'display_name': opp_display, 'topics': []})
    if any(int(item['number']) == args.tema for item in opposition.get('topics', [])) and not args.force:
        raise SystemExit('El tema ya está registrado en temario.json')
    opposition['topics'] = [item for item in opposition.get('topics', []) if int(item['number']) != args.tema]
    opposition['topics'].append({
        'number': args.tema, 'slug': args.slug, 'title': args.titulo, 'content_version': '0.1.0',
        'editorial_status': 'draft', 'publication_status': 'not_published', 'manifest': str(manifest_path.relative_to(ROOT)),
        'parte': parte, 'atestado': atestado, 'question_bank': bank, 'evaluation_plan': eval_plan,
        'assets': asset_manifest, 'teaching_materials': materials_manifest, 'official_exam_index': official_index,
        'official_exam_mapped': 0, 'official_exam_verified': 0, 'ha_caido_active': 0,
    })
    opposition['topics'].sort(key=lambda item: int(item['number']))
    write_json(index_path, index)

    from compilar_tema import process
    process(args.oposicion, args.tema, write=True, check=False)
    print(f'CREADO: {args.oposicion}/{code}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
