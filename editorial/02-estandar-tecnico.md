
# Estándar técnico · Método VIGOR

## 1. Rutas canónicas

```text
conocimiento/<oposicion>/tema-NN/
temas/<oposicion>/parte/
temas/<oposicion>/atestado/
banco-preguntas/<oposicion>/tema-NN/
banco-preguntas/<oposicion>/oficiales/
evaluaciones/<oposicion>/tema-NN/
assets/<oposicion>/tema-NN/
materiales-didacticos/<oposicion>/tema-NN/
```

Los números de tema usan dos cifras: `tema-03`.

## 2. Archivos canónicos

- `master.md`: fuente editorial.
- `manifest.json`: estado, versión y rutas.
- `cobertura.json`: hechos atómicos.
- `preguntas.jsonl`: banco propio, una pregunta por línea.
- `indice-oficiales.json`: referencias históricas del tema.
- `plan.json`: reglas reproducibles para evaluaciones.
- `assets/.../manifest.json`: imágenes insertadas.
- `materiales-didacticos/.../manifest.json`: recursos independientes.
- `banco-preguntas/.../oficiales/manifest.json`: inventario histórico.

## 3. Identificadores

- Hecho: `PN-T03-F001`.
- Pregunta propia: `PN-T03-Q001`.
- Pregunta histórica: `of-pn-p39-a-q001`.
- Test: `PN-T03-B01-A`, `PN-T03-P1-A` o `PN-T03-FINAL-25-A`.
- Material: `PN-T03-AUD-001`, `PN-T03-VID-001`, `PN-T03-INF-001`.

Los IDs publicados no se reutilizan.

## 4. Versionado

Se utiliza versionado semántico. La versión del banco, evaluaciones, assets y materiales declara la versión de conocimiento de la que derivan.

## 5. Archivos no versionados

No se suben:

- `build/`, cachés y temporales;
- PDF, DOC, DOCX, ODT, PPTX o KEY;
- MP3, WAV, M4A, MP4, MOV, AVI o MKV;
- originales, escaneos o fuentes privadas;
- archivos con marcas de agua o maquetación de terceros;
- secretos, claves y datos personales.

PNG, JPG, WEBP y SVG solo se admiten como assets propios o autorizados y deben figurar en un manifiesto.

## 6. Validación

```bash
python scripts/compilar_tema.py --all --check
python scripts/validar_bancos.py --all
python scripts/validar_proyecto.py
python -m unittest discover -s tests -v
```

`validar_proyecto.py` ejecuta también los controles de exámenes oficiales, materiales y derechos.

## 7. Codificación

Todos los textos usan UTF-8, finales de línea Unix y nombres sin espacios salvo causa justificada.
