# Instalación de un paquete de cambios

Los paquetes de Academia En Vigor conservan la estructura del repositorio.

1. Haz una copia de seguridad o crea una rama.
2. Copia el contenido de `SUBIR_AL_REPOSITORIO/` en la raíz del repositorio,
   conservando carpetas y reemplazando los archivos indicados.
3. Revisa `BORRAR_DEL_REPOSITORIO.txt` y elimina únicamente esas rutas.
4. Ejecuta:

```bash
python3 scripts/compilar_tema.py --all --check
python3 scripts/validar_proyecto.py
python3 -m unittest discover -s tests -v
```

5. Si las comprobaciones terminan correctamente, confirma y publica los cambios
   en la rama correspondiente.

No copies al repositorio la carpeta contenedora del ZIP ni archivos de fuentes
privadas, DOCX de trabajo o recursos multimedia pesados no inventariados.
