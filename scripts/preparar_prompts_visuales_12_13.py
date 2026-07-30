#!/usr/bin/env python3
"""Prepara prompts raster diferenciados para los Temas 12 y 13."""
from __future__ import annotations

import json
from pathlib import Path

from generar_temas_12_13 import T12, T13, visuals_for

ROOT = Path(__file__).resolve().parents[1]

LABELS = {
    "t12-01-mapa-general.webp": ["PROTECCIÓN", "PROCEDIMIENTO", "VULNERABILIDAD", "ACOGIDA", "APATRIDIA", "PROTECCIÓN TEMPORAL"],
    "t12-02-mapa-normativo-2026.webp": ["GINEBRA 1951", "UE 2024", "LEY 12/2009", "PRIMACÍA", "COMPATIBILIDAD"],
    "t12-03-dos-estatutos.webp": ["ASILO", "PERSECUCIÓN", "PROTECCIÓN SUBSIDIARIA", "DAÑO GRAVE", "NO DEVOLUCIÓN"],
    "t12-il-01-red-de-persecucion.webp": [],
    "t12-06-triangulo-danos-graves.webp": ["PENA DE MUERTE", "TORTURA", "VIOLENCIA INDISCRIMINADA"],
    "t12-07-tres-filtros.webp": ["EXCLUSIÓN", "DENEGACIÓN", "NO DEVOLUCIÓN"],
    "t12-il-02-primera-escucha.webp": [],
    "t12-09-balanza-derechos-deberes.webp": ["ABOGADO", "INTÉRPRETE", "INFORMACIÓN", "COOPERACIÓN", "COMPARECENCIA"],
    "t12-10-puente-2025-2026.webp": ["ANTES", "12 JUN 2026", "REGLAMENTO UE", "APLICACIÓN DIRECTA"],
    "t12-11-cuatro-accesos-frontera.webp": ["PUESTO FRONTERIZO", "CRUCE NO AUTORIZADO", "RESCATE", "REUBICACIÓN", "TRIAJE"],
    "t12-12-reloj-con-garantias.webp": ["ASISTENCIA JURÍDICA", "ACNUR", "EXAMEN INICIAL", "RESOLUCIÓN"],
    "t12-il-03-expediente-protegido.webp": [],
    "t12-14-radar-vulnerabilidad.webp": ["DETECCIÓN", "ADAPTACIÓN", "ATENCIÓN ESPECIALIZADA", "SEGUIMIENTO"],
    "t12-il-04-brujula-del-menor.webp": [],
    "t12-16-triangulo-mena.webp": ["PROTECCIÓN DE MENORES", "MINISTERIO FISCAL", "REPRESENTACIÓN"],
    "t12-17-itinerario-acogida.webp": ["VALORACIÓN", "ACOGIDA", "AUTONOMÍA", "INCLUSIÓN"],
    "t12-18-tres-fases-sapi.webp": ["VALORACIÓN INICIAL", "ACOGIDA", "AUTONOMÍA"],
    "t12-il-05-red-de-recursos.webp": [],
    "t12-21-apatridia-no-indocumentacion.webp": ["APÁTRIDA", "NINGÚN ESTADO", "INDOCUMENTADO", "SIN DOCUMENTO"],
    "t12-22-ruta-apatridia.webp": ["SOLICITUD", "OAR", "AUDIENCIA 15 DÍAS", "MINISTRO DEL INTERIOR", "RESOLUCIÓN"],
    "t12-23-doble-via-temporal-asilo.webp": ["AFLUENCIA MASIVA", "PROTECCIÓN TEMPORAL", "SOLICITUD INDIVIDUAL", "ASILO"],
    "t12-il-06-maleta-de-derechos.webp": [],
    "t12-25-mesa-institucional.webp": ["OAR", "CIAR", "MINISTERIO", "ACNUR", "INSTRUIR", "PROPONER", "RESOLVER"],
    "t12-26-tablero-cinco-casillas.webp": ["FIGURA", "LUGAR", "PROCEDIMIENTO", "GARANTÍAS", "APOYO"],
    "t13-01-mapa-general.webp": ["BASES", "COORDINACIÓN", "EMPRESAS", "PERSONAL", "SERVICIOS", "MEDIDAS"],
    "t13-02-modelo-complementario.webp": ["SEGURIDAD PÚBLICA", "CONTROL", "SEGURIDAD PRIVADA", "COMPLEMENTARIA", "SUBORDINADA"],
    "t13-03-cuatro-conceptos.webp": ["ACTIVIDAD", "SERVICIO", "FUNCIÓN", "MEDIDA"],
    "t13-04-ecosistema-sujetos.webp": ["EMPRESA", "PERSONAL", "DESPACHO", "USUARIO", "ESTABLECIMIENTO"],
    "t13-05-tres-fines.webp": ["PROTEGER", "CONTRIBUIR", "INTEGRAR"],
    "t13-il-01-relevo-coordinado.webp": [],
    "t13-07-semáforo-limites.webp": ["PERMITIDO", "CONDICIONADO", "PROHIBIDO", "INTIMIDAD", "RESERVA"],
    "t13-08-mapa-competencias.webp": ["MINISTERIO", "POLICÍA", "GUARDIA CIVIL", "COMUNIDAD AUTÓNOMA"],
    "t13-10-centro-coordinacion.webp": ["INFORMACIÓN", "COORDINACIÓN", "INSTRUCCIONES", "SEGURIDAD PÚBLICA"],
    "t13-11-tres-zonas-actividad.webp": ["RESERVADAS", "COMPATIBLES", "EXCLUIDAS"],
    "t13-il-02-sala-operaciones.webp": [],
    "t13-14-frontera-investigacion.webp": ["EMPRESA DE SEGURIDAD", "VIGILANCIA", "DESPACHO DE DETECTIVES", "INVESTIGACIÓN"],
    "t13-15-arbol-profesional.webp": ["VIGILANTE", "EXPLOSIVOS", "ESCOLTA", "GUARDA RURAL", "JEFE", "DIRECTOR", "DETECTIVE"],
    "t13-il-03-escudo-proporcional.webp": [],
    "t13-18-ciclo-vigilante.webp": ["PREVENIR", "CONTROLAR", "INTERVENIR", "ENTREGAR A POLICÍA"],
    "t13-il-04-burbuja-proteccion.webp": [],
    "t13-21-doble-puesto.webp": ["JEFE DE SEGURIDAD", "EMPRESA", "DIRECTOR DE SEGURIDAD", "USUARIO"],
    "t13-il-05-investigacion-legitima.webp": [],
    "t13-il-06-perimetro-servicio.webp": [],
    "t13-25-cono-vision.webp": ["FINALIDAD", "CAMPO DE VISIÓN", "ACCESO", "CONSERVACIÓN", "PRIVACIDAD"],
    "t13-il-07-informe-bajo-llave.webp": [],
    "t13-29-capas-medidas.webp": ["FÍSICAS", "ELECTRÓNICAS", "INFORMÁTICAS", "ORGANIZATIVAS", "PERSONALES"],
    "t13-il-08-inspeccion-en-capas.webp": [],
    "t13-32-tablero-ocho-casillas.webp": ["SUJETO", "ACTIVIDAD", "EMPRESA", "PERSONAL", "FUNCIÓN", "SERVICIO", "MEDIDA", "CONTROL"],
}


def prompt(topic: int, filename: str, kind: str, description: str, family: str) -> str:
    labels = LABELS[filename]
    title = description.upper()
    if kind == "infografia":
        exact = ", ".join(f'"{x}"' for x in labels)
        return f"""Use case: scientific-educational
Asset type: infografía horizontal 16:9 para opositores adultos de Policía Nacional, Tema {topic}
Primary request: {description}. Debe enseñar una relación jurídica concreta mediante una composición de familia «{family}», con jerarquía, conexiones, flechas, iconos, personajes u objetos pertinentes; información visual abundante pero ordenada, sin cajas vacías.
Style/medium: ilustración editorial dibujada a mano, vectorial limpia con volumen suave, aspecto de manual premium, no aspecto corporativo genérico.
Composition/framing: lienzo panorámico completo, título breve arriba, recorrido visual claro de izquierda a derecha o de centro a ramas según la familia.
Color palette: azul marino, azul medio, verde, ámbar y fondo blanco cálido; alto contraste.
Text (verbatim): usar únicamente estas etiquetas exactas en español: {exact}. No añadir frases ni texto inventado.
Constraints: tipografía española perfectamente legible; cada etiqueta unida claramente a su icono o tramo; contenido visual rico y específico; bordes nítidos; sin logotipos; sin escudos ni insignias oficiales; sin marcas de agua.
Avoid: plantilla repetitiva de tarjetas, rectángulos vacíos, párrafos largos, fotorealismo, decoración sin función, texto ilegible."""
    return f"""Use case: illustration-story
Asset type: ilustración didáctica horizontal 16:9 para opositores adultos de Policía Nacional, Tema {topic}
Primary request: {description}. Convertir el concepto en una escena o metáfora visual clara de familia «{family}».
Style/medium: dibujo editorial narrativo, personajes adultos expresivos y respetuosos, línea limpia, color plano con volumen suave, calidad de libro ilustrado contemporáneo.
Composition/framing: escena panorámica con una acción principal, entorno significativo y lectura inmediata; sin diagramas, tablas ni paneles de texto.
Color palette: azul marino, azul medio, verde, ámbar y fondo luminoso.
Text: no incluir palabras, títulos, rótulos ni números.
Constraints: la escena debe explicar el concepto por imagen; sin logotipos; sin escudos ni insignias oficiales; uniforme genérico cuando aparezca personal; sin marcas de agua.
Avoid: infografía de cajas, tarjetas repetitivas, grandes superficies vacías, fotorealismo, estética infantil, texto accidental."""


def main() -> int:
    rows = []
    for cfg in (T12, T13):
        for filename, kind, _blocks, description, family in visuals_for(cfg):
            rows.append({
                "tema": cfg["number"], "filename": filename,
                "png_filename": filename.removesuffix(".webp") + ".png",
                "kind": kind, "description": description, "family": family,
                "labels": LABELS[filename],
                "prompt": prompt(cfg["number"], filename, kind, description, family),
            })
    out = ROOT / "build/visuales/temas-12-13/prompts.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {len(rows)} prompts en {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
