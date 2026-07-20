
# Academia En Vigor

**El temario que nunca duerme.**

Repositorio editorial privado de Academia En Vigor para la preparación de Policía Nacional. El Tema 3 es el tema piloto cerrado internamente y sirve como patrón para construir los siguientes temas con el Método VIGOR.

## Regla principal

Solo entra un tema que tenga:

1. fuente maestra en `conocimiento/`;
2. El Parte y El Atestado compilados desde esa fuente;
3. cobertura de hechos atómicos;
4. banco propio validado;
5. plan de evaluaciones reproducible;
6. fuentes oficiales y estado editorial registrados;
7. imágenes y materiales didácticos vinculados a una versión concreta;
8. control de derechos y ausencia de archivos de terceros.

## Estado

| Elemento | Estado |
|---|---|
| Tema 3 · fuente maestra | Cerrado internamente · v0.3.0 |
| Hechos atómicos del Tema 3 | 470 |
| Banco propio del Tema 3 | 738 preguntas · cobertura 470/470 |
| Evaluaciones del Tema 3 | 61 tests reproducibles |
| Recursos visuales integrados | 28 · 17 infografías y 11 ilustraciones |
| Exámenes históricos normalizados | 10 exámenes · 1000 preguntas |
| Respuestas históricas propuestas | 662 · no equivalen a plantilla oficial final |
| Preguntas oficiales verificadas | 0 |
| Referencias históricas mapeadas al Tema 3 | 30 |
| «Ha caído» activo | 0 hasta verificación definitiva |
| Publicación para alumnos | No publicada |

## Arquitectura

```text
editorial/               normas del Método VIGOR
fuentes/                 catálogo de fuentes oficiales, nunca originales de terceros
conocimiento/            fuente maestra, cobertura, manifiestos y revisiones
temas/                   El Parte y El Atestado derivados
banco-preguntas/         preguntas propias y exámenes oficiales separados
evaluaciones/            planes reproducibles de tests
assets/                  imágenes insertadas dentro del temario
materiales-didacticos/   metadatos de infografías, presentaciones, audios y vídeos
plantillas/              patrón para iniciar nuevos temas
scripts/                 creación, compilación y validación
tests/                   pruebas automáticas
docs/                    procedimientos editoriales y técnicos
build/                   salidas regenerables; no se versionan
```

### Bancos separados

```text
banco-preguntas/policia-nacional/tema-NN/preguntas.jsonl
```

contiene preguntas creadas por Academia En Vigor.

```text
banco-preguntas/policia-nacional/oficiales/
```

contiene transcripciones históricas normalizadas, sin PDF, DOCX, marcas de agua ni comentarios de terceros. Cada tema mantiene un `indice-oficiales.json` que referencia los IDs históricos sin duplicar los enunciados.

## Crear el siguiente tema

```bash
python scripts/crear_tema.py \
  --oposicion policia-nacional \
  --tema 4 \
  --titulo "Título oficial del Tema 4" \
  --slug titulo-oficial-tema-04
```

El script crea la fuente maestra, El Parte, El Atestado, banco, cobertura, evaluaciones, assets y estructura de materiales didácticos, y registra el tema en `temario.json`.

## Comandos de control

```bash
python scripts/compilar_tema.py --all --check
python scripts/validar_bancos.py --all
python scripts/validar_proyecto.py
python -m unittest discover -s tests -v
```

## Seguridad editorial

Este repositorio debe mantenerse **privado**. Los audios, vídeos, presentaciones y archivos pesados se alojan fuera del repositorio y se registran mediante su manifiesto. No se suben documentos de terceros ni originales utilizados para comprobación.

---

© Academia En Vigor · Contenido propietario e interno no publicado.
