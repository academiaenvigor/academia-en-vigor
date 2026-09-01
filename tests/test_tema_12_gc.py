import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
K = ROOT / "conocimiento/guardia-civil/tema-12"
B = ROOT / "banco-preguntas/guardia-civil/tema-12"
A = ROOT / "assets/guardia-civil/tema-12"

class Tema12GuardiaCivilQualityGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coverage = json.loads((K / "cobertura.json").read_text())
        cls.bank = [json.loads(x) for x in (B / "preguntas.jsonl").read_text().splitlines() if x.strip()]
        cls.index = json.loads((B / "indice-oficiales.json").read_text())
        cls.master = (K / "master.md").read_text()

    def test_topic_contract(self):
        self.assertEqual(55, len(self.coverage["blocks"]))
        self.assertEqual(self.coverage["total_atomic_facts"], len(self.coverage["facts"]))
        self.assertIn("artículo 35 bis", self.master.lower())
        self.assertIn("artículo 35 quinquies", self.master)

    def test_bank_balance_feedback_and_coverage(self):
        ids = {q["id"] for q in self.bank}
        self.assertEqual(len(ids), len(self.bank))
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
        self.assertEqual(42, self.index["total_referencias"])
        self.assertEqual(42, self.index["con_respuesta_verificada"])
        items = {q["question_id"]: q for q in self.index["questions"]}
        self.assertIn("GC-T12", items["of-gc-p2024-1a-q064"]["fact_refs"][0])
        facts = {f["id"]: f for f in self.coverage["facts"]}
        self.assertIn("Abogacía del Estado", facts[items["of-gc-p2024-1a-q064"]["fact_refs"][0]]["enunciado_atomico"] or facts[items["of-gc-p2024-1a-q064"]["fact_refs"][0]]["bloque_titulo"])

    def test_visuals_match_disk(self):
        manifest = json.loads((A / "manifest.json").read_text())
        totals = manifest["totals"]
        self.assertEqual(56, totals["resources"])
        self.assertEqual(totals["resources"], totals["integrated"] + totals["planned"])
        en_disco = {ruta.name for ruta in A.glob("*.webp")}
        declaradas = {
            recurso["file"]
            for recurso in manifest.get("resources", [])
            if recurso.get("status") == "integrated_webp"
        }
        self.assertEqual(declaradas, en_disco)

if __name__ == "__main__":
    unittest.main()
