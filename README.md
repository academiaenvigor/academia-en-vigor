# Academia En Vigor

Repositorio editorial del temario de Policía Nacional. Cada tema se mantiene bajo
un contrato único y reproducible:

- `conocimiento/.../master.md` es la fuente canónica;
- El Parte y El Atestado se compilan en `temas/`;
- los hechos atómicos y su cobertura viven en `conocimiento/`;
- las preguntas, evaluaciones, recursos visuales y materiales didácticos se
  inventarían en sus carpetas específicas;
- `temario.json` actúa como índice global.

## Flujo de trabajo

```bash
python3 scripts/compilar_tema.py --all --check
python3 scripts/validar_proyecto.py
python3 -m unittest discover -s tests -v
```

Para recompilar un tema concreto:

```bash
python3 scripts/compilar_tema.py --oposicion policia-nacional --tema 7 --write
python3 scripts/validar_temas.py --oposicion policia-nacional --tema 7
```

Las correcciones sustantivas se hacen en el Máster; El Parte y El Atestado son
salidas generadas. Los binarios pesados y los documentos de terceros no se
almacenan en el repositorio.

## Contrato editorial

El estándar vigente está documentado en `editorial/04-contrato-unico-de-tema.md`.
Las fuentes normativas deben figurar en `fuentes/catalogo.json`, los recursos
visuales integrados deben ser WEBP inventariados bajo `assets/`, y ninguna
aparición histórica se presenta como plantilla oficial sin trazabilidad.
