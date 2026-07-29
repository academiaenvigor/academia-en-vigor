import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExploradorAntecedentesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.explorer = (ROOT / 'explorador.html').read_text(encoding='utf-8')

    def test_admite_el_estado_editorialmente_mapeado(self):
        self.assertIn("'editorially_mapped'", self.explorer)

    def test_respeta_la_politica_de_respuesta_y_retroalimentacion(self):
        self.assertIn('politica.show_answer===true', self.explorer)
        self.assertIn('politica.show_feedback===true', self.explorer)
        self.assertIn('details.dataset.policy', self.explorer)

    def test_las_propuestas_automaticas_no_se_publican(self):
        for path in sorted(
            (ROOT / 'banco-preguntas/policia-nacional').glob(
                'tema-*/indice-oficiales.json'
            )
        ):
            data = json.loads(path.read_text(encoding='utf-8'))
            has_auto = any(
                item.get('appearance_status') == 'auto_proposed'
                for item in data.get('questions', [])
            )
            if has_auto:
                self.assertFalse(
                    data.get('display_policy', {}).get('show_auto_proposed'),
                    path.as_posix(),
                )


if __name__ == '__main__':
    unittest.main()
