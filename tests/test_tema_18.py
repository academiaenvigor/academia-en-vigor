import json
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / 'conocimiento/policia-nacional/tema-18/master.md'
TOPIC = ROOT / 'conocimiento/policia-nacional/tema-18'
BANK = ROOT / 'banco-preguntas/policia-nacional/tema-18'
ASSETS = ROOT / 'assets/policia-nacional/tema-18'


class Tema18QualityGate(unittest.TestCase):
    def setUp(self):
        self.coverage = json.loads((TOPIC / 'cobertura.json').read_text(encoding='utf-8'))
        self.questions = [json.loads(line) for line in (BANK / 'preguntas.jsonl').read_text(encoding='utf-8').splitlines() if line]
        self.assets = json.loads((ASSETS / 'manifest.json').read_text(encoding='utf-8'))

    def test_exact_scope_counts(self):
        self.assertEqual(self.coverage['total_atomic_facts'], 124)
        self.assertEqual(len(self.coverage['facts']), 124)
        self.assertEqual(len(self.questions), 248)
        self.assertEqual({f['bloque'] for f in self.coverage['facts']}, set(range(1, 32)))

    def test_question_schema_balance_and_double_feedback(self):
        self.assertEqual(Counter(q['respuesta_correcta'] for q in self.questions), {'A': 83, 'B': 83, 'C': 82})
        self.assertEqual(len({q['id'] for q in self.questions}), 248)
        for q in self.questions:
            self.assertEqual(set(q['opciones']), {'A', 'B', 'C'})
            self.assertEqual(len(set(q['opciones'].values())), 3)
            self.assertIn(q['respuesta_correcta'], q['opciones'])
            self.assertTrue(q['retroalimentacion']['acierto']['explicacion'])
            self.assertTrue(q['retroalimentacion']['fallo']['explicacion'])

    def test_critical_2026_rules_are_explicit(self):
        text = MASTER.read_text(encoding='utf-8')
        self.assertIn('artículo 244.3, y no el 244.2', text)
        self.assertIn('Desde el 10 de abril de 2026', text)
        self.assertIn('teléfonos u otros dispositivos móviles', text)
        self.assertIn('artículo 255.3', text)
        self.assertIn('conductas del artículo 368', text)

    def test_visual_assets_and_compiled_documents(self):
        self.assertEqual(self.assets['totals'], {'resources': 28, 'integrated': 28, 'planned': 0})
        self.assertEqual(Counter(r['type'] for r in self.assets['resources']), {'infografia': 22, 'ilustracion_simple': 6})
        for resource in self.assets['resources']:
            path = ASSETS / resource['file']
            self.assertTrue(path.is_file())
            self.assertLess(path.stat().st_size, 1_000_000)
        parte = next((ROOT / 'temas/policia-nacional/parte').glob('tema-18-*.md')).read_text(encoding='utf-8')
        atestado = next((ROOT / 'temas/policia-nacional/atestado').glob('tema-18-*.md')).read_text(encoding='utf-8')
        self.assertEqual(parte.count('<!-- VISUAL:'), 14)
        self.assertEqual(atestado.count('<!-- VISUAL:'), 28)

    def test_historical_items_remain_quarantined(self):
        index = json.loads((BANK / 'indice-oficiales.json').read_text(encoding='utf-8'))
        self.assertEqual(index['con_respuesta_verificada'], 0)
        self.assertFalse(index['display_policy']['show_reviewed_appearances'])
        for item in index['questions']:
            self.assertFalse(item['counts_for_ha_caido'])
            self.assertIsNone(item['respuesta'])
            self.assertEqual(item['verification_status'], 'quarantine')

    def test_evaluation_catalogue(self):
        catalogue = ROOT / 'build/evaluaciones/policia-nacional/tema-18/tests-generados/catalogo.json'
        data = json.loads(catalogue.read_text(encoding='utf-8'))
        self.assertEqual(data['total_tests'], 43)


if __name__ == '__main__':
    unittest.main()
