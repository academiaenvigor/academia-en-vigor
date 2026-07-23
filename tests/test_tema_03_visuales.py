from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets/policia-nacional/tema-03"
MASTER = ROOT / "conocimiento/policia-nacional/tema-03/master.md"
OUTPUTS = (
    ROOT / "temas/policia-nacional/parte/tema-03-constitucion-espanola-ii.md",
    ROOT / "temas/policia-nacional/atestado/tema-03-constitucion-espanola-ii.md",
)


def load_compiler():
    path = ROOT / "scripts/compilar_tema.py"
    spec = importlib.util.spec_from_file_location("compilar_tema", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def load_manifest() -> dict:
    return json.loads((ASSETS / "manifest.json").read_text(encoding="utf-8"))


class VisualesTema03(unittest.TestCase):
    def test_catalogo_contiene_17_infografias_y_11_ilustraciones(self):
        resources = load_manifest()["resources"]
        self.assertEqual(len(resources), 28)
        self.assertEqual(sum(r["type"] == "infografia" for r in resources), 17)
        self.assertEqual(
            sum(r["type"] == "ilustracion_simple" for r in resources), 11
        )
        self.assertEqual(
            sum(r["status"] == "pending_visual_review" for r in resources), 17
        )
        self.assertEqual(
            sum(r["status"] == "approved_internal" for r in resources), 11
        )

    def test_assets_activos_son_webp_validos_y_menores_de_1_mb(self):
        for resource in load_manifest()["resources"]:
            filename = resource["file"]
            self.assertTrue(filename.endswith(".webp"), filename)
            path = ASSETS / filename
            self.assertTrue(path.is_file(), filename)
            self.assertLess(path.stat().st_size, 1_000_000, filename)
            data = path.read_bytes()[:12]
            self.assertEqual(data[:4], b"RIFF", filename)
            self.assertEqual(data[8:12], b"WEBP", filename)

    def test_fuente_maestra_referencia_exactamente_el_catalogo_webp(self):
        compiler = load_compiler()
        text = MASTER.read_text(encoding="utf-8")
        referenced = {
            match.group("archivo")
            for block in compiler.VISUAL_BLOCK_RE.finditer(text)
            for match in compiler.VISUAL_REF_RE.finditer(block.group(1))
        }
        catalog = {resource["file"] for resource in load_manifest()["resources"]}
        self.assertEqual(referenced, catalog)
        self.assertNotIn(".png", text)

    def test_parte_y_atestado_estan_compilados_con_webp(self):
        for output in OUTPUTS:
            text = output.read_text(encoding="utf-8")
            self.assertNotIn(".png", text)
            self.assertNotIn("VISUAL PENDIENTE", text)
            self.assertIn("../../../assets/policia-nacional/tema-03/", text)
            self.assertIn(".webp", text)

    def test_materiales_se_organizan_en_seis_partes(self):
        data = json.loads(
            (
                ROOT
                / "materiales-didacticos/policia-nacional/tema-03/manifest.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(data["schema_version"], "2.1.0")
        self.assertEqual(len(data["parts"]), 6)
        self.assertEqual(len(data["resources"]), 24)
        for part in data["parts"]:
            resources = [
                r for r in data["resources"] if r["part_number"] == part["number"]
            ]
            self.assertEqual(len(resources), 4)
            self.assertEqual(
                {r["category"] for r in resources},
                {"audios", "videos", "presentaciones", "infografias"},
            )
            self.assertEqual(
                {tuple(r["blocks"]) for r in resources}, {tuple(part["blocks"])}
            )


if __name__ == "__main__":
    unittest.main()
