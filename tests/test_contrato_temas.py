from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ContratoTemas(unittest.TestCase):
    def test_temas_registrados_superan_el_contrato_universal(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/validar_temas.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_derivados_se_pueden_recompilar_sin_cambios(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/compilar_tema.py"), "--all", "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
