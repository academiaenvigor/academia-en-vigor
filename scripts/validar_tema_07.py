#!/usr/bin/env python3
"""Validaciones editoriales y de sincronización para el Tema 7."""

from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "conocimiento/policia-nacional/tema-07/manifest.json"
PARTE = ROOT / "temas/policia-nacional/parte/tema-07-ministerio-interior-secretaria-estado-seguridad.md"
ATESTADO = ROOT / "temas/policia-nacional/atestado/tema-07-ministerio-interior-secretaria-estado-seguridad.md"
COVERAGE = ROOT / "conocimiento/policia-nacional/tema-07/cobertura.json"
BANK = ROOT / "banco-preguntas/policia-nacional/tema-07/preguntas.jsonl"
BANK_MANIFEST = ROOT / "banco-preguntas/policia-nacional/tema-07/manifest.json"
EVALUATION_PLAN = ROOT / "evaluaciones/policia-nacional/tema-07/plan.json"

REQUIRED_BOTH = [
    "Secretaría General de Protección Civil y Emergencias",
    "Dirección General de Ejecución Penal y Reinserción Social",
    "Dirección General de Relaciones Internacionales y Extranjería",
    "Dirección General de Coordinación y Estudios",
    "Unidad Nacional de Retirada de Contenidos Ilícitos en Internet",
    "informes **anuales**",
    "Subdirección General de Sistemas de Información y Comunicaciones para la Seguridad",
    "Oficina Nacional de Garantías de los Derechos Humanos",
    "27 de abril de 2026",
    "💡 **HABLEMOS CLARO**",
    "🚔 **EN LA CALLE**",
    "🎯 **LO QUE CAE**",
    "📅 Ha caído",
]

FORBIDDEN = [
    "EN CRISTIANO",
    "El temario que nunca descansa",
    "Dirección General de Protección Civil y Emergencias depende de la Subsecretaría",
    "informes semestrales sobre la situación",
    "Oficina Nacional de Garantía de los Derechos Humanos",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/compilar_tema_07.py")],
        cwd=ROOT,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    require(manifest["normative_cutoff"] == "2026-07-28", "Corte normativo incorrecto")
    require(manifest["number"] == 7, "Número de tema incorrecto")

    parte = PARTE.read_text(encoding="utf-8")
    atestado = ATESTADO.read_text(encoding="utf-8")
    for phrase in REQUIRED_BOTH:
        require(phrase in parte, f"Falta en El Parte: {phrase}")
        require(phrase in atestado, f"Falta en El Atestado: {phrase}")
    for phrase in FORBIDDEN:
        require(phrase not in parte, f"Contenido prohibido en El Parte: {phrase}")
        require(phrase not in atestado, f"Contenido prohibido en El Atestado: {phrase}")

    parte_words = len(parte.split())
    atestado_words = len(atestado.split())
    require(parte_words < atestado_words, "El Parte no es más breve que El Atestado")
    require(atestado_words / parte_words >= 1.30, "Diferencia insuficiente entre vistas")

    coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
    bank_manifest = json.loads(BANK_MANIFEST.read_text(encoding="utf-8"))
    evaluation_plan = json.loads(EVALUATION_PLAN.read_text(encoding="utf-8"))
    questions = [
        json.loads(line)
        for line in BANK.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    facts = coverage["facts"]
    require(len(facts) == 106, "El inventario debe contener 106 hechos atómicos")
    require(len(questions) == 190, "El banco debe contener 190 preguntas")
    require(len({question["id"] for question in questions}) == len(questions), "IDs de preguntas duplicados")
    require(len({question["enunciado"] for question in questions}) == len(questions), "Enunciados duplicados")
    require(
        {question["fact_id"] for question in questions} == {fact["id"] for fact in facts},
        "El banco y la cobertura no contienen los mismos hechos",
    )
    by_fact = Counter(question["fact_id"] for question in questions)
    require(
        all(by_fact[fact["id"]] >= 2 for fact in facts if fact["riesgo_examen"] == 5),
        "Hay hechos de riesgo 5 sin segunda formulación",
    )
    answers = Counter(question["respuesta_correcta"] for question in questions)
    require(max(answers.values()) - min(answers.values()) <= 1, "Distribución A/B/C desequilibrada")
    for question in questions:
        require(set(question["opciones"]) == {"A", "B", "C"}, f"Opciones inválidas: {question['id']}")
        require(len(set(question["opciones"].values())) == 3, f"Opciones repetidas: {question['id']}")
        require(
            set(question["retroalimentacion"]) == {"acierto", "fallo"},
            f"Retroalimentación incompleta: {question['id']}",
        )
        for branch in ("acierto", "fallo"):
            require(
                set(question["retroalimentacion"][branch]) == {"humor", "explicacion"},
                f"Rama de retroalimentación inválida: {question['id']}/{branch}",
            )
    require(bank_manifest["quality_gate"]["status"] == "passed", "Puerta de calidad del banco no superada")
    require(bank_manifest["total_preguntas"] == len(questions), "Contador de preguntas incoherente")
    require(evaluation_plan["status"] == "ready", "Plan de evaluación bloqueado")
    require(
        [item["number"] for item in evaluation_plan["coverage_tests"]["blocks"]] == list(range(1, 17)),
        "El plan no cubre los 16 bloques",
    )

    print(
        f"OK · Parte {parte_words} palabras · Atestado {atestado_words} palabras · "
        f"ratio {atestado_words / parte_words:.2f} · "
        f"{len(facts)} hechos · {len(questions)} preguntas · "
        f"A/B/C {answers['A']}/{answers['B']}/{answers['C']}"
    )


if __name__ == "__main__":
    main()
