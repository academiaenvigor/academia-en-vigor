# Academia En Vigor

**El temario que nunca duerme.**

Repositorio editorial de Academia En Vigor para la preparación de Policía Nacional. Esta base limpia comienza con el **Tema 3 · La Constitución Española (II)**, terminado como versión interna `0.3.0`.

## Regla principal

Solo entra en este repositorio un tema que tenga:

1. fuente maestra en `conocimiento/`;
2. El Parte y El Atestado compilados desde esa fuente;
3. cobertura de hechos atómicos;
4. banco de preguntas validado;
5. plan de evaluaciones reproducible;
6. fuentes y estado editorial registrados.

Los documentos generados no sustituyen a la fuente maestra. Los materiales de NotebookLM tampoco se consideran fuentes jurídicas.

## Estado actual

| Elemento | Estado |
|---|---|
| Tema 3 · fuente maestra | Cerrado internamente · v0.3.0 |
| El Parte | Generado y validado |
| El Atestado | Generado y validado |
| Hechos atómicos | 470 |
| Banco propio | 738 preguntas |
| Cobertura | 470/470 hechos |
| Evaluaciones | Plan reproducible: 61 tests |
| Preguntas oficiales | Ninguna incorporada sin trazabilidad |
| Publicación para alumnos | No publicada |

## Estructura

```text
editorial/          normas internas del Método VIGOR
fuentes/            catálogo de fuentes oficiales
conocimiento/       fuente maestra, manifiesto, cobertura y revisiones
temas/              El Parte y El Atestado derivados
banco-preguntas/    banco canónico y esquema
evaluaciones/       plan para generar tests
materiales/         instrucciones y registro de materiales derivados
scripts/            compilación, generación y validación
tests/              pruebas técnicas automáticas
docs/               documentación de uso
build/               resultados generados localmente; no se versionan
```

## Comandos de control

```bash
python scripts/compilar_tema.py --check
python scripts/validar_banco_tema_03.py
python scripts/generar_evaluaciones_tema_03.py
python -m unittest discover -s tests -v
python scripts/validar_proyecto.py
```

Para regenerar El Parte y El Atestado tras editar la fuente maestra:

```bash
python scripts/compilar_tema.py --write
```

## Próximo tema

El siguiente tema debe crearse copiando **la estructura**, no el contenido, del Tema 3. No se trasladarán directamente temarios antiguos sin convertirlos al circuito completo VIGOR.

---

© Academia En Vigor · Contenido interno no publicado.
