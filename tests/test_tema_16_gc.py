import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
K = ROOT / "conocimiento/guardia-civil/tema-16"
B = ROOT / "banco-preguntas/guardia-civil/tema-16"
A = ROOT / "assets/guardia-civil/tema-16"

class Tema16GuardiaCivilQualityGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coverage = json.loads((K / "cobertura.json").read_text())
        cls.bank = [json.loads(x) for x in (B / "preguntas.jsonl").read_text().splitlines() if x.strip()]
        cls.index = json.loads((B / "indice-oficiales.json").read_text())
        cls.master = (K / "master.md").read_text()

    def test_topic_contract_and_scope(self):
        self.assertEqual(48, len(self.coverage["blocks"]))
        self.assertEqual(self.coverage["total_atomic_facts"], len(self.coverage["facts"]))
        self.assertIn("títulos I a V", self.master)
        self.assertIn("título preliminar y títulos II a IV", self.master)
        self.assertIn("capítulos I y II", self.master)

    def test_repealed_directive_is_not_presented_as_current(self):
        self.assertIn("dejó de estar vigente el 12/10/2025", self.master)
        self.assertIn("Directiva (UE) 2023/1791", self.master)
        self.assertIn("norma programada histórica", self.master)

    def test_bank_balance_feedback_and_coverage(self):
        self.assertEqual(len(self.bank), len({q["id"] for q in self.bank}))
        counts = Counter(q["respuesta_correcta"] for q in self.bank)
        self.assertLessEqual(max(counts.values()) - min(counts.values()), 1)
        by_fact = Counter(q["fact_id"] for q in self.bank)
        for fact in self.coverage["facts"]:
            self.assertGreaterEqual(by_fact[fact["id"]], 2 if fact["riesgo_examen"] == 5 else 1)
        for q in self.bank:
            self.assertEqual({"A", "B", "C"}, set(q["opciones"]))
            self.assertEqual(3, len(set(q["opciones"].values())))
            self.assertTrue(q["retroalimentacion"]["acierto"]["humor"] and q["retroalimentacion"]["fallo"]["explicacion"])

    def test_official_mapping(self):
        self.assertGreaterEqual(self.index["total_referencias"], 20)
        self.assertEqual(self.index["total_referencias"], self.index["con_respuesta_verificada"] + self.index["en_cuarentena"])
        self.assertEqual(1, self.index["en_cuarentena"])
        self.assertTrue(all(q["fact_refs"][0].startswith("GC-T16-F") for q in self.index["questions"]))

    def test_visuals_only_planned(self):
        manifest = json.loads((A / "manifest.json").read_text())
        self.assertEqual(0, manifest["totals"]["integrated"])
        self.assertEqual(49, manifest["totals"]["planned"])
        self.assertFalse(list(A.glob("*.webp")))

if __name__ == "__main__":
    unittest.main()
