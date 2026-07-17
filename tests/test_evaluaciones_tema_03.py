import collections
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build/evaluaciones/policia-nacional/tema-03/tests-generados"


class EvaluacionesTema03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, "scripts/generar_evaluaciones_tema_03.py"], cwd=ROOT, check=True)
        cls.bank = [json.loads(line) for line in (ROOT / "banco-preguntas/policia-nacional/tema-03/preguntas.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
        cls.catalogue = json.loads((OUT / "catalogo.json").read_text(encoding="utf-8"))

    @staticmethod
    def load(entry):
        return json.loads((OUT / entry["ruta"]).read_text(encoding="utf-8"))

    def test_catalogue_counts(self):
        self.assertEqual(self.catalogue["total_tests"], 61)
        self.assertEqual(self.catalogue["tests_cobertura_bloque"], 40)
        self.assertEqual(self.catalogue["tests_por_partes"], 18)
        self.assertEqual(self.catalogue["tests_finales"], 3)

    def test_block_tests_cover_bank_exactly_once(self):
        ids = []
        for entry in self.catalogue["tests"]:
            if entry["tipo"] == "cobertura_bloque":
                ids.extend(q["id"] for q in self.load(entry)["preguntas"])
        self.assertEqual(collections.Counter(ids), collections.Counter(q["id"] for q in self.bank))

    def test_limits_and_solutions(self):
        bank = {q["id"]: q for q in self.bank}
        for entry in self.catalogue["tests"]:
            data = self.load(entry)
            if entry["tipo"] == "cobertura_bloque":
                self.assertLessEqual(entry["preguntas"], 25)
            self.assertEqual(len(data["preguntas"]), len(data["soluciones"]))
            for solution in data["soluciones"]:
                self.assertEqual(solution["respuesta_correcta"], bank[solution["id"]]["respuesta_correcta"])

    def test_part_and_final_sizes(self):
        parts = [e for e in self.catalogue["tests"] if e["tipo"] == "test_parte"]
        finals = [e for e in self.catalogue["tests"] if e["tipo"] == "test_final"]
        self.assertEqual(len(parts), 18)
        self.assertTrue(all(e["preguntas"] == 25 for e in parts))
        self.assertEqual([e["preguntas"] for e in finals], [25, 50, 100])


if __name__ == "__main__":
    unittest.main()
