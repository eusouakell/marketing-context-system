import unittest
from dataclasses import replace
from pathlib import Path

from marketing_context.catalog import load_catalog, load_task_spec, read_item
from marketing_context.models import ContextItem
from marketing_context.router import ContextRouter
from marketing_context.utils import compress_extractively, estimate_tokens

ROOT = Path(__file__).resolve().parents[1]


class RouterTests(unittest.TestCase):
    def setUp(self):
        root, items = load_catalog(ROOT / "examples/catalog.json")
        spec = load_task_spec(ROOT / "examples/task-spec.executive-article.json")
        self.router = ContextRouter(root, items, spec)

    def test_superseded_source_is_excluded(self):
        result = self.router.route("Write an executive article about agent governance for banking CTOs")
        selected = {x["id"] for x in result["selected"]}
        self.assertNotIn("brand.old-campaign", selected)
        reasons = {d["item_id"]: d["reason"] for d in result["decisions"] if not d["included"]}
        self.assertIn("status=superseded", reasons["brand.old-campaign"])

    def test_required_domains_are_selected(self):
        result = self.router.route("Write an executive article about agent governance for banking CTOs")
        domains = {x["domain"] for x in result["selected"]}
        self.assertTrue({"brand", "audience", "evidence", "content"}.issubset(domains))

    def test_budget_is_respected(self):
        result = self.router.route("Write an executive article about agent governance for banking CTOs")
        self.assertLessEqual(result["budget"]["used_tokens"], result["budget"]["limit_tokens"])

    def test_manifest_explains_selection(self):
        result = self.router.route("Write an executive article about agent governance for banking CTOs")
        included = [d for d in result["decisions"] if d["included"]]
        self.assertGreaterEqual(len(included), 4)
        self.assertTrue(all(d["reason"] for d in included))

    def test_sensor_snapshot_reports_route_health(self):
        result = self.router.route("Write an executive article about agent governance for banking CTOs")
        sensors = result["sensors"]
        self.assertEqual(sensors["selected_items"], len(result["selected"]))
        self.assertEqual(
            sensors["required_domain_coverage"]["missing"],
            result["missing_required_domains"],
        )
        self.assertGreaterEqual(sensors["budget_utilization"], 0)
        self.assertLessEqual(sensors["budget_utilization"], 1)

    def test_manifest_exposes_four_part_harness(self):
        result = self.router.route("Write an executive article about agent governance for banking CTOs")
        self.assertEqual(
            set(result["harness"]),
            {"guides", "guards", "sensors", "checks"},
        )
        self.assertEqual(result["harness"]["guides"]["task_spec"], self.router.spec.id)
        self.assertIn("context-budget", result["harness"]["guards"]["applied"])
        self.assertEqual(
            result["harness"]["sensors"]["selected_items"],
            len(result["selected"]),
        )
        checks = {check["id"]: check for check in result["harness"]["checks"]}
        self.assertTrue(checks["context-budget-respected"]["passed"])
        self.assertTrue(checks["required-domains-present"]["passed"])

    def test_required_domain_check_fails_when_budget_prevents_selection(self):
        router = ContextRouter(
            self.router.catalog_root,
            self.router.items,
            replace(self.router.spec, context_budget_tokens=0),
        )
        result = router.route("agent governance")
        checks = {check["id"]: check for check in result["harness"]["checks"]}
        self.assertFalse(checks["required-domains-present"]["passed"])
        self.assertEqual(
            set(result["harness"]["sensors"]["missing_required_domains"]),
            set(router.spec.required_domains),
        )

    def test_rendered_bundle_budget_includes_metadata(self):
        for limit in (0, 25, 100, 300, 500):
            router = ContextRouter(
                self.router.catalog_root,
                self.router.items,
                replace(self.router.spec, context_budget_tokens=limit),
            )
            result = router.route("agent governance")
            self.assertEqual(estimate_tokens(result["context"]), result["budget"]["used_tokens"])
            self.assertLessEqual(estimate_tokens(result["context"]), limit)
            if limit == 0:
                self.assertEqual(
                    set(result["missing_required_domains"]),
                    set(router.spec.required_domains),
                )

    def test_compression_respects_small_limits(self):
        for limit in (0, 1, 5, 25, 100):
            text, _ = compress_extractively("Long source text. " * 100, limit)
            self.assertLessEqual(estimate_tokens(text), limit)

    def test_catalog_cannot_read_outside_its_root(self):
        item = replace(self.router.items[0], path="../../README.md")
        with self.assertRaises(ValueError):
            read_item(self.router.catalog_root, item)

    def test_negative_budget_is_rejected(self):
        with self.assertRaises(ValueError):
            ContextRouter(
                self.router.catalog_root,
                self.router.items,
                replace(self.router.spec, context_budget_tokens=-1),
            )

    def test_required_and_optional_domains_cannot_overlap(self):
        with self.assertRaises(ValueError):
            ContextRouter(
                self.router.catalog_root,
                self.router.items,
                replace(
                    self.router.spec,
                    optional_domains=(
                        *self.router.spec.optional_domains,
                        self.router.spec.required_domains[0],
                    ),
                ),
            )


if __name__ == "__main__":
    unittest.main()
