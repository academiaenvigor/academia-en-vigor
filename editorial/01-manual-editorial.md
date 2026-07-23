# Manual editorial · Método VIGOR

## 1. Circuito de un tema

1. Confirmar el epígrafe oficial.
2. Registrar las fuentes en `fuentes/catalogo.json`.
3. Dividir el contenido en bloques semánticos.
4. Redactar en `master.md` la representación de El Parte y El Atestado.
5. Identificar hechos jurídicos atómicos con ID estable.
6. Compilar las dos vistas.
7. Construir `cobertura.json`.
8. Crear y validar el banco.
9. Definir el plan de evaluaciones.
10. Registrar la revisión y mantener `not_published` hasta decisión expresa.

## 2. Las seis capas

Todo tema conserva exactamente estas capas:

1. Mapa del tema.
2. Contenido.
3. Hablemos claro.
4. En la calle.
5. Lo que cae.
6. Ha caído.

“Ha caído” solo incluye referencias oficiales verificadas. En ausencia de ellas, debe declararse expresamente.

## 2.1. Bloques semánticos y código de color

Los avisos pedagógicos se escriben con contenedores VIGOR. La marca de apertura y la de cierre deben comenzar en la primera columna, no pueden anidarse y deben conservar exactamente estos identificadores:

```markdown
:::hablemos-claro
Explicación directa y accesible.
:::

:::en-la-calle
Aplicación práctica o policial.
:::

:::lo-que-cae
Dato prioritario para examen o repaso.
:::

:::perla-vigor
Idea breve de alto valor memorístico.
:::

:::trampa
Error frecuente, excepción o concepto que no debe confundirse.
:::

:::ha-caido
Referencia oficial verificada conforme al protocolo histórico.
:::

:::visual
**Referencia visual prevista:** `tNN-XX-nombre.webp` · descripción del recurso.
:::
```

La paleta es fija para toda la academia:

| Bloque | Color editorial | Finalidad |
|---|---|---|
| `hablemos-claro` | Azul | Comprender una explicación difícil |
| `en-la-calle` | Verde | Ver la aplicación práctica |
| `lo-que-cae` | Amarillo/ámbar | Repasar lo prioritario |
| `perla-vigor` | Morado | Retener una idea de alto valor |
| `trampa` | Rojo | Evitar errores y confusiones |
| `ha-caido` | Naranja | Localizar antecedentes oficiales verificados |
| `visual` | Blanco/gris azulado | Identificar ilustraciones e infografías |

El color nunca sustituye al rótulo, al icono ni al texto. La presentación debe seguir siendo comprensible para una persona que no distinga los colores. El explorador puede filtrar estos bloques, pero los documentos Markdown siguen siendo legibles fuera de la web.

## 3. El Parte

- Es la versión esencial.
- Debe servir para estudiar y repasar.
- No puede eliminar un concepto examinable por ser difícil o extenso.
- Prioriza relaciones, listas, plazos, mayorías, competencias y diferencias.

## 4. El Atestado

- Es la versión desarrollada.
- Contiene todos los hechos que alimentan el banco.
- Debe explicar trampas y conceptos próximos.
- No repite una fórmula genérica para aparentar profundidad.
- Empieza cada bloque explicando la lógica general antes del detalle normativo.
- Integra los hechos atómicos en párrafos breves agrupados por artículos o ideas.
- Evita cadenas de más de cuatro o cinco viñetas consecutivas.
- Incluye ejemplos mentales, comparaciones y una estrategia de estudio cuando aporten comprensión.
- Conserva los identificadores `FACT` en la fuente para mantener la trazabilidad, aunque no sean visibles para el alumno.
- Utiliza listas solo cuando la naturaleza del contenido exige enumeración o comparación, no como formato dominante.

## 5. Preguntas

Cada pregunta debe:

- tener tres opciones distintas;
- tener una única respuesta correcta;
- poder resolverse con El Atestado;
- incluir explicación;
- vincularse a un `fact_id`;
- indicar artículo o referencia cuando proceda;
- declararse `propio` salvo trazabilidad oficial completa.

La cobertura del 100 % significa que cada hecho inventariado tiene pregunta. No significa que se hayan agotado todas las redacciones posibles.

## 6. Imágenes y materiales didácticos

Las imágenes integradas en El Parte o El Atestado se guardan en `assets/<oposicion>/tema-NN/` y se registran en su manifest.

El formato de publicación ordinario es **WebP**. Los PNG originales se conservan fuera del repositorio como archivos maestros; el repositorio contiene únicamente las copias WebP optimizadas. Las excepciones SVG, PNG o JPG deben estar justificadas en el manifiesto.

Cada copia WebP debe conservar la legibilidad del texto en móvil, mantener la proporción del original y quedar por debajo de 1 MB. La conversión no autoriza a reducir la calidad hasta degradar cifras, tildes, artículos o etiquetas.

Se distinguen dos funciones:

- **Infografía técnica (`tNN-XX-...`)**: organiza datos, plazos, requisitos, comparaciones o árboles de decisión. Puede contener texto jurídico revisado.
- **Ilustración simple (`tNN-il-XX-...`)**: explica una sola idea mediante una escena o metáfora visual, con texto mínimo o inexistente. No sustituye el contenido ni añade reglas jurídicas.

El Atestado puede integrar ambas cuando cumplan funciones distintas. El Parte solo reutiliza las ilustraciones imprescindibles para recordar conceptos de alto rendimiento; no debe convertirse en una galería ni duplicar el peso visual del Atestado.

Toda ilustración simple debe tener formato horizontal 16:9, márgenes seguros, estilo editorial adulto, lectura clara en móvil y ausencia de emblemas oficiales, marcas de agua o texto jurídico generado dentro de la imagen.

Los productos independientes se guardan o referencian desde `materiales-didacticos/<oposicion>/tema-NN/`, separados en:

- infografías;
- presentaciones;
- audios;
- vídeos.

La herramienta de origen puede ser ChatGPT, NotebookLM, Gemini, Canva, una persona u otra herramienta. Todo producto debe registrar la versión del temario utilizada y quedar como `pendiente_revision` hasta su comprobación.

Los materiales derivados nunca modifican automáticamente la fuente maestra.

## 7. Control de cambios

Toda revisión debe indicar:

- versión;
- fecha;
- motivo;
- alcance;
- archivos afectados;
- estado de publicación;
- validaciones realizadas.

## 8. Exámenes oficiales históricos

- Se almacenan en `banco-preguntas/<oposicion>/oficiales/` y nunca se mezclan con el banco propio.
- El repositorio solo conserva enunciado, opciones y metadatos normalizados.
- No se incorporan PDF, DOCX, capturas, marcas de agua ni explicaciones de terceros.
- Una respuesta disponible puede registrarse como `proposed_answer_option_id`, pero no como oficial definitiva.
- «Ha caído» exige `status: verified`, `official_answer_option_id` y constancia de plantilla final oficial.
- Cada tema usa `indice-oficiales.json` para referenciar IDs; no duplica los enunciados.

## 9. Materiales didácticos

Todo recurso independiente debe registrar:

- tema y versión fuente;
- categoría;
- herramienta o autor de producción;
- autoría o permiso;
- estado de revisión;
- ubicación externa o ruta local permitida.

Los audios, vídeos y presentaciones pesadas se alojan externamente. El repositorio conserva el guion, los metadatos y el enlace autorizado.

## 10. Cierre de un tema

Un tema solo pasa a `approved_internal` cuando supera revisión normativa, pedagógica, editorial, de cobertura, de materiales y de derechos. La publicación para alumnos es una decisión posterior y separada.
