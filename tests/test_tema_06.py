from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPIC_DIR = ROOT / "conocimiento/policia-nacional/tema-06"


class Tema06(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(
            (TOPIC_DIR / "manifest.json").read_text(encoding="utf-8")
        )
        cls.coverage = json.loads(
            (TOPIC_DIR / "cobertura.json").read_text(encoding="utf-8")
        )
        cls.master = (ROOT / cls.manifest["source_file"]).read_text(encoding="utf-8")
        cls.parte = (ROOT / cls.manifest["outputs"]["parte"]).read_text(encoding="utf-8")
        cls.atestado = (ROOT / cls.manifest["outputs"]["atestado"]).read_text(
            encoding="utf-8"
        )

    def test_official_scope_and_structure(self) -> None:
        self.assertEqual(self.manifest["content_version"], "1.0.1")
        self.assertEqual(
            self.manifest["editorial_status"],
            "ready_for_user_approval",
        )
        self.assertEqual(
            self.manifest["title"],
            "Los funcionarios públicos: concepto y clases. "
            "Adquisición y pérdida de la condición de funcionario",
        )
        self.assertEqual(self.manifest["semantic_blocks"], 14)
        self.assertEqual(self.master.count("<!-- BLOCK "), 28)
        for heading in (
            "situaciones administrativas",
            "carrera profesional",
            "movilidad",
            "retribuciones",
            "código de conducta",
        ):
            self.assertNotRegex(
                self.parte.lower(),
                rf"(?m)^##\s+\d+\.\s+.*{re.escape(heading)}",
            )
            self.assertNotRegex(
                self.atestado.lower(),
                rf"(?m)^##\s+\d+\.\s+.*{re.escape(heading)}",
            )

    def test_atomic_fact_traceability(self) -> None:
        facts = self.coverage["facts"]
        expected_ids = {f"PN-T06-F{i:03d}" for i in range(1, 95)}
        actual_ids = {fact["id"] for fact in facts}
        self.assertEqual(self.manifest["atomic_facts"], 94)
        self.assertEqual(actual_ids, expected_ids)
        self.assertEqual(self.master.count("<!-- FACT:PN-T06-F"), 94)
        self.assertEqual(self.atestado.count("<!-- FACT:PN-T06-F"), 94)
        self.assertEqual(self.parte.count("<!-- FACT:PN-T06-F"), 0)
        for fact_id in expected_ids:
            self.assertEqual(
                self.master.count(f"<!-- FACT:{fact_id} -->"),
                1,
                fact_id,
            )
            self.assertEqual(
                self.atestado.count(f"<!-- FACT:{fact_id} -->"),
                1,
                fact_id,
            )

    def test_current_high_risk_rules_are_explicit(self) -> None:
        text = self.atestado.lower()
        for fragment in (
            "nueve meses dentro de un periodo de dieciocho meses",
            "veinte días de retribuciones fijas por año de servicio",
            "no aparece como quinta clase",
            "tomar posesión dentro del plazo",
            "pérdida de la nacionalidad española",
            "dirección adjunta operativa",
            "silencio desestimatorio",
        ):
            self.assertIn(fragment, text)

    def test_question_generation_remains_blocked(self) -> None:
        bank_path = ROOT / self.manifest["question_bank"]["path"]
        bank_manifest = json.loads(
            (ROOT / self.manifest["question_bank"]["manifest"]).read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(bank_path.read_text(encoding="utf-8").strip(), "")
        self.assertEqual(bank_manifest["total_preguntas"], 0)
        self.assertEqual(
            bank_manifest["quality_gate"]["status"],
            "blocked",
        )

    def test_official_appearances_are_not_presented_as_official_answers(self) -> None:
        index = json.loads(
            (ROOT / self.manifest["official_exam_index"]).read_text(encoding="utf-8")
        )
        self.assertEqual(index["total_referencias"], 15)
        self.assertEqual(index["con_bloque_asignado"], 15)
        self.assertEqual(index["con_respuesta_verificada"], 15)
        self.assertEqual(sum(index["por_promocion"].values()), 15)
        self.assertEqual(
            sum(index["por_bloque"].values()),
            sum(len(item["block_refs"]) for item in index["questions"]),
        )
        self.assertEqual(
            index["retroalimentacion"],
            "banco-preguntas/policia-nacional/oficiales/retroalimentacion.json",
        )
        self.assertFalse(index["display_policy"]["show_answer"])
        self.assertTrue(index["display_policy"]["never_present_as_official_plantilla"])
        self.assertEqual(
            sum(
                item["rule_status_2026"] == "historical_rule_changed"
                for item in index["questions"]
            ),
            3,
        )

    def test_visual_assets_are_integrated(self) -> None:
        visual = json.loads(
            (ROOT / self.manifest["assets"]["manifest"]).read_text(encoding="utf-8")
        )
        self.assertEqual(visual["totals"], {"resources": 11, "integrated": 11, "planned": 0})
        self.assertEqual(visual["integration_status"], "complete")
        self.assertEqual(len(visual["resources"]), 11)
        for resource in visual["resources"]:
            path = ROOT / "assets/policia-nacional/tema-06" / resource["file"]
            self.assertTrue(path.exists(), resource["file"])
            self.assertGreater(path.stat().st_size, 50_000, resource["file"])
            ref = f"../../../assets/policia-nacional/tema-06/{resource['file']}"
            self.assertIn(ref, self.parte)
            self.assertIn(ref, self.atestado)

    def test_structural_homologation_1_0_1(self) -> None:
        teaching = json.loads(
            (ROOT / self.manifest["teaching_materials"]["manifest"]).read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(teaching["schema_version"], "2.1.0")
        self.assertEqual(teaching["content_version"], "1.0.1")
        self.assertEqual(teaching["source_version"], "1.0.1")
        self.assertEqual(len(teaching["parts"]), 5)
        self.assertEqual(len(teaching["resources"]), 24)
        self.assertEqual(
            sorted(
                {
                    block
                    for part in teaching["parts"]
                    for block in part["blocks"]
                }
            ),
            [f"{number:02d}" for number in range(1, 15)],
        )
        self.assertTrue(
            all(resource["status"] == "planned" for resource in teaching["resources"])
        )

        temario = json.loads((ROOT / "temario.json").read_text(encoding="utf-8"))
        topic = next(
            item
            for item in temario["oppositions"]["policia-nacional"]["topics"]
            if item["number"] == 6
        )
        self.assertEqual(topic["content_version"], "1.0.1")
        self.assertEqual(topic["visual_version"], "1.0.0")
        self.assertEqual(topic["visual_assets"], 11)

        catalog = json.loads(
            (ROOT / "fuentes/catalogo.json").read_text(encoding="utf-8")
        )
        self.assertEqual(catalog["catalog_version"], "1.0.0")
        source_ids = {source["id"] for source in catalog["sources"]}
        self.assertTrue(set(self.manifest["official_references"]) <= source_ids)

    def test_no_third_party_binary_is_packaged(self) -> None:
        forbidden = {".doc", ".docx", ".pdf", ".odt"}
        topic_paths = [
            TOPIC_DIR,
            ROOT / "temas/policia-nacional/parte",
            ROOT / "temas/policia-nacional/atestado",
            ROOT / "banco-preguntas/policia-nacional/tema-06",
            ROOT / "assets/policia-nacional/tema-06",
            ROOT / "materiales-didacticos/policia-nacional/tema-06",
        ]
        for path in topic_paths:
            candidates = path.rglob("*") if path.is_dir() else [path]
            self.assertFalse(
                any(item.is_file() and item.suffix.lower() in forbidden for item in candidates)
            )


if __name__ == "__main__":
    unittest.main()
