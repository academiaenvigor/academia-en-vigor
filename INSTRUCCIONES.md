# Corrección del Tema 7 en el explorador

## Qué corrige

El Tema 7 ya tenía sus versiones Parte y Atestado en el repositorio, pero no aparecía porque faltaba su entrada en `temario.json`. `explorador.html` carga ese archivo para construir el menú, por lo que no es necesario modificar el HTML.

Este paquete:

1. registra el Tema 7 en `temario.json`;
2. alinea su manifiesto editorial con el estado interno del repositorio;
3. crea los manifiestos auxiliares que espera el explorador;
4. deja el banco de preguntas vacío y las evaluaciones bloqueadas hasta que se generen;
5. registra ocho ilustraciones como pendientes, sin incluir las imágenes rechazadas;
6. añade un comprobador automático de rutas.

## Cómo instalarlo

1. Descomprime el ZIP.
2. Copia **el contenido de esta carpeta** en la raíz de `academia-en-vigor`.
3. Conserva exactamente la estructura de carpetas y acepta reemplazar los dos archivos existentes:
   - `temario.json`
   - `conocimiento/policia-nacional/tema-07/manifest.json`
4. Sube los cambios a la rama que publica la academia, normalmente `main`.
5. Espera a que termine GitHub Pages y fuerza la recarga del navegador:
   - macOS: `Cmd + Shift + R`
   - Windows/Linux: `Ctrl + F5`

## Comprobación local

Desde la raíz del repositorio:

```bash
python3 scripts/verificar_integracion_tema_07.py
```

El resultado correcto es:

```text
OK: Tema 7 registrado y todas las rutas del explorador son válidas.
```

## Importante

- No reemplaces `explorador.html`: no es el origen del fallo.
- No subas todavía archivos WebP del Tema 7. El manifiesto visual los deja en estado `planned` hasta que se aprueben las nuevas ilustraciones.
- El botón de preguntas mostrará cero preguntas hasta que se genere el banco definitivo.
