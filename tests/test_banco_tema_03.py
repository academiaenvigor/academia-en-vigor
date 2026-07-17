import collections
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BancoTema03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coverage = json.loads((ROOT / "conocimiento/policia-nacional/tema-03/cobertura.json").read_text(encoding="utf-8"))
        cls.questions = [json.loads(line) for line in (ROOT / "banco-preguntas/policia-nacional/tema-03/preguntas.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]

    def test_ids_and_wording(self):
        self.assertEqual(len(self.questions), len({q["id"] for q in self.questions}))
        self.assertEqual(len(self.questions), len({q["enunciado"] for q in self.questions}))

    def test_all_facts_covered(self):
        self.assertEqual({f["id"] for f in self.coverage["facts"]}, {q["fact_id"] for q in self.questions})

    def test_options(self):
        for question in self.questions:
            self.assertEqual(set(question["opciones"]), {"A", "B", "C"})
            self.assertEqual(len(set(question["opciones"].values())), 3)

    def test_balance(self):
        counts = collections.Counter(q["respuesta_correcta"] for q in self.questions)
        self.assertEqual(counts, {"A": 246, "B": 246, "C": 246})

    def test_versions_and_character(self):
        self.assertTrue(all(q["content_version"] == "0.3.0" for q in self.questions))
        self.assertTrue(all(q["caracter"] == "propio" and q["referencia_oficial"] is None for q in self.questions))

    def test_risk5_double(self):
        counts = collections.Counter(q["fact_id"] for q in self.questions)
        self.assertTrue(all(counts[f["id"]] >= 2 for f in self.coverage["facts"] if f["risk"] == 5))


if __name__ == "__main__":
    unittest.main()
