
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ExamenesOficiales(unittest.TestCase):
    def test_validator(self):
        subprocess.run([sys.executable, 'scripts/validar_examenes_oficiales.py'], cwd=ROOT, check=True)


if __name__ == '__main__':
    unittest.main()
