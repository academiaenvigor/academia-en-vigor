# Sincronización del índice y migración de callouts

**Fecha:** 29 de julio de 2026

> Informe histórico. El estado vigente queda documentado en
> `revision-integral-temas-01-09-2026-07-29.md`.

**Motivo:** el informe `revision-homologacion-temas-01-09-2026-07-29.md`
describía una homologación que no llegó al repositorio. `temario.json` seguía
con los valores anteriores, `validar_proyecto.py` fallaba con seis errores y el
workflow de CI estaba en rojo en cada push.

## Causa

`temario.json` es un índice derivado, pero se editaba a mano. La lógica que lo
recalculaba vivía dentro de `homologar_temas_01_06.py`, un script de un solo uso
limitado a los temas 1 a 6, así que los temas 7, 8 y 9 nunca pasaron por ella.

Además, `tests/test_bloques_vigor.py` estaba escrito con funciones sueltas al
estilo pytest. El workflow usa `unittest discover`, que no las recoge: sus
cuatro casos llevaban tiempo sin ejecutarse en CI.

## Cambios

- **`scripts/sincronizar_temario.py`** (nuevo). Recalcula los diez campos
  derivados del índice para cualquier tema y oposición. Corrigió 17 desvíos:
  `question_count` de los temas 1, 2 y 4; los diez campos del tema 8; los
  contadores oficiales de los temas 5 y 9; `visual_version` de los temas 7 y 9.
- **`scripts/migrar_callouts.py`** (nuevo). Convierte los avisos en cita a la
  sintaxis `:::`. Migró 99 callouts: 75 del tema 3 y 24 del tema 7, que hasta
  ahora quedaban fuera de los filtros del explorador. El tema 3 pasa de 0 a 25
  bloques con las tres capas del Atestado; el tema 7, de 0 a 6.
- **`scripts/validar_temas.py`**. Seis comprobaciones nuevas: los contadores de
  antecedentes oficiales, la versión de contenido, los dos estados y la versión
  visual del índice se contrastan contra sus fuentes.
- **`tema-02/master.md`**. Tres cabeceras de nivel 1 dentro del bloque 37 se
  compilaban como capas falsas del Atestado, numeradas 38 a 40 en un tema de 37
  bloques. Pasan a anexos de nivel 3. El contenido se conserva íntegro.
- **`tests/`**. `test_bloques_vigor.py` reescrito en `unittest` y extendido a
  los nueve temas; nuevo `test_sincronizacion_temario.py`.
- **`.github/workflows/validar.yml`**. Dos pasos nuevos: índice sincronizado y
  ausencia de callouts antiguos.

## Estado tras los cambios

- las seis capas son idénticas en los 18 documentos derivados;
- 78 pruebas en verde;
- `validar_proyecto.py` sin errores ni avisos;
- 0 desvíos en el índice y 0 callouts en formato antiguo.

## Pendiente en aquella revisión

La densidad de avisos por bloque seguía siendo desigual: los temas 4 y 5
repetían avisos del Parte, los temas 8 y 9 no tenían trampas y el tema 6
presentaba una densidad menor. La revisión integral posterior corrige los
problemas estructurales, amplía el Atestado del Tema 8 y añade contrastes al
Tema 9.
