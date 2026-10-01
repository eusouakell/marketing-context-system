import copy
import json
from pathlib import Path
import unittest
from run import prepare

ROOT = Path(__file__).resolve().parent


class PilotTests(unittest.TestCase):
    def setUp(self):
        self.corpus = json.loads((ROOT / "corpus.json").read_text(encoding="utf-8"))
        self.brief = json.loads((ROOT / "brief.json").read_text(encoding="utf-8"))

    def run_pilot(self, corpus=None, brief=None, encode=None):
        return prepare(corpus or self.corpus, brief or self.brief, encode or (lambda text: list(text.split())))

    def test_manifest_sources_and_exclusions(self):
        report = self.run_pilot()
        self.assertEqual([i["id"] for i in report["selected"]], ["brand", "audience", "editorial-policy"])
        self.assertTrue(all(i["reason"] for i in report["selected"]))
        self.assertEqual(report["excluded"], [{"id": "old-campaign", "reason": "superseded"}])

    def test_synthetic_evidence_boundary(self):
        self.assertTrue(self.brief["synthetic"])
        self.assertTrue(all(i["synthetic"] for i in self.corpus["items"]))
        self.assertEqual(self.brief["external_evidence"], [])
        self.brief["external_evidence"] = ["brand"]
        with self.assertRaises(ValueError): self.run_pilot()

    def test_unsupported_claim(self):
        self.assertEqual(self.brief["unsupported_claims"], ["Usar IA dobra o ROI"])
        self.brief["unsupported_claims"] = []
        with self.assertRaises(ValueError): self.run_pilot()

    def test_human_gate(self):
        self.assertEqual(self.brief["publication_status"], "HOLD")
        self.assertIsNone(self.brief["human_approval"])
        self.brief["publication_status"] = "READY"
        with self.assertRaises(ValueError): self.run_pilot()

    def test_missing_source(self):
        self.corpus["items"] = []
        with self.assertRaises(KeyError): self.run_pilot()

    def test_budget_and_report(self):
        report = self.run_pilot(encode=lambda text: [0] * 1500)["token_report"]
        self.assertEqual(report["selected_knowledge_tokens"], 1500)
        self.assertEqual(report["encoding"], "o200k_base")
        self.assertEqual(report["budget_tokens"], 1500)
        self.assertTrue(report["within_budget"])
        self.assertEqual(report["skill_instruction_tokens"], 3783)
        self.assertIsNone(report["session_total_tokens"])
        with self.assertRaises(ValueError): self.run_pilot(encode=lambda text: [0] * 1501)

    def test_section_traceability(self):
        self.brief["outline"][0]["source_ids"] = ["invented"]
        with self.assertRaises(ValueError): self.run_pilot()


if __name__ == "__main__":
    unittest.main()
