# El Parte y El Atestado

## El Parte

Es el Temario Esencial. Reúne todo lo que debe estar disponible para una primera vuelta, memorización y repaso rápido. Es más breve que El Atestado, pero no puede ser conceptualmente incompleto.

## El Atestado

Es el Temario Desarrollado. Explica el contenido con mayor profundidad, separa requisitos y efectos, incluye trampas y contiene todos los hechos atómicos que alimentan el banco de preguntas.

## Relación entre ambos

Ambos se generan desde `master.md`. No se editan como fuentes independientes. Cuando se detecta una mejora:

1. se modifica `master.md`;
2. se ejecuta `python scripts/compilar_tema.py --write`;
3. se revisa la cobertura;
4. se actualiza el banco si cambia algún hecho.
