
# Flujo para crear un tema

## 1. Crear la estructura

```bash
python scripts/crear_tema.py --oposicion policia-nacional --tema 4 --titulo "Título oficial" --slug titulo-oficial
```

## 2. Registrar fuentes

Añadir únicamente fuentes oficiales a `fuentes/catalogo.json` y utilizar sus IDs en el `master.md`.

## 3. Construir conocimiento

- dividir el tema en bloques semánticos;
- redactar El Parte y El Atestado dentro del `master.md`;
- crear hechos atómicos estables;
- actualizar `cobertura.json` y el manifiesto.

## 4. Compilar

```bash
python scripts/compilar_tema.py --oposicion policia-nacional --tema 4 --write
```

## 5. Entrenar

Crear preguntas propias resolubles con El Atestado, actualizar el manifiesto del banco y definir `plan.json`.

## 6. Mapear exámenes históricos

Añadir al `indice-oficiales.json` únicamente los IDs relacionados. El mapeo no activa «Ha caído» mientras las preguntas sigan en cuarentena.

## 7. Producir materiales

Crear briefing, guiones e infografías desde la versión aprobada del tema. Registrar cada recurso en el manifiesto correspondiente.

## 8. Validar y revisar

```bash
python scripts/compilar_tema.py --all --check
python scripts/validar_bancos.py --all
python scripts/validar_proyecto.py
python -m unittest discover -s tests -v
```

Solo después se cambia el estado editorial.
