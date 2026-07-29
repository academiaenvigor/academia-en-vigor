import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Tema07(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.master = (
            ROOT / "conocimiento/policia-nacional/tema-07/master.md"
        ).read_text(encoding="utf-8")
        cls.coverage = json.loads(
            (ROOT / "conocimiento/policia-nacional/tema-07/cobertura.json").read_text(
                encoding="utf-8"
            )
        )
        cls.assets = json.loads(
            (ROOT / "assets/policia-nacional/tema-07/manifest.json").read_text(
                encoding="utf-8"
            )
        )

    def test_universal_structure_and_traceability(self):
        self.assertEqual(len(re.findall(r"<!-- BLOCK \d{2} START -->", self.master)), 16)
        fact_ids = {fact["id"] for fact in self.coverage["facts"]}
        master_ids = set(re.findall(r"<!-- FACT:([A-Z0-9-]+) -->", self.master))
        self.assertEqual(len(fact_ids), 106)
        self.assertEqual(master_ids, fact_ids)

    def test_visual_inventory_matches_master(self):
        inventory = {resource["file"] for resource in self.assets["resources"]}
        references = set(re.findall(r"`([^`]+\.webp)`", self.master))
        self.assertEqual(inventory, references)
        self.assertEqual(
            self.assets["totals"],
            {"resources": 13, "integrated": 13, "planned": 0},
        )

    def test_giese_source_uses_the_correct_boe_identifier(self):
        catalog = json.loads(
            (ROOT / "fuentes/catalogo.json").read_text(encoding="utf-8")
        )
        source = next(
            item for item in catalog["sources"] if item["id"] == "GIESE-RD904-2021"
        )
        self.assertIn("BOE-A-2021-17049", source["url"])
        self.assertNotIn(
            "src-es-boe-a-2021-17346",
            {fact["fuente"] for fact in self.coverage["facts"]},
        )


if __name__ == "__main__":
    unittest.main()
