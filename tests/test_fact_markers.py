from __future__ import annotations

import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIXED_FACT = re.compile(r'^<!-- FACT:[A-Z0-9-]+ -->\s*\*\*', re.MULTILINE)


def load_compiler():
    path = ROOT / 'scripts/compilar_tema.py'
    spec = importlib.util.spec_from_file_location('compilar_tema', path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class FactMarkersTest(unittest.TestCase):
    def test_fact_markers_move_after_each_fact(self):
        module = load_compiler()
        source = (
            '<!-- FACT:PN-T03-F001 --> **Primer hecho.** Contenido. '
            '<!-- FACT:PN-T03-F002 --> **Segundo hecho.** Contenido.'
        )

        result = module.normalize_fact_markers(source)

        self.assertEqual(
            result,
            '**Primer hecho.** Contenido. <!-- FACT:PN-T03-F001 --> '
            '**Segundo hecho.** Contenido. <!-- FACT:PN-T03-F002 -->',
        )

    def test_tema_03_atestado_has_no_line_starting_with_fact_before_bold(self):
        path = ROOT / 'temas/policia-nacional/atestado/tema-03-constitucion-espanola-ii.md'
        text = path.read_text(encoding='utf-8')

        self.assertIsNone(PREFIXED_FACT.search(text))
        self.assertEqual(text.count('<!-- FACT:PN-T03-F'), 470)


if __name__ == '__main__':
    unittest.main()
