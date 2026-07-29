# Revisión integral de los Temas 1 a 9

**Fecha:** 29 de julio de 2026  
**Versión del proyecto:** 0.9.1  
**Estado:** validación técnica completa; publicación no activada

## Resultado

Los nueve temas vuelven a superar conjuntamente el contrato VIGOR. La revisión
se realizó sobre una copia limpia de `main` y abarcó fuentes maestras,
derivados, bancos, evaluaciones, visuales, antecedentes oficiales, explorador,
documentación y CI.

## Correcciones visuales

- Se sustituyeron cuatro ilustraciones del Tema 4 que eran copias exactas de
  otras infografías por escenas propias y diferenciadas.
- Se eliminaron las referencias repetidas de los Temas 1, 2, 6 y 8.
- Se recuperaron las referencias declaradas pero ausentes de los Temas 1, 2, 4,
  5 y 8.
- Los manifiestos visuales utilizan solo los tipos canónicos `infografia` e
  `ilustracion_simple`.
- Cada recurso declarado aparece exactamente una vez en cada documento al que
  pertenece.
- El repositorio conserva únicamente los WebP optimizados; no se añadieron PNG.
- Se incorporó `scripts/validar_activos_visuales.py` y su prueba de regresión.

## Correcciones editoriales

- Las capas finales de los Temas 3 y 7 usan callouts semánticos como el resto.
- La cobertura del Tema 7 vuelve a declarar sus dieciséis bloques.
- El plan de evaluación del Tema 3 queda en estado `ready` y su banco usa la
  misma puerta de publicación que los demás temas aprobados.
- El Atestado del Tema 8 incorpora veintiocho contrastes específicos y supera
  en más de un 30 % la extensión de El Parte.
- El Tema 9 incorpora seis trampas de examen en confusiones nucleares.
- Las cajas VIGOR mantienen tipografía de cuerpo homogénea, también al final de
  cada tema.

## Antecedentes oficiales

- El explorador reconoce `reviewed` y `editorially_mapped`.
- Las propuestas `auto_proposed` quedan ocultas hasta revisión.
- `show_answer` y `show_feedback` se respetan de forma efectiva.
- Ningún antecedente se presenta como plantilla oficial.
- «Ha caído» permanece desactivado mientras no exista cotejo final conforme a
  la política del repositorio.

## Automatización y controles

El workflow comprueba ahora, de forma explícita:

1. derivados reproducibles;
2. `temario.json` sincronizado;
3. ausencia de callouts antiguos;
4. suite `unittest`;
5. contrato integral, bancos, derechos, materiales, exámenes y visuales.

La revisión termina con:

- 9 temas compilados y homologados;
- 85 pruebas automatizadas superadas;
- 3.700 preguntas propias validadas;
- 1.000 preguntas históricas inventariadas, sin duplicados;
- 240 recursos visuales integrados, todos en WebP y sin referencias repetidas;
- 0 desvíos en `temario.json`;
- 0 callouts antiguos;
- 0 documentos de terceros o binarios pesados no permitidos.

## Estados que se conservan deliberadamente

Los Temas 1, 2, 4 y 5 continúan en `draft_review`: cambiar ese estado equivaldría
a registrar una aprobación humana que todavía no consta. Los nueve temas están
técnicamente completos, pero esos cuatro conservan su puerta editorial.

El repositorio remoto no se modifica desde esta revisión. Su visibilidad pública
tampoco se cambia automáticamente, porque hacerlo puede afectar al explorador
publicado. La separación entre contenido editorial privado y entrega pública
debe decidirse antes de alterar esa configuración.
