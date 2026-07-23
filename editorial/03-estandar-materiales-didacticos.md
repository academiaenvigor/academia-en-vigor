# Estándar de materiales didácticos · Método VIGOR

## 1. Qué es un material didáctico

Todo recurso que acompaña al temario sin sustituirlo: audio, vídeo, presentación e infografía.
Se produce **siempre a partir de El Atestado aprobado**, nunca de una fuente externa.

## 2. Los cuatro tipos y sus dos ámbitos

| Tipo | Categoría | Icono |
|---|---|---|
| Audio | `audios` | 🎧 |
| Vídeo | `videos` | 🎬 |
| Presentación gráfica | `presentaciones` | 📊 |
| Infografía / esquema | `infografias` | 🖼 |

Cada tipo existe en dos ámbitos (`scope`):

- **`tema`** — un material general que cubre el tema entero. Es el que entra en el **plan mensual**.
- **`bloque`** — un material por cada punto del tema, anclado a su bloque semántico. Es el valor diferencial de la **Completa**.

## 3. Doble acceso desde la plataforma

Un mismo manifest alimenta dos vistas:

1. **En línea con la lectura.** El compilador inyecta al final de cada bloque una tira con el material de ese punto. El alumno nunca descubre un esquema *después* de haberse estudiado el tema.
2. **Sección Material.** Vista independiente que agrupa por tipo todos los recursos del tema.

La infografía no aparece en la tira: ya se muestra incrustada en el propio texto.

## 4. Almacenamiento y migración

Los audios y vídeos **nunca se guardan en el repositorio** (lo impide `validar_derechos.py`).

- **Hoy:** Google Drive de la cuenta de la academia, enlace privado provisional.
- **Mañana:** servidor propio con URL firmada y validada por usuario, para que un enlace compartido no dé acceso.

La migración es una operación de una sola línea: cada recurso se identifica por su **`asset_key`** (`pn/tema-03/b05/audio`), no por su URL. Al cambiar de proveedor se actualiza `storage_config` en cada manifest y el resolvedor de la plataforma; **el contenido de los temas no se toca**.

## 5. Estados y publicación

`planned` → `in_production` → `pending_review` → `approved_internal` → `published` → `retired`

- Un recurso `planned` o `in_production` **no necesita URL todavía**.
- Solo se muestra como enlace real cuando está `approved_internal` o `published` **y** tiene URL.
- Mientras `display_policy.show_planned_in_temas` sea `true`, los recursos no producidos aparecen como *(en producción)*. **Al lanzar la plataforma debe ponerse en `false`.**

## 6. Reglas de producción

1. Todo recurso registra la **versión del temario** con la que se generó (`source_content_version`). Si el tema cambia de versión, el material queda desactualizado y debe revisarse.
2. Todo recurso declara su **autoría o autorización** (`ownership`). Antes de usar comercialmente audio o vídeo generados con una herramienta externa, hay que verificar sus condiciones de uso comercial.
3. No se incorporan preguntas oficiales, años de examen ni afirmaciones normativas que no estén en el temario aprobado.
4. Ningún material se publica sin contraste con El Atestado.
