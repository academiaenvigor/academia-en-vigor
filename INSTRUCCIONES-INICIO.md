# Instrucciones para crear el repositorio limpio

## 1. Repositorio antiguo

Renombrar el repositorio actual como:

```text
academia-en-vigor-legacy
```

No borrar ni seguir trabajando en él.

## 2. Repositorio nuevo

Crear un repositorio vacío llamado:

```text
academia-en-vigor
```

No añadir README, `.gitignore` ni licencia al crearlo, porque ya se incluyen en este paquete.

## 3. Subida

Descomprimir el ZIP y subir **el contenido interior** de la carpeta, no la carpeta contenedora ni el ZIP.

La raíz del repositorio debe mostrar directamente:

```text
.github/
banco-preguntas/
conocimiento/
docs/
editorial/
evaluaciones/
fuentes/
materiales/
scripts/
temas/
tests/
.gitignore
README.md
temario.json
```

## 4. Primera comprobación

Tras subirlo, GitHub Actions debe ejecutar `Validar contenido`. El resultado esperado es verde.
