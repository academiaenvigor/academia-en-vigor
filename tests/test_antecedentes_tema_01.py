from __future__ import annotations

import json
import unittest
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = (
    ROOT
    / "banco-preguntas"
    / "policia-nacional"
    / "tema-01"
    / "indice-oficiales.json"
)


class AntecedentesTema01Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(INDEX.read_text(encoding="utf-8"))

    def test_pilot_has_reviewed_appearances(self):
        questions = self.data["questions"]
        self.assertEqual(len(questions), self.data["total_referencias"])
        self.assertEqual(len({q["question_id"] for q in questions}), len(questions))
        self.assertTrue(
            all(q["appearance_status"] in {"reviewed", "auto_proposed", "editorially_mapped"} for q in questions)
        )
        self.assertTrue(self.data["display_policy"]["never_present_as_official_plantilla"])

    def test_expected_years_by_block(self):
        years = defaultdict(set)
        for question in self.data["questions"]:
            for block in question["block_refs"]:
                years[block].add(question["series_year"])

        self.assertTrue(years)
        self.assertTrue(all(year >= 2016 for block_years in years.values() for year in block_years))
        self.assertEqual(
            sum(self.data["por_bloque"].values()),
            sum(len(question["block_refs"]) for question in self.data["questions"]),
        )

    def test_explorer_loads_index_and_never_promotes_answers(self):
        explorer = (ROOT / "explorador.html").read_text(encoding="utf-8")
        self.assertIn("inyectarAntecedentesOficiales", explorer)
        self.assertIn("appearance_status==='reviewed'", explorer)
        self.assertIn("No se muestra una solución como oficial", explorer)


if __name__ == "__main__":
    unittest.main()
