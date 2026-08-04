
# Exámenes oficiales históricos · Guardia Civil

Banco separado de las preguntas propias de Academia En Vigor. Espejo del banco
de Policía Nacional, con el prefijo `gc` en lugar de `pn`.

## Estado

Andamiaje creado el 05/08/2026. `manifest.json` está vacío (`exams: []`) a la
espera de los JSON de exámenes.

## Convenio de identificadores

| Elemento | Formato | Ejemplo |
|---|---|---|
| Examen | `of-gc-p<año>-<modelo>` | `of-gc-p2025-a` |
| Pregunta | `of-gc-p<año>-<modelo>-q<nnn>` | `of-gc-p2025-a-q001` |
| Hecho atómico | `GC-T<nn>-F<nnn>` | `GC-T04-F001` |
| Pregunta propia | `GC-T<nn>-Q<nnn>` | `GC-T04-Q001` |

Policía Nacional numera por promoción (`p42`); Guardia Civil usa el año de la
convocatoria. Se mantiene la `p` para no tocar los patrones del validador.

## Carpeta por examen

```
C2025-A/
├── metadata.json
└── preguntas.jsonl
```

Cada examen debe quedar registrado en el array `exams` de `manifest.json` con
`id`, `metadata_path`, `questions_path`, `question_count`,
`verification_status`, `proposed_answers`, `official_answers` y
`annulment_flags`.

## Estados

- `quarantine`: sirve para investigación, mapeo temático y revisión interna,
  pero no alimenta «Ha caído».
- `verified`: exige cuestionario identificado, plantilla final oficial y
  respuesta contrastada.

Una pregunta solo puede tener `counts_for_ha_caido: true` cuando esté en estado
`verified` y tenga `official_answer_option_id`.

## Política de fuentes

Ningún PDF, DOCX, escaneo, marca de agua ni retroalimentación de terceros entra
en el repositorio. Los originales viven en archivo privado no versionado.

## Validación

```
python scripts/validar_examenes_oficiales.py .
```

Debe imprimir un bloque `== guardia-civil ==` sin errores.
