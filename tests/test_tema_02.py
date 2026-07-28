
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class Tema02(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / "conocimiento/policia-nacional/tema-02/manifest.json").read_text(encoding="utf-8"))
        self.master = (ROOT / self.manifest["source_file"]).read_text(encoding="utf-8")
        self.parte = (ROOT / self.manifest["outputs"]["parte"]).read_text(encoding="utf-8")
        self.atestado = (ROOT / self.manifest["outputs"]["atestado"]).read_text(encoding="utf-8")

    def test_blocks_and_facts(self):
        self.assertEqual(self.manifest["semantic_blocks"], 37)
        self.assertEqual(self.master.count("<!-- BLOCK "), 74)
        self.assertEqual(self.master.count("<!-- FACT:"), self.manifest["atomic_facts"])

    def test_articles_and_reforms(self):
        coverage = json.loads((ROOT / self.manifest["coverage_file"]).read_text(encoding="utf-8"))
        requirements = coverage["requirements"]
        self.assertEqual(requirements["required_constitution_articles"], list(range(1, 56)))
        self.assertEqual(requirements["covered_constitution_articles"], list(range(1, 56)))
        self.assertIn("cuatro veces", self.parte.lower())
        self.assertIn("69.3", self.atestado)

    def test_webp_only(self):
        for document in (self.master, self.parte, self.atestado):
            self.assertNotIn(".png", document.lower())

    def test_bank(self):
        questions = [json.loads(line) for line in (ROOT / self.manifest["question_bank"]["path"]).read_text(encoding="utf-8").splitlines() if line]
        self.assertEqual(len(questions), self.manifest["question_bank"]["questions"])
        self.assertEqual({q["respuesta_correcta"] for q in questions}, {"A", "B", "C"})
        self.assertTrue(all(len(q["opciones"]) == 3 for q in questions))
        self.assertTrue(all(len(set(q["opciones"].values())) == 3 for q in questions))

    def test_visual_and_multimedia(self):
        visual = json.loads((ROOT / self.manifest["assets"]["manifest"]).read_text(encoding="utf-8"))
        media = json.loads((ROOT / self.manifest["teaching_materials"]["manifest"]).read_text(encoding="utf-8"))
        self.assertEqual(visual["totals"]["resources"], 22)
        self.assertEqual(sum(r["type"] == "infografia" for r in visual["resources"]), 14)
        self.assertEqual(sum(r["type"] == "ilustracion_simple" for r in visual["resources"]), 8)
        self.assertEqual(len(media["parts"]), 7)
        self.assertEqual(len(media["resources"]), 28)

    def test_official_markers_safe(self):
        index = json.loads((ROOT / self.manifest["official_exam_index"]).read_text(encoding="utf-8"))
        self.assertEqual(index["con_bloque_asignado"], index["total_referencias"])
        self.assertEqual(index["con_respuesta_verificada"], index["total_referencias"])
        self.assertTrue(index["display_policy"]["never_present_as_official_plantilla"])

if __name__ == "__main__":
    unittest.main()
