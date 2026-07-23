
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

## Marca de aparición durante la lectura

La marca compacta `Preguntado en examen · AÑO` tiene una finalidad distinta:
indica que un bloque del temario está relacionado con un enunciado del banco
histórico cuyo mapeo editorial se ha revisado.

- Se genera desde `indice-oficiales.json`; los años no se escriben a mano en el
  temario.
- Puede mostrarse aunque la respuesta final siga en cuarentena.
- Al desplegarla se muestra el enunciado, pero no se señala una solución como
  oficial.
- Solo las preguntas que cumplan todos los requisitos de la sección anterior
  pueden activar la capa «Ha caído».

Esta separación permite enseñar antecedentes útiles sin convertir una respuesta
propuesta o una plantilla no cotejada en una respuesta oficial.
