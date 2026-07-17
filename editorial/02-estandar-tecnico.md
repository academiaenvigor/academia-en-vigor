# Estándar técnico · Método VIGOR

## 1. Rutas

```text
conocimiento/<oposicion>/tema-NN/
temas/<oposicion>/parte/
temas/<oposicion>/atestado/
banco-preguntas/<oposicion>/tema-NN/
evaluaciones/<oposicion>/tema-NN/
materiales/<oposicion>/tema-NN/
```

Los números de tema usan dos cifras: `tema-03`.

## 2. Archivos canónicos

- `master.md`: fuente editorial.
- `manifest.json`: estados, versión y rutas.
- `cobertura.json`: hechos atómicos.
- `preguntas.jsonl`: banco, una pregunta por línea.
- `plan.json`: reglas reproducibles para evaluaciones.

## 3. Identificadores

- Hecho: `PN-T03-F001`.
- Pregunta: `PN-T03-Q001`.
- Test: `PN-T03-B01-A`, `PN-T03-P1-A` o `PN-T03-FINAL-25-A`.

Los IDs publicados no se reutilizan para otro contenido.

## 4. Versionado

Se utiliza versionado semántico:

- parche: corrección sin cambiar el alcance;
- menor: ampliación compatible;
- mayor: cambio estructural incompatible.

La versión del banco debe declarar la versión de conocimiento que utiliza.

## 5. Resultados generados

Los tests estáticos se escriben en `build/` y no se versionan. Se conservan en el repositorio el banco, el plan y el generador.

No se suben:

- `__pycache__/`;
- archivos `.pyc`;
- salidas temporales;
- audios o vídeos pesados;
- resultados que puedan regenerarse exactamente.

## 6. Validación mínima

Antes de aceptar un cambio deben pasar:

```bash
python scripts/compilar_tema.py --check
python scripts/validar_banco_tema_03.py
python -m unittest discover -s tests -v
python scripts/validar_proyecto.py
```

## 7. Codificación

Todos los archivos de texto usan UTF-8, finales de línea Unix y nombres sin espacios salvo causa justificada.
