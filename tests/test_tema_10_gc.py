import json
import re
import unittest
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPIC = ROOT / "conocimiento/guardia-civil/tema-10"
BANK = ROOT / "banco-preguntas/guardia-civil/tema-10"
ASSETS = ROOT / "assets/guardia-civil/tema-10"
TESTS = ROOT / "build/evaluaciones/guardia-civil/tema-10/tests-generados"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class Tema10GuardiaCivilQualityGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = load_json(TOPIC / "manifest.json")
        cls.coverage = load_json(TOPIC / "cobertura.json")
        cls.questions = load_jsonl(BANK / "preguntas.jsonl")
        cls.official = load_json(BANK / "indice-oficiales.json")
        cls.assets = load_json(ASSETS / "manifest.json")
        cls.catalog = load_json(TESTS / "catalogo.json")
        cls.master = (TOPIC / "master.md").read_text(encoding="utf-8")

    def test_topic_contract(self):
        self.assertEqual(self.manifest["content_version"], "1.0.0")
        self.assertEqual(self.manifest["editorial_status"], "approved_internal")
        self.assertEqual(self.manifest["publication_status"], "not_published")
        self.assertEqual(self.manifest["semantic_blocks"], 66)
        self.assertEqual(self.manifest["atomic_facts"], 999)
        self.assertEqual(self.manifest["question_bank"]["questions"], 1386)
        self.assertEqual(self.manifest["question_bank"]["coverage_by_atomic_facts"], 100.0)

    def test_all_facts_are_covered(self):
        self.assertEqual(self.coverage["total_atomic_facts"], 999)
        self.assertEqual(self.coverage["covered_atomic_facts"], 999)
        self.assertEqual(self.coverage["coverage_percent"], 100.0)
        self.assertEqual({fact["bloque"] for fact in self.coverage["facts"]}, set(range(1, 67)))
        self.assertTrue(all(fact["covered"] for fact in self.coverage["facts"]))

    def test_official_scope_is_explicit_and_complete(self):
        self.assertIn("Ley 39/2015 completa", self.master)
        self.assertIn("títulos preliminar, I y III y disposición final tercera", self.master)
        self.assertIn("El título II de la Ley 40/2015", self.master)
        articles_39 = set()
        articles_40 = set()
        for question in self.questions:
            match = re.search(r"Artículo\s+(\d+)", question["articulo"], re.I)
            if not match:
                continue
            number = int(match.group(1))
            if question["norma"].startswith("Ley 39/2015"):
                articles_39.add(number)
            elif question["norma"].startswith("Ley 40/2015") and "Disposición final tercera" not in question["articulo"]:
                articles_40.add(number)
        self.assertEqual(articles_39, set(range(1, 134)))
        self.assertEqual(articles_40, set(range(1, 81)) | set(range(140, 159)))

    def test_question_bank_balance_feedback_and_uniqueness(self):
        self.assertEqual(len(self.questions), 1386)
        self.assertEqual(len({item["id"] for item in self.questions}), 1386)
        distribution = Counter(item["respuesta_correcta"] for item in self.questions)
        self.assertEqual(distribution, {"A": 462, "B": 462, "C": 462})
        for item in self.questions:
            self.assertEqual(set(item["opciones"]), {"A", "B", "C"})
            self.assertEqual(len(set(item["opciones"].values())), 3)
            self.assertIn(item["respuesta_correcta"], item["opciones"])
            self.assertTrue(item["retroalimentacion"]["acierto"]["humor"])
            self.assertTrue(item["retroalimentacion"]["acierto"]["explicacion"])
            self.assertTrue(item["retroalimentacion"]["fallo"]["humor"])
            self.assertTrue(item["retroalimentacion"]["fallo"]["explicacion"])
            self.assertEqual(item["caracter"], "propio")

    def test_high_risk_facts_have_two_formulations(self):
        questions_by_fact = defaultdict(list)
        for item in self.questions:
            questions_by_fact[item["fact_id"]].append(item)
        high_risk = [fact for fact in self.coverage["facts"] if fact["risk"] == 5]
        self.assertTrue(high_risk)
        for fact in high_risk:
            self.assertGreaterEqual(len(questions_by_fact[fact["id"]]), 2, fact["id"])

    def test_official_history_and_exact_critical_links(self):
        self.assertEqual(self.official["total_referencias"], 81)
        self.assertEqual(self.official["con_bloque_asignado"], 81)
        self.assertEqual(self.official["con_respuesta_verificada"], 81)
        fact_by_id = {fact["id"]: fact for fact in self.coverage["facts"]}
        official_by_id = {item["question_id"]: item for item in self.official["questions"]}
        for item in self.official["questions"]:
            self.assertTrue(item["fact_refs"])
            self.assertTrue(set(item["fact_refs"]) <= set(fact_by_id))
            self.assertEqual(item["answer_status"], "official_final_answer_key")
        expected = {
            "of-gc-p2024-1a-q055": "plazo de diez días",
            "of-gc-p2024-1a-q057": "funcionamiento de la Administración de Justicia",
            "of-gc-p2024-1a-q058": "composición multilateral o bilateral",
            "of-gc-p2026-a-q051": "desviación de poder",
            "of-gc-p2026-a-q052": "plazo de tres meses",
        }
        for question_id, needle in expected.items():
            facts = [fact_by_id[fact_id]["enunciado_atomico"] for fact_id in official_by_id[question_id]["fact_refs"]]
            self.assertIn(needle, " ".join(facts), question_id)

    def test_visuals_are_only_planned(self):
        self.assertEqual(self.assets["visual_version"], "0.0.0")
        self.assertEqual(self.assets["status"], "planned")
        self.assertEqual(self.assets["totals"], {"resources": 67, "integrated": 0, "planned": 67})
        self.assertFalse(list(ASSETS.glob("*.webp")))

    def test_generated_tests_cover_bank_once(self):
        self.assertEqual(self.catalog["total_tests"], 121)
        self.assertEqual(self.catalog["tests_cobertura_bloque"], 91)
        self.assertEqual(self.catalog["tests_por_partes"], 24)
        self.assertEqual(self.catalog["tests_finales"], 6)
        coverage_ids = []
        for entry in self.catalog["tests"]:
            data = load_json(TESTS / entry["ruta"])
            if entry["tipo"] == "cobertura_bloque":
                coverage_ids.extend(item["id"] for item in data["preguntas"])
        self.assertEqual(Counter(coverage_ids), Counter(item["id"] for item in self.questions))


if __name__ == "__main__":
    unittest.main()
