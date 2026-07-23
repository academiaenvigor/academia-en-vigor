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
        self.assertEqual(len(questions), 18)
        self.assertTrue(all(q["appearance_status"] == "reviewed" for q in questions))
        self.assertTrue(all(q["counts_for_ha_caido"] is False for q in questions))

    def test_expected_years_by_block(self):
        years = defaultdict(set)
        for question in self.data["questions"]:
            for block in question["block_refs"]:
                years[block].add(question["series_year"])

        self.assertEqual(years[11], {2019, 2024})
        self.assertEqual(years[19], {2017, 2018, 2019, 2023})
        self.assertEqual(years[22], {2016, 2018, 2024})
        self.assertEqual(years[23], {2018, 2020})
        self.assertEqual(years[28], {2017, 2024})

    def test_explorer_loads_index_and_never_promotes_answers(self):
        explorer = (ROOT / "explorador.html").read_text(encoding="utf-8")
        self.assertIn("inyectarAntecedentesOficiales", explorer)
        self.assertIn("appearance_status==='reviewed'", explorer)
        self.assertIn("No se muestra una solución como oficial", explorer)


if __name__ == "__main__":
    unittest.main()
