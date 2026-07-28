# Academia En Vigor · Tema 7

Paquete editorial del Tema 7 de Policía Nacional, Escala Básica:

> El Ministerio del Interior: estructura orgánica básica. La Secretaría de Estado de Seguridad: estructura y funciones.

## Contenido

- `conocimiento/policia-nacional/tema-07/manifest.json`: identidad, fuentes, conceptos, revisiones y salidas.
- `conocimiento/policia-nacional/tema-07/master.md`: fuente canónica con bloques VIGOR.
- `temas/policia-nacional/parte/...md`: Temario Esencial — El Parte.
- `temas/policia-nacional/atestado/...md`: Temario Completo — El Atestado.
- `scripts/compilar_tema_07.py`: recompila ambas vistas desde el maestro.
- `word/`: copias de lectura en DOCX.

## Estado

- Versión: `1.0.0`
- Corte normativo: `28/07/2026`
- Programa: convocatoria de Escala Básica publicada en el BOE el 14/07/2026.
- Reforma crítica incorporada: Real Decreto 328/2026, de 22 de abril.
- Redacción: propia y construida sobre fuentes oficiales; el documento de muestra se utilizó únicamente para contrastar cobertura.

## Compilación

Desde la raíz del paquete:

```bash
python scripts/compilar_tema_07.py
```

Los archivos de `temas/` son salidas generadas. Las correcciones sustantivas deben realizarse en `master.md`.
