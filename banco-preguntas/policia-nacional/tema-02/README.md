# Banco propio · Tema 2

212 preguntas propias sobre los 209 hechos atómicos del Tema 2.
Cobertura por hechos: 100.0 %. Bloques 1 a 37, partes 1 a 7.

## Qué cambia respecto al banco anterior

El banco previo tenía 418 preguntas generadas con dos plantillas fijas. El enunciado
citaba literalmente el concepto preguntado, los distractores eran enunciados de otros
conceptos y el campo `feedback` repetía el mismo texto en las tres opciones.

Este banco reescribe las preguntas en estilo de examen oficial: el enunciado plantea
el supuesto sin nombrar la respuesta y los distractores recogen las confusiones reales
(por ejemplo, autorización previa frente a comunicación previa en el derecho de reunión,
o el estado de alarma incluido entre los que permiten suspender derechos).

## Campos de retroalimentación

- `feedback`: una línea por opción, explicando por qué es correcta o incorrecta.
- `retroalimentacion`: `acierto` y `fallo`, cada uno con `humor` y `explicacion`.
  El comentario con humor va primero, para que el alumno lo asocie al contenido.

## Generación de tests

- Test por bloque: filtrar por `bloque` (1 a 37).
- Test por partes: filtrar por `parte` (1 a 7).
- Test completo de 25 o 50: muestrear repartiendo por `parte` y ponderando por
  `riesgo_examen`, de modo que los hechos de riesgo 5 salgan con más frecuencia.

## Estado

Todas las preguntas están en `estado_revision: "generado_pendiente_revision_editorial"`.
El `publication_gate` del manifiesto sigue vigente: revisión humana de distractores y
feedback antes de publicar.

## Pendiente de verificar

El hecho `PN-T02-F020` (reforma de 2026 del artículo 69.3, senador propio de Formentera)
y el `PN-T02-F021` (cuatro reformas) proceden del master.md. Conviene contrastarlos con
el BOE antes de publicar: de ellos dependen tres preguntas del bloque 4.
