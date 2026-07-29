"""`temario.json` es un índice derivado y no puede desviarse de sus fuentes.

Este caso existe porque el desvío ya ocurrió: el Tema 8 llegó a estar
registrado con 0 hechos, 0 preguntas y 0 visuales mientras sus manifiestos
declaraban 199, 389 y 23. Ninguna prueba lo detectaba antes del commit.
"""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SincronizacionTemario(unittest.TestCase):
    def test_el_indice_no_tiene_desvios(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/sincronizar_temario.py"), "--check"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(
            result.returncode, 0,
            "temario.json desincronizado; ejecuta "
            "python scripts/sincronizar_temario.py --write\n\n"
            + result.stdout + result.stderr,
        )

    def test_no_quedan_callouts_antiguos(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/migrar_callouts.py"), "--check"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
