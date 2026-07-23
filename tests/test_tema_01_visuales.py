from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets/policia-nacional/tema-01"
MASTER = ROOT / "conocimiento/policia-nacional/tema-01/master.md"
OUTPUTS = (
    ROOT / "temas/policia-nacional/parte/tema-01-el-derecho-la-persona-y-la-nacionalidad.md",
    ROOT / "temas/policia-nacional/atestado/tema-01-el-derecho-la-persona-y-la-nacionalidad.md",
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


class VisualesTema01(unittest.TestCase):
    def test_catalogo_contiene_21_infografias_y_6_ilustraciones(self):
        resources = load_manifest()["resources"]
        self.assertEqual(len(resources), 27)
        self.assertEqual(sum(resource["type"] == "infografia" for resource in resources), 21)
        self.assertEqual(sum(resource["type"] == "ilustracion_simple" for resource in resources), 6)
        self.assertEqual({resource["status"] for resource in resources}, {"approved_internal"})

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
        self.assertNotIn("PENDIENTE DE GENERAR", text)

    def test_parte_y_atestado_estan_compilados_con_webp(self):
        for output in OUTPUTS:
            text = output.read_text(encoding="utf-8")
            self.assertNotIn(".png", text)
            self.assertNotIn("VISUAL PENDIENTE", text)
            self.assertIn("../../../assets/policia-nacional/tema-01/", text)
            self.assertIn(".webp", text)


if __name__ == "__main__":
    unittest.main()
