import json
import unittest
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPIC = ROOT / "conocimiento/policia-nacional/tema-08"
BANK = ROOT / "banco-preguntas/policia-nacional/tema-08"
ASSETS = ROOT / "assets/policia-nacional/tema-08"
TESTS = ROOT / "build/evaluaciones/policia-nacional/tema-08/tests-generados"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


class Tema08QualityGate(unittest.TestCase):
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
        self.assertEqual(self.manifest["visual_version"], "1.0.0")
        self.assertEqual(self.manifest["editorial_status"], "approved_internal")
        self.assertEqual(self.manifest["publication_status"], "not_published")
        self.assertEqual(self.manifest["semantic_blocks"], 28)
        self.assertEqual(self.manifest["atomic_facts"], 199)
        self.assertEqual(self.manifest["question_bank"]["questions"], 389)
        self.assertEqual(self.manifest["question_bank"]["coverage_by_atomic_facts"], 100.0)

    def test_all_facts_and_blocks_are_covered(self):
        self.assertEqual(self.coverage["total_atomic_facts"], 199)
        self.assertEqual(self.coverage["covered_atomic_facts"], 199)
        self.assertEqual(self.coverage["coverage_percent"], 100.0)
        self.assertEqual(self.coverage["scope"]["blocks_completed"], list(range(1, 29)))
        self.assertEqual(
            {fact["parte"] for fact in self.coverage["facts"]},
            set(range(1, 8)),
        )
        self.assertTrue(all(fact["covered"] for fact in self.coverage["facts"]))

    def test_question_bank_schema_balance_and_feedback(self):
        self.assertEqual(len(self.questions), 389)
        self.assertEqual(len({item["id"] for item in self.questions}), 389)
        distribution = Counter(item["respuesta_correcta"] for item in self.questions)
        self.assertLessEqual(max(distribution.values()) - min(distribution.values()), 1)
        self.assertEqual(set(distribution), {"A", "B", "C"})

        for item in self.questions:
            self.assertEqual(set(item["opciones"]), {"A", "B", "C"})
            self.assertEqual(len(set(item["opciones"].values())), 3)
            self.assertIn(item["respuesta_correcta"], item["opciones"])
            self.assertTrue(item["retroalimentacion"]["acierto"]["humor"])
            self.assertTrue(item["retroalimentacion"]["acierto"]["explicacion"])
            self.assertTrue(item["retroalimentacion"]["fallo"]["humor"])
            self.assertTrue(item["retroalimentacion"]["fallo"]["explicacion"])
            self.assertEqual(item["caracter"], "propio")
            self.assertIsNone(item["referencia_oficial"])

    def test_high_risk_facts_have_second_formulation(self):
        questions_by_fact = defaultdict(list)
        for item in self.questions:
            questions_by_fact[item["fact_id"]].append(item)
        high_risk = [fact for fact in self.coverage["facts"] if fact["risk"] == 5]
        self.assertTrue(high_risk)
        for fact in high_risk:
            formulations = questions_by_fact[fact["id"]]
            self.assertGreaterEqual(len(formulations), 2, fact["id"])
            self.assertGreaterEqual(
                len({item["tipo"] for item in formulations}),
                2,
                fact["id"],
            )

    def test_official_history_is_tracked_without_official_answer_claim(self):
        self.assertEqual(self.official["total_referencias"], 42)
        self.assertEqual(self.official["con_bloque_asignado"], 42)
        self.assertEqual(self.official["con_respuesta_verificada"], 42)
        self.assertFalse(self.official["display_policy"]["show_answer"])
        self.assertTrue(
            self.official["display_policy"]["never_present_as_official_plantilla"]
        )
        self.assertEqual(len(self.official["questions"]), 42)
        self.assertTrue(
            all(
                item["answer_status"]
                == "verificada_por_autor_no_plantilla_oficial"
                for item in self.official["questions"]
            )
        )

    def test_visual_package_is_complete(self):
        self.assertEqual(self.assets["visual_version"], "1.0.0")
        self.assertEqual(self.assets["status"], "integrated")
        self.assertEqual(
            self.assets["totals"],
            {"resources": 23, "integrated": 23, "planned": 0},
        )
        self.assertEqual(len(self.assets["resources"]), 23)
        for resource in self.assets["resources"]:
            path = ASSETS / resource["file"]
            self.assertTrue(path.is_file(), resource["file"])
            self.assertGreater(path.stat().st_size, 0, resource["file"])
            self.assertLessEqual(
                path.stat().st_size,
                resource["max_bytes"],
                resource["file"],
            )
            self.assertEqual(resource["status"], "integrated_webp")
            self.assertEqual(resource["source_content_version"], "1.0.0")

    def test_generated_tests_cover_bank_once(self):
        self.assertEqual(self.catalog["total_tests"], 47)
        self.assertEqual(self.catalog["tests_cobertura_bloque"], 29)
        self.assertEqual(self.catalog["tests_por_partes"], 14)
        self.assertEqual(self.catalog["tests_finales"], 4)

        coverage_ids = []
        for entry in self.catalog["tests"]:
            path = TESTS / entry["ruta"]
            test = load_json(path)
            self.assertLessEqual(test["numero_preguntas"], 25 if entry["tipo"] == "cobertura_bloque" else 50)
            if entry["tipo"] == "cobertura_bloque":
                coverage_ids.extend(item["id"] for item in test["preguntas"])

        bank_ids = [item["id"] for item in self.questions]
        self.assertEqual(Counter(coverage_ids), Counter(bank_ids))

    def test_legal_correction_and_editorial_language(self):
        self.assertIn("a disposición del Ministro del Interior", self.master)
        self.assertNotIn("a disposición de la DGP", self.master)
        self.assertNotIn("En cristiano", self.master)
        self.assertNotIn("0.9.0", self.master)


if __name__ == "__main__":
    unittest.main()
