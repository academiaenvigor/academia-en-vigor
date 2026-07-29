import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'validar_activos_visuales',
    ROOT / 'scripts' / 'validar_activos_visuales.py',
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ActivosVisualesTest(unittest.TestCase):
    def test_manifiestos_y_documentos_estan_sincronizados(self):
        self.assertEqual([], MODULE.validate(ROOT))


if __name__ == '__main__':
    unittest.main()
