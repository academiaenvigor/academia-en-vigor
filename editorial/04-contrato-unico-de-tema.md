# Contrato único de tema · Academia En Vigor

**Versión:** 2.0.0  
**Ámbito:** Policía Nacional · Temas 1–45

Este contrato impide que cada tema evolucione con una estructura distinta. Las
diferencias de extensión, número de bloques, imágenes o preguntas son legítimas;
las diferencias de esquema, trazabilidad y rutas no lo son.

## Fuente única

Cada tema nace de:

`conocimiento/policia-nacional/tema-NN/master.md`

La fuente debe contener:

- bloques `BLOCK NN` con una fuente principal;
- contenido separado para El Parte y El Atestado;
- seis capas: Mapa, Contenido, Hablemos claro, En la calle, Lo que cae y Ha caído;
- una única ancla `FACT` por hecho atómico, situada en El Atestado.

El Parte y El Atestado son derivados. Deben poder regenerarse con:

```bash
python scripts/compilar_tema.py --all --write
```

La comprobación `--check` debe terminar sin diferencias.

## Rutas obligatorias

Todo tema registrado en `temario.json` debe tener:

- manifiesto, fuente maestra y cobertura;
- El Parte y El Atestado;
- banco propio, manifiesto e índice de antecedentes oficiales;
- plan de evaluación;
- manifiesto visual;
- manifiesto y estructura de materiales didácticos;
- informe de revisión.

## Trazabilidad

`cobertura.json` usa el esquema 2.0.0. Cada hecho incluye el mismo conjunto de
campos y debe:

- tener un ID único;
- señalar bloque, parte, fuente, riesgo y versión;
- enlazar sus preguntas propias;
- aparecer exactamente una vez en la fuente maestra y una vez en El Atestado;
- quedar asociado a un fragmento textual verificable.

## Banco propio

Todas las preguntas usan:

- tres opciones A/B/C distintas;
- una única respuesta correcta;
- referencia a un hecho existente;
- retroalimentación separada de acierto y fallo;
- en cada rama, entrada con humor y explicación;
- carácter propio y ninguna atribución oficial.

La estructura puede estar homologada aunque el banco siga bloqueado. La puerta
de calidad solo pasa cuando:

- todos los hechos están cubiertos;
- los hechos de riesgo 5 tienen dos formulaciones;
- el reparto A/B/C difiere como máximo en una respuesta;
- la revisión editorial está cerrada.

Un banco bloqueado no puede presentarse como terminado.

## Antecedentes oficiales

El índice de antecedentes usa el esquema 2.0.0. Separa siempre:

- aparición localizada;
- bloque asignado;
- respuesta verificada;
- regla vigente o histórica;
- permiso para mostrar la respuesta.

Una respuesta verificada por el equipo no se presenta como plantilla oficial.

## Recursos visuales

El manifiesto distingue:

- `integrated`: el WEBP debe existir, estar inventariado y respetar el límite;
- `planned`: el archivo puede no existir y no rompe la compilación.

No se admiten WEBP huérfanos. Los recursos planificados permanecen invisibles en
los documentos del alumno hasta integrarse.

## Materiales didácticos

Todos los temas usan el esquema 2.1.0, las cuatro categorías comunes y una
división explícita por partes. Cada parte tiene bloques y un bloque de anclaje.
Los archivos pesados se almacenan fuera del repositorio y deben ser propios o
estar expresamente autorizados.

## Validación obligatoria

Antes de entregar o publicar un tema:

```bash
python scripts/validar_temas.py
python -m unittest discover -s tests -v
python scripts/validar_proyecto.py
```

Los errores impiden la entrega. Los avisos de puerta de calidad permiten
conservar un borrador, pero impiden declararlo terminado.
