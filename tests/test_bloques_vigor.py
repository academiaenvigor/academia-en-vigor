"""Contrato de bloques semánticos VIGOR.

Estos casos se escriben con `unittest` a propósito: el flujo de CI usa
`python -m unittest discover -s tests`, que NO recoge las funciones sueltas al
estilo pytest. Cuando este archivo eran funciones, sus fallos no llegaban a
aparecer en el workflow.
"""
from __future__ import annotations

import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGACY_CALLOUT = re.compile(
    r"^>\s*(?:[^\w\s>]{1,3}\s*)?\*\*\s*"
    r"(?:hablemos claro|en la calle|lo que cae|perla vigor|trampa|"
    r"no confundas|alerta del vig[ií]a|ha ca[ií]do|ejemplo mental)"
    r"\s*:?\s*\*\*",
    re.IGNORECASE | re.MULTILINE,
)


def load_compiler():
    path = ROOT / "scripts/compilar_tema.py"
    spec = importlib.util.spec_from_file_location("compilar_tema", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def topics() -> list[dict]:
    data = json.loads((ROOT / "temario.json").read_text(encoding="utf-8"))
    return [
        (opposition, topic)
        for opposition, info in data["oppositions"].items()
        for topic in info["topics"]
    ]


class BloquesVigor(unittest.TestCase):
    def test_all_semantic_types_are_allowed(self):
        module = load_compiler()
        expected = {
            "hablemos-claro", "en-la-calle", "lo-que-cae",
            "perla-vigor", "trampa", "ha-caido", "visual",
        }
        self.assertEqual(module.VIGOR_BLOCKS, expected)

    def test_masters_have_balanced_semantic_blocks(self):
        module = load_compiler()
        for opposition, topic in topics():
            code = f"tema-{int(topic['number']):02d}"
            path = ROOT / f"conocimiento/{opposition}/{code}/master.md"
            with self.subTest(tema=code):
                module.validate_vigor_blocks(
                    path.read_text(encoding="utf-8"), str(path.relative_to(ROOT))
                )

    def test_no_quedan_callouts_en_formato_antiguo(self):
        """Los avisos en blockquote quedan fuera de los filtros del explorador."""
        for opposition, topic in topics():
            code = f"tema-{int(topic['number']):02d}"
            path = ROOT / f"conocimiento/{opposition}/{code}/master.md"
            with self.subTest(tema=code):
                encontrados = LEGACY_CALLOUT.findall(path.read_text(encoding="utf-8"))
                self.assertEqual(
                    encontrados, [],
                    f"{code}: quedan callouts antiguos; "
                    "ejecuta scripts/migrar_callouts.py --write",
                )

    def test_compiled_views_preserve_semantic_blocks(self):
        """El compilador conserva los callouts y convierte :::visual en imagen."""
        for opposition, topic in topics():
            code = f"tema-{int(topic['number']):02d}"
            for vista in ("parte", "atestado"):
                with self.subTest(tema=code, vista=vista):
                    text = (ROOT / topic[vista]).read_text(encoding="utf-8")
                    # render_visuals() sustituye :::visual por HTML: en el
                    # derivado no debe quedar ningún bloque visual sin resolver.
                    self.assertNotIn(":::visual", text, f"{code}/{vista}")
                    self.assertRegex(text, r"<!-- VISUAL(?: PENDIENTE)?:")

    def test_las_seis_capas_son_identicas_en_todos_los_temas(self):
        esperado = [
            "Mapa del tema", "Contenido", "Hablemos claro",
            "En la calle", "Lo que cae", "Ha caído",
        ]
        for opposition, topic in topics():
            code = f"tema-{int(topic['number']):02d}"
            for vista in ("parte", "atestado"):
                with self.subTest(tema=code, vista=vista):
                    text = (ROOT / topic[vista]).read_text(encoding="utf-8")
                    self.assertEqual(re.findall(r"^# (.+)$", text, re.M)[1:], esperado)

    def test_explorer_supports_filters_and_auto_images(self):
        text = (ROOT / "explorador.html").read_text(encoding="utf-8")
        self.assertIn("function filtrar", text)
        self.assertIn("function resolverVisuales", text)
        self.assertIn("'hablemos-claro'", text)
        self.assertIn("'lo-que-cae'", text)


if __name__ == "__main__":
    unittest.main()
