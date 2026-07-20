
# Exámenes oficiales históricos

## Finalidad

Permiten saber qué conceptos han aparecido y vincularlos con hechos atómicos. No son la fuente jurídica del temario.

## Separación

- Preguntas propias: `banco-preguntas/<oposicion>/tema-NN/preguntas.jsonl`.
- Históricas: `banco-preguntas/<oposicion>/oficiales/`.
- Relación con un tema: `banco-preguntas/<oposicion>/tema-NN/indice-oficiales.json`.

## Estados

- `quarantine`: pregunta útil para revisión interna, sin activación pública.
- `verified`: cuestionario y respuesta final oficialmente contrastados.

## «Ha caído»

Solo se activa si se cumplen simultáneamente:

1. `status` es `verified`;
2. existe `official_answer_option_id`;
3. la plantilla final oficial está identificada;
4. el mapeo al tema y al hecho atómico ha sido revisado;
5. `counts_for_ha_caido` es `true`.

Las respuestas propuestas no se presentan como oficiales.
