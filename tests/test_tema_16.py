import json
import unittest
from collections import Counter
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TOPIC = ROOT / "conocimiento/policia-nacional/tema-16"
BANK = ROOT / "banco-preguntas/policia-nacional/tema-16"
ASSETS = ROOT / "assets/policia-nacional/tema-16"
MASTER = TOPIC / "master.md"


class Tema16QualityGate(unittest.TestCase):
    def setUp(self):
        self.coverage = json.loads((TOPIC / "cobertura.json").read_text(encoding="utf-8"))
        self.questions = [
            json.loads(line)
            for line in (BANK / "preguntas.jsonl").read_text(encoding="utf-8").splitlines()
            if line
        ]
        self.assets = json.loads((ASSETS / "manifest.json").read_text(encoding="utf-8"))

    def test_exact_scope_counts(self):
        self.assertEqual(self.coverage["total_atomic_facts"], 212)
        self.assertEqual(len(self.coverage["facts"]), 212)
        self.assertEqual(len(self.questions), 424)
        self.assertEqual({fact["bloque"] for fact in self.coverage["facts"]}, set(range(1, 54)))

    def test_question_schema_balance_and_double_feedback(self):
        self.assertEqual(Counter(q["respuesta_correcta"] for q in self.questions), {"A": 142, "B": 141, "C": 141})
        self.assertEqual(len({q["id"] for q in self.questions}), 424)
        for question in self.questions:
            self.assertEqual(set(question["opciones"]), {"A", "B", "C"})
            self.assertEqual(len(set(question["opciones"].values())), 3)
            self.assertIn(question["respuesta_correcta"], question["opciones"])
            self.assertTrue(question["retroalimentacion"]["acierto"]["explicacion"])
            self.assertTrue(question["retroalimentacion"]["fallo"]["explicacion"])

    def test_critical_current_rules_are_explicit(self):
        text = MASTER.read_text(encoding="utf-8")
        self.assertIn("Corte normativo: 2026-08-01", text)
        self.assertIn("LO1-2026-T16", text)
        self.assertIn("No se computan antecedentes cancelados o cancelables", text)
        self.assertIn("tipos agravados por multirreincidencia de delitos leves", text)
        self.assertIn("mayores de catorce y menores de dieciocho años", text)
        self.assertIn("artículo 23 de la Ley Orgánica del Poder Judicial", text)

    def test_visual_assets_and_compiled_documents(self):
        self.assertEqual(self.assets["totals"], {"resources": 32, "integrated": 32, "planned": 0})
        self.assertEqual(Counter(r["type"] for r in self.assets["resources"]), {"infografia": 26, "ilustracion_simple": 6})
        hashes = set()
        for resource in self.assets["resources"]:
            path = ASSETS / resource["file"]
            self.assertTrue(path.is_file())
            self.assertLess(path.stat().st_size, 1_000_000)
            with Image.open(path) as image:
                image.load()
                self.assertEqual(image.size, (1600, 900))
            hashes.add(path.read_bytes())
        self.assertEqual(len(hashes), 32)
        parte = next((ROOT / "temas/policia-nacional/parte").glob("tema-16-*.md")).read_text(encoding="utf-8")
        atestado = next((ROOT / "temas/policia-nacional/atestado").glob("tema-16-*.md")).read_text(encoding="utf-8")
        self.assertEqual(parte.count("<!-- VISUAL:"), 20)
        self.assertEqual(atestado.count("<!-- VISUAL:"), 32)

    def test_historical_items_remain_quarantined(self):
        index = json.loads((BANK / "indice-oficiales.json").read_text(encoding="utf-8"))
        self.assertEqual(index["total_referencias"], 18)
        self.assertEqual(index["con_respuesta_verificada"], 0)
        self.assertFalse(index["display_policy"]["show_reviewed_appearances"])
        for item in index["questions"]:
            self.assertFalse(item["counts_for_ha_caido"])
            self.assertIsNone(item["respuesta"])
            self.assertEqual(item["verification_status"], "quarantine")

    def test_evaluation_catalogue(self):
        catalogue = ROOT / "build/evaluaciones/policia-nacional/tema-16/tests-generados/catalogo.json"
        data = json.loads(catalogue.read_text(encoding="utf-8"))
        self.assertEqual(data["total_tests"], 67)
        self.assertEqual(data["tests_cobertura_bloque"], 53)
        self.assertEqual(data["tests_por_partes"], 10)
        self.assertEqual(data["tests_finales"], 4)


if __name__ == "__main__":
    unittest.main()
