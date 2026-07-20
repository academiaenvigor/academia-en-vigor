
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_topics() -> list[tuple[str, int]]:
    data = json.loads((ROOT / 'temario.json').read_text(encoding='utf-8'))
    return [
        (opposition, int(topic['number']))
        for opposition, info in data.get('oppositions', {}).items()
        for topic in info.get('topics', [])
    ]


def validate_topic(opposition: str, topic: int) -> list[str]:
    code = f'tema-{topic:02d}'
    prefix = 'PN' if opposition == 'policia-nacional' else opposition[:2].upper()
    root = ROOT / f'banco-preguntas/{opposition}/{code}'
    manifest_path = root / 'manifest.json'
    coverage_path = ROOT / f'conocimiento/{opposition}/{code}/cobertura.json'
    questions_path = root / 'preguntas.jsonl'
    errors = []

    for path in (manifest_path, coverage_path, questions_path):
        if not path.exists():
            errors.append(f'Falta {path.relative_to(ROOT)}')
    if errors:
        return errors

    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    coverage = json.loads(coverage_path.read_text(encoding='utf-8'))
    questions = [json.loads(line) for line in questions_path.read_text(encoding='utf-8').splitlines() if line.strip()]
    facts = {fact['id'] for fact in coverage.get('facts', [])}
    ids = [question.get('id') for question in questions]
    if len(ids) != len(set(ids)):
        errors.append(f'{opposition}/{code}: IDs duplicados')

    expected_id = re.compile(rf'^{re.escape(prefix)}-T{topic:02d}-Q\d{{3,}}$')
    question_facts = set()
    by_fact = defaultdict(int)
    for question in questions:
        qid = question.get('id', '')
        if not expected_id.match(qid):
            errors.append(f'{opposition}/{code}: ID inválido {qid}')
        fact_id = question.get('fact_id')
        question_facts.add(fact_id)
        by_fact[fact_id] += 1
        options = question.get('opciones', {})
        if set(options) != {'A', 'B', 'C'}:
            errors.append(f'Opciones inválidas {qid}')
        elif len(set(options.values())) != 3:
            errors.append(f'Opciones repetidas {qid}')
        if question.get('respuesta_correcta') not in options:
            errors.append(f'Respuesta inválida {qid}')
        if question.get('caracter') != 'propio' or question.get('referencia_oficial') is not None:
            errors.append(f'Atribución oficial indebida {qid}')

    draft = manifest.get('estado') in {'draft', 'borrador'}
    if not draft:
        if facts - question_facts:
            errors.append(f'Hechos sin pregunta: {sorted(facts - question_facts)[:10]}')
        if question_facts - facts:
            errors.append(f'Preguntas huérfanas: {sorted(question_facts - facts)[:10]}')
        if questions:
            distribution = Counter(q['respuesta_correcta'] for q in questions)
            if max(distribution.values()) - min(distribution.values()) > 1:
                errors.append(f'Distribución desequilibrada: {distribution}')
        risk5 = {fact['id'] for fact in coverage.get('facts', []) if fact.get('risk') == 5}
        if any(by_fact[fact] < 2 for fact in risk5):
            errors.append('Hay hechos de riesgo 5 con menos de dos preguntas')

    if manifest.get('total_preguntas') != len(questions):
        errors.append(f'{opposition}/{code}: total_preguntas no coincide con el banco')
    if manifest.get('total_hechos') != len(facts):
        errors.append(f'{opposition}/{code}: total_hechos no coincide con cobertura')

    print(f'OK banco: {opposition}/{code}: {len(questions)} preguntas; {len(facts)} hechos')
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--oposicion', default='policia-nacional')
    parser.add_argument('--tema', type=int, default=3)
    parser.add_argument('--all', action='store_true')
    args = parser.parse_args(argv)
    selected = load_topics() if args.all else [(args.oposicion, args.tema)]
    errors = []
    for opposition, topic in selected:
        errors.extend(validate_topic(opposition, topic))
    if errors:
        print('\n'.join(f'ERROR: {error}' for error in errors))
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
