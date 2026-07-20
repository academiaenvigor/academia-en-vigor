
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MaterialesYDerechos(unittest.TestCase):
    def test_materials(self):
        subprocess.run([sys.executable, 'scripts/validar_materiales.py'], cwd=ROOT, check=True)

    def test_rights(self):
        subprocess.run([sys.executable, 'scripts/validar_derechos.py'], cwd=ROOT, check=True)


if __name__ == '__main__':
    unittest.main()
