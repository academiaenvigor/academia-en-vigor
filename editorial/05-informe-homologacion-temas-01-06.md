# Informe de homologación · Temas 1–6

**Contrato aplicado:** 2.0.0  
**Materiales didácticos:** 2.1.0  
**Fecha de cierre:** 27 de julio de 2026

## Resultado estructural

| Tema | Bloques | Hechos | Preguntas | Visuales integrados | Visuales planificados | Contrato |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 29 | 200 | 203 | 27 | 0 | Correcto |
| 2 | 37 | 209 | 212 | 22 | 0 | Correcto |
| 3 | 25 | 470 | 738 | 28 | 0 | Correcto |
| 4 | 28 | 367 | 367 | 43 | 0 | Correcto |
| 5 | 35 | 383 | 657 | 0 | 45 | Correcto |
| 6 | 14 | 94 | 0 | 11 | 0 | Correcto |

Los seis temas:

- nacen de una fuente maestra compilable;
- generan El Parte y El Atestado sin diferencias pendientes;
- mantienen una ancla única por hecho en El Atestado;
- usan los mismos esquemas para conocimiento, cobertura, banco, antecedentes,
  evaluación, visuales y materiales;
- tienen todas sus fuentes inventariadas;
- distinguen recursos integrados y planificados;
- superan el validador universal.

## Cambios de saneamiento

- T4 y T5 se migraron desde mantenimiento manual a fuente maestra compilable.
- T1, T2, T4 y T5 recibieron trazabilidad textual completa.
- T3 recibió retroalimentación diferenciada de acierto y fallo sin cambiar
  enunciados, opciones, claves ni explicaciones.
- Los índices de antecedentes oficiales usan ya el mismo esquema.
- `full_tests` se sustituyó por `final_tests`.
- Se añadieron los scaffolds que faltaban en T4 y T5.
- Se retiraron 30 WEBP no inventariados: dos duplicados de T2 y veintiocho
  versiones sustituidas de T4.
- Los 45 visuales de T5 permanecen planificados y dejan de romper la
  validación mientras no se declaren integrados.

## Puertas de calidad del banco

La estructura está homologada, pero no todos los bancos están terminados.

| Tema | Estado del banco | Pendiente real |
|---:|---|---|
| 1 | Bloqueado | 146 segundas formulaciones de riesgo 5 y reequilibrio A/B/C |
| 2 | Bloqueado | 167 segundas formulaciones de riesgo 5 |
| 3 | Aprobado | Nada estructural |
| 4 | Bloqueado | 251 segundas formulaciones de riesgo 5 y reequilibrio A/B/C |
| 5 | Aprobado | Nada estructural |
| 6 | Bloqueado | Banco todavía no iniciado; 66 hechos de riesgo 5 exigirán doble formulación |

Estos bloqueos son deliberados. Generar variantes automáticas de baja calidad
habría hecho pasar los contadores a costa de empeorar el banco.

## Pruebas

- 59 pruebas unitarias superadas.
- Compilación limpia de 6 fuentes maestras y 12 derivados.
- Validador universal superado por los 6 temas.
- Validación global de estructura, derechos, materiales, bancos y antecedentes
  oficiales superada.
- Migración comprobada como idempotente: ejecutarla dos veces no cambia ningún
  archivo.
