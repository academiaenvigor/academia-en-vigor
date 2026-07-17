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

## 6. Materiales de NotebookLM

NotebookLM recibe copias de El Parte, El Atestado y fuentes autorizadas. Sus resultados quedan como `pendiente_revision`. Nunca modifican automáticamente la fuente maestra.

## 7. Control de cambios

Toda revisión debe indicar:

- versión;
- fecha;
- motivo;
- alcance;
- archivos afectados;
- estado de publicación;
- validaciones realizadas.
