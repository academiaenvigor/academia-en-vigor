# Preparar la segunda oposición: Guardia Civil

## 1. Lo que ya funciona sin tocar nada

La infraestructura nació multi-oposición. Estos scripts ya recorren
`temario.json` entero y detectarán Guardia Civil sola:

- `compilar_tema.py --all` (usa `topics_from_index()`)
- `sincronizar_temario.py`
- `validar_proyecto.py`, `validar_temas.py`, `validar_activos_visuales.py`
- `validar_bancos.py --all`
- `crear_tema.py --oposicion guardia-civil` (ya conoce el prefijo **GC**)
- `integrar_visuales.py --all` (nuevo)

`validar_examenes_oficiales.py` era el único bloqueo real: tenía clavados
`of-pn-` y la ruta de Policía Nacional. Ya corregido: detecta cualquier
`banco-preguntas/*/oficiales/manifest.json` y aplica el prefijo que toque
(`of-gc-...`, `GC-Txx-Fxxx`).

## 2. Dar de alta la oposición en `temario.json`

Añade la clave hermana dentro de `oppositions`:

```json
"guardia-civil": {
  "display_name": "Guardia Civil · Escala de Cabos y Guardias",
  "topics": []
}
```

Y en `official_exam_banks`, cuando tengas el banco:

```json
"guardia-civil": {
  "manifest": "banco-preguntas/guardia-civil/oficiales/manifest.json",
  "exams": 0, "questions": 0, "proposed_answers": 0,
  "verified_questions": 0, "active_ha_caido": 0
}
```

## 3. Convenio de identificadores

| Elemento | Policía Nacional | Guardia Civil |
|---|---|---|
| Prefijo | `PN` | `GC` |
| Pregunta propia | `PN-T04-Q001` | `GC-T04-Q001` |
| Hecho atómico | `PN-T04-F001` | `GC-T04-F001` |
| Examen oficial | `of-pn-p42-a` | `of-gc-2025-a` |
| Pregunta oficial | `of-pn-p42-a-q001` | `of-gc-2025-a-q001` |
| Imagen | `t04-01-...webp` | `t04-01-...webp` |

Ojo con el identificador de examen: PN usa **promoción** (`p42`) porque las
convocatorias van numeradas por promoción. En Guardia Civil lo natural es el
**año** de convocatoria. El validador acepta `of-gc-p<algo>-<modelo>`, así que
si prefieres año usa `of-gc-p2025-a` y mantienes el patrón sin tocar código.

## 4. Estructura de un examen oficial (replica esta)

```
banco-preguntas/guardia-civil/oficiales/
├── manifest.json              ← índice de todos los exámenes
├── schema-pregunta-oficial.json
├── retroalimentacion.json
├── revisar-respuestas.json
├── README.md
└── C2025-A/
    ├── metadata.json
    └── preguntas.jsonl
```

`manifest.json` mínimo:

```json
{
  "schema_version": "1.0.0",
  "bank_id": "of-gc-2020-2025",
  "profile_id": "gc",
  "opposition": "guardia-civil",
  "title": "Banco histórico normalizado de exámenes oficiales · Guardia Civil",
  "generated_at": "2026-08-05",
  "repository_visibility_required": "private",
  "exam_count": 0, "question_count": 0,
  "canonical_id_pattern": "of-gc-p<year>-<model>-q<number>",
  "exams": []
}
```

Cada entrada de `exams` necesita: `id`, `metadata_path`, `questions_path`,
`question_count`, `verification_status`, `proposed_answers`,
`official_answers`, `annulment_flags`.

Cada pregunta del `.jsonl` replica el esquema de PN: `id`, `version`,
`profile_id`, `exam_id`, `exam{}`, `origin{}`, `prompt`, `options[]` con
`id`/`source_label`/`text`, `proposed_answer_option_id`, etc. Cópialo de
`schema-pregunta-oficial.json`.

## 5. Orden de trabajo recomendado

1. Crear la clave en `temario.json` y las carpetas del banco oficial.
2. Volcar los JSON de exámenes que estás generando.
3. `python scripts/validar_examenes_oficiales.py .` → debe imprimir un bloque
   `== guardia-civil ==` limpio antes de seguir.
4. Primer tema: `python scripts/crear_tema.py --oposicion guardia-civil --tema 1 --titulo "..." --slug "..."`
5. Redactar `master.md`, luego `compilar_tema.py --all --write`.
6. Cerrar con la rutina de siempre.

Consejo: valida el banco oficial **antes** de escribir ningún tema. Renombrar
1.000 identificadores después es mucho más caro que decidir el convenio ahora.

## 6. Rutina de cierre (memorízala)

```
python scripts/integrar_visuales.py --all
python scripts/sincronizar_temario.py --write
python scripts/compilar_tema.py --all --write
python scripts/validar_proyecto.py
```

## 7. Pendientes conocidos

- `explorador.html` línea 77: `const OP='policia-nacional';` — necesitará un
  selector de oposición cuando Guardia Civil tenga temas.
- Los 18 tests de `tests/` están escritos contra temas concretos de PN. No
  estorban, pero Guardia Civil arrancará sin red de seguridad propia.
- Siguen sin borrar los 12 scripts de un solo uso de `scripts/`.
- El banco oficial de GC está creado y vacío; `topics` de la oposición también.
