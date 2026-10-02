from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from .catalog import read_item
from .models import AUTHORITY_WEIGHTS, Candidate, ContextItem, Decision, TaskSpec
from .utils import compress_extractively, estimate_tokens, keyword_relevance


class ContextRouter:
    def __init__(self, catalog_root: Path, items: list[ContextItem], spec: TaskSpec):
        self.catalog_root = catalog_root
        self.items = items
        self.spec = spec
        if spec.context_budget_tokens < 0 or spec.per_item_token_limit < 0:
            raise ValueError("context budgets must be non-negative")

    @staticmethod
    def render_candidate(cand: Candidate) -> str:
        return (f"## {cand.item.title}\nSource-ID: {cand.item.id}\n"
                f"Domain: {cand.item.domain}\nAuthority: {cand.item.authority}\n\n"
                f"{cand.text.strip()}")

    def selection_cost(self, selected: list[Candidate], cand: Candidate) -> int:
        before = "\n\n---\n\n".join(self.render_candidate(c) for c in selected)
        after = "\n\n---\n\n".join(self.render_candidate(c) for c in [*selected, cand])
        return estimate_tokens(after) - estimate_tokens(before)

    def _minimum_weight(self) -> int:
        return AUTHORITY_WEIGHTS.get(self.spec.minimum_authority, 0)

    def candidates(self, task: str) -> tuple[list[Candidate], list[Decision]]:
        candidates: list[Candidate] = []
        decisions: list[Decision] = []

        for item in self.items:
            if not item.is_eligible:
                decisions.append(Decision(item.id, False, f"status={item.status} is not eligible"))
                continue
            if item.domain not in self.spec.all_domains:
                decisions.append(Decision(item.id, False, f"domain={item.domain} is outside task scope"))
                continue
            if item.kind not in self.spec.allowed_kinds:
                decisions.append(Decision(item.id, False, f"kind={item.kind} is not allowed"))
                continue
            if item.authority_weight < self._minimum_weight():
                decisions.append(Decision(item.id, False, f"authority={item.authority} below minimum"))
                continue

            text = read_item(self.catalog_root, item)
            limit = min(
                self.spec.per_item_token_limit,
                item.max_tokens if item.max_tokens is not None else self.spec.per_item_token_limit,
            )
            compressed, _ = compress_extractively(text, limit)
            tokens = estimate_tokens(compressed)
            relevance = keyword_relevance(task, item.title, item.tags, compressed)
            required = item.domain in self.spec.required_domains
            total = item.authority_weight + (30 if required else 0) + relevance * 20

            candidates.append(
                Candidate(
                    item=item,
                    text=compressed,
                    estimated_tokens=tokens,
                    authority_score=item.authority_weight,
                    relevance_score=relevance,
                    required_domain=required,
                    total_score=total,
                )
            )
        return candidates, decisions

    def _harness_report(
        self,
        *,
        selected: list[Candidate],
        decisions: list[Decision],
        used_tokens: int,
        missing_required_domains: list[str],
    ) -> dict:
        excluded = [decision for decision in decisions if not decision.included]
        limit = self.spec.context_budget_tokens
        utilization = 0.0 if limit == 0 else round(used_tokens / limit, 4)

        return {
            "guides": {
                "task_spec": self.spec.id,
                "required_domains": list(self.spec.required_domains),
                "optional_domains": list(self.spec.optional_domains),
                "selection_policy": "authority + task relevance + required-domain priority + context budget",
            },
            "guards": {
                "applied": [
                    "eligible-source-state",
                    "task-domain-scope",
                    "allowed-kind",
                    "minimum-authority",
                    "context-budget",
                    "catalog-root-boundary",
                ],
                "blocked_items": sorted({decision.item_id for decision in excluded}),
                "blocked_count": len(excluded),
            },
            "sensors": {
                "selected_items": len(selected),
                "excluded_items": len(excluded),
                "budget_used_tokens": used_tokens,
                "budget_limit_tokens": limit,
                "budget_utilization": utilization,
                "missing_required_domains": missing_required_domains,
            },
            "checks": [
                {
                    "id": "context-budget-respected",
                    "passed": used_tokens <= limit,
                    "observed": used_tokens,
                    "expected": f"<= {limit}",
                },
                {
                    "id": "required-domains-present",
                    "passed": not missing_required_domains,
                    "observed": missing_required_domains,
                    "expected": "[]",
                },
            ],
        }

    def route(self, task: str) -> dict:
        candidates, decisions = self.candidates(task)
        selected: list[Candidate] = []
        budget = self.spec.context_budget_tokens
        remaining = candidates[:]

        # Guard: guarantee the best feasible candidate for each required domain first.
        for domain in self.spec.required_domains:
            domain_candidates = [c for c in remaining if c.item.domain == domain]
            if not domain_candidates:
                continue
            best = sorted(domain_candidates, key=lambda c: (-c.total_score, c.item.id))[0]
            cost = self.selection_cost(selected, best)
            if cost <= budget:
                selected.append(best)
                budget -= cost
            else:
                decisions.append(
                    Decision(
                        best.item.id,
                        False,
                        "required-domain candidate exceeds remaining context budget",
                        best.estimated_tokens,
                        best.total_score,
                    )
                )
            remaining.remove(best)

        # Guard: fill the remaining budget by score without exceeding the configured limit.
        for cand in sorted(remaining, key=lambda c: (-c.total_score, c.item.id)):
            cost = self.selection_cost(selected, cand)
            if cost <= budget:
                selected.append(cand)
                budget -= cost
            else:
                decisions.append(
                    Decision(
                        cand.item.id,
                        False,
                        "context budget exhausted",
                        cand.estimated_tokens,
                        cand.total_score,
                    )
                )

        selected_ids = {c.item.id for c in selected}
        for cand in candidates:
            if cand.item.id in selected_ids:
                decisions.append(
                    Decision(
                        cand.item.id,
                        True,
                        "selected by authority/relevance within context budget",
                        cand.estimated_tokens,
                        cand.total_score,
                    )
                )

        domain_order = {d: i for i, d in enumerate(self.spec.required_domains)}
        selected = sorted(
            selected,
            key=lambda c: (domain_order.get(c.item.domain, 999), -c.total_score, c.item.id),
        )

        context = "\n\n---\n\n".join(self.render_candidate(cand) for cand in selected)
        used = estimate_tokens(context)
        missing_required_domains = sorted(
            set(self.spec.required_domains) - {cand.item.domain for cand in selected}
        )
        sorted_decisions = sorted(decisions, key=lambda decision: (not decision.included, decision.item_id))

        return {
            "task": task,
            "task_spec": self.spec.id,
            "budget": {
                "limit_tokens": self.spec.context_budget_tokens,
                "used_tokens": used,
                "remaining_tokens": self.spec.context_budget_tokens - used,
            },
            "selected": [
                {
                    **asdict(c.item),
                    "estimated_tokens": c.estimated_tokens,
                    "authority_score": c.authority_score,
                    "relevance_score": round(c.relevance_score, 4),
                    "total_score": round(c.total_score, 4),
                }
                for c in selected
            ],
            "missing_required_domains": missing_required_domains,
            "decisions": [asdict(decision) for decision in sorted_decisions],
            "harness": self._harness_report(
                selected=selected,
                decisions=sorted_decisions,
                used_tokens=used,
                missing_required_domains=missing_required_domains,
            ),
            "context": context,
        }
