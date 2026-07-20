
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CrearTema(unittest.TestCase):
    def test_help(self):
        subprocess.run([sys.executable, 'scripts/crear_tema.py', '--help'], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)

    def test_project_index_has_official_bank(self):
        data = json.loads((ROOT / 'temario.json').read_text(encoding='utf-8'))
        self.assertEqual(data['official_exam_banks']['policia-nacional']['questions'], 1000)


if __name__ == '__main__':
    unittest.main()
