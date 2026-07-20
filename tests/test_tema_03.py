import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Tema03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads((ROOT / "conocimiento/policia-nacional/tema-03/manifest.json").read_text(encoding="utf-8"))
        cls.c = json.loads((ROOT / "conocimiento/policia-nacional/tema-03/cobertura.json").read_text(encoding="utf-8"))
        cls.master = (ROOT / cls.m["source_file"]).read_text(encoding="utf-8")
        cls.parte = (ROOT / cls.m["outputs"]["parte"]).read_text(encoding="utf-8")
        cls.atestado = (ROOT / cls.m["outputs"]["atestado"]).read_text(encoding="utf-8")

    def test_version(self):
        self.assertEqual(self.m["content_version"], "0.3.0")

    def test_blocks(self):
        self.assertEqual(self.master.count("<!-- BLOCK "), 50)
        self.assertEqual(self.m["semantic_blocks"], 25)

    def test_layers(self):
        expected = ["Mapa del tema", "Contenido", "Hablemos claro", "En la calle", "Lo que cae", "Ha caído"]
        self.assertEqual(self.m["layers"], expected)
        for document in (self.parte, self.atestado):
            self.assertEqual(sum(document.count("# " + layer) for layer in expected), 6)

    def test_atomic_facts(self):
        self.assertEqual(self.master.count("<!-- FACT:"), self.m["atomic_facts"])
        self.assertEqual(self.c["coverage_percent"], 100.0)

    def test_all_articles(self):
        self.assertEqual(self.c["required_constitution_articles"], self.c["covered_constitution_articles"])

    def test_derivatives(self):
        self.assertGreater(len(self.atestado), len(self.parte) * 2)
        self.assertIn("artículo 149", self.atestado.lower())

    def test_narrative_atestado(self):
        self.assertEqual(self.atestado.count("### Para entender el bloque"), 25)
        self.assertEqual(self.atestado.count("### Cómo estudiarlo"), 25)
        self.assertEqual(self.atestado.count("> **Ejemplo mental:**"), 25)
        bullet_lines = [line for line in self.atestado.splitlines() if line.startswith("- ")]
        self.assertLessEqual(len(bullet_lines), 5)

    def test_no_old_label(self):
        for document in (self.master, self.parte, self.atestado):
            self.assertNotIn("En cristiano", document)

    def test_no_legacy_quarantine(self):
        self.assertNotIn("continúan en cuarentena", self.master)
        self.assertNotIn("legacy_files_preserved", self.m)

    def test_ha_caido_safe(self):
        section = self.master.split("# Ha caído", 1)[1]
        self.assertIn("30 referencias históricas", section)
        self.assertIn("Ninguna alimenta todavía", section)

    def test_visual_assets(self):
        visual = json.loads((ROOT / "assets/policia-nacional/tema-03/manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(visual["summary"]["total"], 28)
        self.assertEqual(visual["summary"]["infografias"], 17)
        self.assertEqual(visual["summary"]["ilustraciones"], 11)
        for resource in visual["resources"]:
            path = ROOT / "assets/policia-nacional/tema-03" / resource["file"]
            self.assertTrue(path.exists(), resource["file"])
            ref = f"../../../assets/policia-nacional/tema-03/{resource['file']}"
            if "parte" in resource["documents"]:
                self.assertIn(ref, self.parte)
            if "atestado" in resource["documents"]:
                self.assertIn(ref, self.atestado)


if __name__ == "__main__":
    unittest.main()
