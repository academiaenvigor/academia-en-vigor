# Banco propio · Tema 1

203 preguntas propias sobre 200 hechos atómicos extraídos del
`master.md` del Tema 1, versión 0.2.0. Cobertura por hechos: 100.0 %.

## Archivos

- `preguntas.jsonl` — una pregunta por línea, numeradas de corrido y ordenadas por bloque.
- `manifest.json` — totales, distribuciones y criterios de generación de tests.
- `cobertura.json` — hechos atómicos con los identificadores de las preguntas que los cubren.
  Sustituye al de `conocimiento/policia-nacional/tema-01/`, que estaba en
  `pending_atomic_fact_extraction` con la lista de hechos vacía.

## Formato de pregunta

Igual que el banco del Tema 3, con un campo añadido:

```json
"retroalimentacion": {
  "acierto": { "humor": "...", "explicacion": "..." },
  "fallo":   { "humor": "...", "explicacion": "..." }
}
```

## Generación de tests

- Test por bloque: filtrar por `bloque`.
- Test por puntos: filtrar por `punto`.
- Test completo de 25 o 50: muestrear repartiendo por `punto` y ponderando por
  `riesgo_examen`, de modo que los hechos de riesgo 5 aparezcan con más frecuencia.

No hace falta almacenar los tests: se construyen al vuelo desde el banco.

## Estado

Todas las preguntas están en `estado_revision: "generado_pendiente_revision_editorial"`.
Tras la revisión, cambiar a `revisado_fuente_oficial`, como en el Tema 3.
