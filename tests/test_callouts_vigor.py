import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location('compilar_tema', ROOT / 'scripts/compilar_tema.py')
compilar_tema = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(compilar_tema)


class CalloutsVigor(unittest.TestCase):
    def test_esquema_semantico_admitido(self):
        self.assertEqual(
            compilar_tema.VIGOR_BLOCKS,
            {'hablemos-claro', 'en-la-calle', 'lo-que-cae', 'perla-vigor', 'trampa', 'ha-caido', 'visual'},
        )

    def test_tema_01_usa_marcas_semanticas(self):
        path = ROOT / 'conocimiento/policia-nacional/tema-01/master.md'
        text = path.read_text(encoding='utf-8')
        self.assertIn(':::hablemos-claro', text)
        self.assertIn(':::lo-que-cae', text)
        self.assertIn(':::visual', text)
        compilar_tema.validate_vigor_blocks(text, 'conocimiento/policia-nacional/tema-01/master.md')

    def test_derivados_conservan_marcas(self):
        for relative in (
            'temas/policia-nacional/parte/tema-01-el-derecho-la-persona-y-la-nacionalidad.md',
            'temas/policia-nacional/atestado/tema-01-el-derecho-la-persona-y-la-nacionalidad.md',
        ):
            output = (ROOT / relative).read_text(encoding='utf-8')
            self.assertIn(':::lo-que-cae', output)
            compilar_tema.validate_vigor_blocks(output, relative)


if __name__ == '__main__':
    unittest.main()
