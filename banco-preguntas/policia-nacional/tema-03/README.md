# Banco de preguntas · Policía Nacional · Tema 3

`preguntas.jsonl` es la fuente canónica. Cada línea contiene una pregunta independiente vinculada mediante `fact_id` a `cobertura.json`.

## Estado

- 738 preguntas propias.
- 470 hechos cubiertos.
- Tres opciones por pregunta.
- Respuestas equilibradas: 246 A, 246 B y 246 C.
- No publicado para alumnos.
- Ninguna pregunta se atribuye a una convocatoria oficial.

Los tests se generan con `scripts/generar_evaluaciones_tema_03.py` y se escriben en `build/`.
