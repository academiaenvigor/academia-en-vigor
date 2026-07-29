# Homologación global de los Temas 1 a 9

**Fecha:** 29 de julio de 2026

**Versión del proyecto:** 0.9.0

> Informe histórico. La revisión correctiva posterior queda documentada en
> `revision-integral-temas-01-09-2026-07-29.md`.

**Estado de publicación:** no publicado para alumnos

## Motivo

Cerrar las incoherencias detectadas después de incorporar el Tema 9 y aplicar
el contrato único vigente a los nueve temas existentes.

## Alcance

- restauración en `temario.json` de los contadores y estados reales del Tema 8;
- sincronización de hechos, preguntas, visuales y antecedentes de los nueve temas;
- normalización de `official_exam_verified` y `ha_caido_active` para no presentar
  respuestas revisadas por el equipo como plantillas oficiales;
- incorporación de 146 segundas formulaciones de riesgo 5 al Tema 1;
- incorporación de 167 segundas formulaciones de riesgo 5 al Tema 2;
- incorporación de 251 segundas formulaciones de riesgo 5 al Tema 4;
- equilibrio A/B/C y cierre de las puertas de calidad de esos tres bancos;
- eliminación de enunciados y conjuntos de opciones duplicados en los bancos
  afectados;
- normalización de los planes de evaluación de los Temas 1, 2, 4 y 5;
- sincronización de los recuentos de preguntas en los manifiestos de conocimiento.

## Archivos afectados

- `temario.json`;
- bancos, coberturas y manifiestos de los Temas 1, 2 y 4;
- planes de evaluación de los Temas 1, 2, 4 y 5;
- manifiestos de conocimiento de los Temas 1, 2 y 4;
- documentación de los bancos homologados.

## Validaciones

- compilación reproducible de El Parte y El Atestado para los nueve temas;
- contrato universal superado por los nueve temas;
- bancos completos, equilibrados y con doble formulación en riesgo 5;
- evaluaciones generadas para los nueve temas con cobertura única del banco;
- materiales, derechos y exámenes históricos validados;
- 70 pruebas automatizadas superadas en aquella revisión;
- ausencia de PNG, fuentes privadas y binarios pesados no permitidos.
