import json
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "conocimiento/policia-nacional/tema-19/master.md"
TOPIC = ROOT / "conocimiento/policia-nacional/tema-19"
BANK = ROOT / "banco-preguntas/policia-nacional/tema-19"
ASSETS = ROOT / "assets/policia-nacional/tema-19"


class Tema19QualityGate(unittest.TestCase):
    def setUp(self):
        self.coverage = json.loads((TOPIC / "cobertura.json").read_text(encoding="utf-8"))
        self.questions = [
            json.loads(line)
            for line in (BANK / "preguntas.jsonl").read_text(encoding="utf-8").splitlines()
            if line
        ]
        self.assets = json.loads((ASSETS / "manifest.json").read_text(encoding="utf-8"))

    def test_exact_scope_counts(self):
        self.assertEqual(self.coverage["total_atomic_facts"], 124)
        self.assertEqual(len(self.coverage["facts"]), 124)
        self.assertEqual(len(self.questions), 248)
        self.assertEqual({fact["bloque"] for fact in self.coverage["facts"]}, set(range(1, 32)))

    def test_question_schema_balance_and_double_feedback(self):
        self.assertEqual(Counter(q["respuesta_correcta"] for q in self.questions), {"A": 83, "B": 83, "C": 82})
        self.assertEqual(len({q["id"] for q in self.questions}), 248)
        for question in self.questions:
            self.assertEqual(set(question["opciones"]), {"A", "B", "C"})
            self.assertEqual(len(set(question["opciones"].values())), 3)
            self.assertIn(question["respuesta_correcta"], question["opciones"])
            self.assertTrue(question["retroalimentacion"]["acierto"]["explicacion"])
            self.assertTrue(question["retroalimentacion"]["fallo"]["explicacion"])

    def test_critical_current_rules_are_explicit(self):
        text = MASTER.read_text(encoding="utf-8")
        self.assertIn("Los artículos 552, 555, 557 ter y 559 están suprimidos", text)
        self.assertIn("El artículo 556 vigente solo tiene dos apartados", text)
        self.assertIn("cinco o más armas", text)
        self.assertIn("sin distinguir entre armas cortas y largas", text)
        self.assertIn("Desde el 10 de abril de 2026", text)
        self.assertIn("artículo 568.2", text)
        self.assertIn("combustible líquido", text)

    def test_visual_assets_and_compiled_documents(self):
        self.assertEqual(self.assets["totals"], {"resources": 28, "integrated": 28, "planned": 0})
        self.assertEqual(Counter(r["type"] for r in self.assets["resources"]), {"infografia": 22, "ilustracion_simple": 6})
        for resource in self.assets["resources"]:
            path = ASSETS / resource["file"]
            self.assertTrue(path.is_file())
            self.assertLess(path.stat().st_size, 1_000_000)
        parte = next((ROOT / "temas/policia-nacional/parte").glob("tema-19-*.md")).read_text(encoding="utf-8")
        atestado = next((ROOT / "temas/policia-nacional/atestado").glob("tema-19-*.md")).read_text(encoding="utf-8")
        self.assertEqual(parte.count("<!-- VISUAL:"), 18)
        self.assertEqual(atestado.count("<!-- VISUAL:"), 28)

    def test_historical_items_remain_quarantined(self):
        index = json.loads((BANK / "indice-oficiales.json").read_text(encoding="utf-8"))
        self.assertEqual(index["total_referencias"], 9)
        self.assertEqual(index["con_respuesta_verificada"], 0)
        self.assertFalse(index["display_policy"]["show_reviewed_appearances"])
        for item in index["questions"]:
            self.assertFalse(item["counts_for_ha_caido"])
            self.assertIsNone(item["respuesta"])
            self.assertEqual(item["verification_status"], "quarantine")

    def test_evaluation_catalogue(self):
        catalogue = ROOT / "build/evaluaciones/policia-nacional/tema-19/tests-generados/catalogo.json"
        data = json.loads(catalogue.read_text(encoding="utf-8"))
        self.assertEqual(data["total_tests"], 43)


if __name__ == "__main__":
    unittest.main()
