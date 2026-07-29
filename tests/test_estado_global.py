import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class EstadoGlobalTest(unittest.TestCase):
    def manifests(self):
        for number in range(1, 10):
            path = (
                ROOT
                / f'conocimiento/policia-nacional/tema-{number:02d}/manifest.json'
            )
            yield number, json.loads(path.read_text(encoding='utf-8'))

    def test_toda_cobertura_declara_sus_bloques(self):
        for number, manifest in self.manifests():
            coverage = json.loads(
                (ROOT / manifest['coverage_file']).read_text(encoding='utf-8')
            )
            self.assertEqual(
                manifest['semantic_blocks'],
                len(coverage.get('blocks', [])),
                f'Tema {number}',
            )

    def test_temas_aprobados_tienen_evaluacion_lista(self):
        for number, manifest in self.manifests():
            if manifest['editorial_status'] != 'approved_internal':
                continue
            plan = json.loads(
                (ROOT / manifest['evaluations']['plan']).read_text(encoding='utf-8')
            )
            bank = json.loads(
                (ROOT / manifest['question_bank']['manifest']).read_text(
                    encoding='utf-8'
                )
            )
            self.assertEqual('ready', plan['status'], f'Tema {number}')
            self.assertEqual(
                'ready_after_editorial_approval',
                bank['publication_gate'],
                f'Tema {number}',
            )

    def test_atestado_08_es_sustancialmente_mas_profundo(self):
        manifest = dict(self.manifests())[8]
        parte = (ROOT / manifest['outputs']['parte']).read_text(encoding='utf-8')
        atestado = (ROOT / manifest['outputs']['atestado']).read_text(encoding='utf-8')
        parte_words = len(re.findall(r'\b\w+\b', parte))
        atestado_words = len(re.findall(r'\b\w+\b', atestado))
        self.assertGreaterEqual(atestado_words, int(parte_words * 1.30))
        self.assertEqual(28, atestado.count(':::trampa'))


if __name__ == '__main__':
    unittest.main()
