
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def load_questions(path: Path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]


def balanced(items):
    groups = {letter: [q for q in items if q['respuesta_correcta'] == letter] for letter in 'ABC'}
    output = []
    while any(groups.values()):
        for letter in 'ABC':
            if groups[letter]:
                output.append(groups[letter].pop(0))
    return output


def public_test(test_id, title, blocks, items, test_type, version):
    return {
        'id': test_id,
        'titulo': title,
        'content_version': version,
        'bank_version': version,
        'tipo': test_type,
        'ambito': {'bloques': blocks},
        'numero_preguntas': len(items),
        'preguntas': [
            {key: q[key] for key in ('id', 'fact_id', 'bloque', 'concepto', 'articulo', 'tipo', 'dificultad', 'enunciado', 'opciones')}
            for q in items
        ],
        'soluciones': [
            {key: q[key] for key in ('id', 'respuesta_correcta', 'explicacion', 'fact_id', 'articulo')}
            for q in items
        ],
        'estado': 'generado_validado',
        'publicacion': 'not_published',
    }


def select_round_robin(questions, blocks, count, offset=0):
    pools = {block: balanced([q for q in questions if q['bloque'] == block]) for block in blocks}
    if any(not pool for pool in pools.values()):
        raise RuntimeError(f'Hay bloques sin preguntas: {[b for b, pool in pools.items() if not pool]}')
    positions = {block: offset % len(pools[block]) for block in blocks}
    selected, used_facts = [], set()
    while len(selected) < count:
        added = False
        for block in blocks:
            pool = pools[block]
            for _ in range(len(pool)):
                question = pool[positions[block] % len(pool)]
                positions[block] += 1
                if question['fact_id'] not in used_facts:
                    selected.append(question)
                    used_facts.add(question['fact_id'])
                    added = True
                    break
            if len(selected) >= count:
                break
        if not added:
            break
    if len(selected) != count:
        raise RuntimeError(f'No se pudieron seleccionar {count} hechos únicos para {blocks}')
    return balanced(selected)


def generate(plan_path: Path) -> int:
    plan = read_json(plan_path)
    version = plan['content_version']
    prefix = plan['id_prefix']
    topic_number = int(plan['topic_number'])
    topic_title = plan['topic_title']
    bank_path = ROOT / plan['bank']
    out = ROOT / plan['output']
    questions = load_questions(bank_path)
    if out.exists():
        shutil.rmtree(out)
    if not questions:
        write_json(out / 'catalogo.json', {
            'content_version': version,
            'total_tests': 0,
            'tests_cobertura_bloque': 0,
            'tests_por_partes': 0,
            'tests_finales': 0,
            'tests': [],
        })
        print(f'OK: Tema {topic_number} sin preguntas; catálogo vacío generado')
        return 0

    catalogue, coverage_ids = [], []
    max_size = plan['coverage_tests']['max_questions_per_test']
    for block in plan['coverage_tests']['blocks']:
        number, title = block['number'], block['title']
        pool = balanced([q for q in questions if q['bloque'] == number])
        for index in range(0, len(pool), max_size):
            chunk = pool[index:index + max_size]
            variant = chr(ord('A') + index // max_size)
            test_id = f'{prefix}-B{number:02d}-{variant}'
            relative = Path('por-bloques') / f'{test_id}.json'
            write_json(out / relative, public_test(test_id, f'Tema {topic_number} · Bloque {number}: {title} · Test {variant}', [number], chunk, 'cobertura_bloque', version))
            catalogue.append({'id': test_id, 'ruta': relative.as_posix(), 'tipo': 'cobertura_bloque', 'preguntas': len(chunk), 'bloques': [number]})
            coverage_ids.extend(q['id'] for q in chunk)

    part_plan = plan.get('part_tests', {})
    for part in part_plan.get('parts', []):
        for variant in part_plan.get('variants', []):
            items = select_round_robin(questions, part['blocks'], part_plan['questions_per_test'], variant['offset'])
            test_id = f'{prefix}-{part["code"]}-{variant["id"]}'
            relative = Path('por-partes') / f'{test_id}.json'
            write_json(out / relative, public_test(test_id, f'Tema {topic_number} · {part["title"]} · Test {variant["id"]}', part['blocks'], items, 'test_parte', version))
            catalogue.append({'id': test_id, 'ruta': relative.as_posix(), 'tipo': 'test_parte', 'preguntas': len(items), 'bloques': part['blocks']})

    all_blocks = [block['number'] for block in plan['coverage_tests']['blocks']]
    for final in plan.get('final_tests', []):
        items = select_round_robin(questions, all_blocks, final['questions'], final['offset'])
        test_id = f'{prefix}-FINAL-{final["questions"]}-{final["variant"]}'
        relative = Path('finales') / f'{test_id}.json'
        write_json(out / relative, public_test(test_id, f'Tema {topic_number} · {topic_title} · Test final {final["variant"]}', all_blocks, items, 'test_final', version))
        catalogue.append({'id': test_id, 'ruta': relative.as_posix(), 'tipo': 'test_final', 'preguntas': len(items), 'bloques': all_blocks})

    if Counter(coverage_ids) != Counter(q['id'] for q in questions):
        raise RuntimeError('Los tests de cobertura no contienen exactamente una vez todas las preguntas')

    write_json(out / 'catalogo.json', {
        'content_version': version,
        'total_tests': len(catalogue),
        'tests_cobertura_bloque': sum(e['tipo'] == 'cobertura_bloque' for e in catalogue),
        'tests_por_partes': sum(e['tipo'] == 'test_parte' for e in catalogue),
        'tests_finales': sum(e['tipo'] == 'test_final' for e in catalogue),
        'regla_cobertura': 'Cada pregunta del banco aparece exactamente una vez en el conjunto de tests de cobertura por bloque.',
        'tests': catalogue,
    })
    print(f'OK: {len(catalogue)} tests generados; {len(coverage_ids)} preguntas cubiertas una vez')
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--plan')
    parser.add_argument('--oposicion', default='policia-nacional')
    parser.add_argument('--tema', type=int, default=3)
    args = parser.parse_args(argv)
    plan_path = Path(args.plan) if args.plan else ROOT / f'evaluaciones/{args.oposicion}/tema-{args.tema:02d}/plan.json'
    if not plan_path.is_absolute():
        plan_path = ROOT / plan_path
    return generate(plan_path)


if __name__ == '__main__':
    raise SystemExit(main())
