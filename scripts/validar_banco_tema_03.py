#!/usr/bin/env python3
from pathlib import Path
from collections import Counter,defaultdict
import json,sys
ROOT=Path(__file__).resolve().parents[1]
COV=json.loads((ROOT/'conocimiento/policia-nacional/tema-03/cobertura.json').read_text(encoding='utf-8'))
P=ROOT/'banco-preguntas/policia-nacional/tema-03/preguntas.jsonl'
Q=[json.loads(x) for x in P.read_text(encoding='utf-8').splitlines() if x.strip()]
errors=[]
ids=[q['id'] for q in Q]
if len(ids)!=len(set(ids)): errors.append('IDs de preguntas duplicados')
facts={f['id'] for f in COV['facts']}
qfacts={q['fact_id'] for q in Q}
if facts-qfacts: errors.append(f'Hechos sin pregunta: {sorted(facts-qfacts)[:10]}')
if qfacts-facts: errors.append(f'Preguntas huérfanas: {sorted(qfacts-facts)[:10]}')
for q in Q:
 if set(q['opciones'])!={'A','B','C'}: errors.append(f"Opciones inválidas {q['id']}")
 if len(set(q['opciones'].values()))!=3: errors.append(f"Opciones repetidas {q['id']}")
 if q['respuesta_correcta'] not in q['opciones']: errors.append(f"Respuesta inválida {q['id']}")
 if q['caracter']!='propio' or q['referencia_oficial'] is not None: errors.append(f"Atribución oficial indebida {q['id']}")
c=Counter(q['respuesta_correcta'] for q in Q)
if max(c.values())-min(c.values())>1: errors.append(f'Distribución desequilibrada: {c}')
byfact=defaultdict(int)
for q in Q: byfact[q['fact_id']]+=1
risk5={f['id'] for f in COV['facts'] if f['risk']==5}
if any(byfact[x]<2 for x in risk5): errors.append('Hay hechos de riesgo 5 con menos de dos preguntas')
if errors:
 print('\n'.join(errors)); raise SystemExit(1)
print(f"OK: {len(Q)} preguntas; {len(facts)} hechos cubiertos; respuestas {dict(c)}")
