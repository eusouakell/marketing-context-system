import json
import unittest
from pathlib import Path

from agents.validate_registry import validate_registry

ROOT = Path(__file__).resolve().parents[1]


class AgentRegistryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "agents" / "registry.json").read_text(encoding="utf-8"))

    def test_registry_is_valid(self):
        self.assertEqual(validate_registry(self.data, ROOT), [])

    def test_agent_ids_are_unique(self):
        ids = [agent["id"] for agent in self.data["agents"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_pilot_agents_are_disabled_by_default(self):
        for agent in self.data["agents"]:
            if agent["status"] == "pilot":
                self.assertFalse(agent["enabled_by_default"])

    def test_no_agent_has_direct_main_or_publish_authority(self):
        forbidden = {"main", "publish", "production"}
        self.assertTrue(all(agent["write_authority"] not in forbidden for agent in self.data["agents"]))

    def test_every_agent_has_a_matching_contract(self):
        for agent in self.data["agents"]:
            expected = ROOT / "agents" / "contracts" / f"{agent['id']}.md"
            self.assertEqual(agent["contract"], str(expected.relative_to(ROOT)))
            self.assertTrue(expected.is_file())


if __name__ == "__main__":
    unittest.main()
