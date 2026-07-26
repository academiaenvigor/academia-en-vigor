# Banco propio · Tema 4 · La Unión Europea

367 preguntas propias sobre los 367 hechos atómicos del Tema 4.
Cobertura por hechos: 100.0 %. Bloques 1 a 28, partes 1 a 8.

## Origen

Las preguntas se han generado a partir del `master.md` del tema, del que se
extrajeron 367 hechos atómicos, uno por enunciado cerrado. Cada hecho tiene
al menos una pregunta asociada.

## Estilo

Preguntas de examen oficial con tres opciones. El enunciado plantea el supuesto
sin nombrar la respuesta, y los distractores recogen las confusiones reales del
alumno: los tres Consejos, reglamento frente a directiva, Interpol frente a
Europol, o Estrasburgo frente a Luxemburgo.

## Campos de retroalimentación

- `feedback`: una línea por opción, explicando por qué es correcta o incorrecta.
- `retroalimentacion`: `acierto` y `fallo`, cada uno con `humor` y `explicacion`.
  El comentario con humor va primero, para que el alumno lo asocie al contenido.

## Generación de tests

- Test por bloque: filtrar por `bloque` (1 a 28).
- Test por parte: filtrar por `parte` (1 a 8).
- Test completo de 25 o 50: muestrear repartiendo por `parte` y ponderando por
  `riesgo_examen`.

## Estado

Todas las preguntas están en `estado_revision: "generado_pendiente_revision_editorial"`.
El `publication_gate` sigue vigente: revisión humana antes de publicar.

## Datos volátiles

Varias preguntas dependen de cifras que cambian entre convocatorias: escaños del
Parlamento Europeo, Estados de la zona del euro, países del espacio Schengen,
miembros de Interpol y del Consejo de Europa. Están verificadas a 25 de julio de
2026. La lista completa está en `volatile_data`, dentro del manifiesto de
conocimiento del tema.
