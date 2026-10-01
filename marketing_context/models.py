from __future__ import annotations

from dataclasses import dataclass, field

AUTHORITY_WEIGHTS = {
    "canonical": 100,
    "approved": 80,
    "reference": 50,
    "derived": 20,
}

CURRENT_STATUSES = {"current", "approved", "active"}


@dataclass(frozen=True)
class ContextItem:
    id: str
    domain: str
    kind: str
    authority: str
    status: str
    path: str
    title: str
    tags: tuple[str, ...] = field(default_factory=tuple)
    effective_date: str | None = None
    max_tokens: int | None = None

    @property
    def authority_weight(self) -> int:
        return AUTHORITY_WEIGHTS.get(self.authority, 0)

    @property
    def is_eligible(self) -> bool:
        return self.status in CURRENT_STATUSES


@dataclass(frozen=True)
class TaskSpec:
    id: str
    required_domains: tuple[str, ...]
    optional_domains: tuple[str, ...]
    allowed_kinds: tuple[str, ...]
    context_budget_tokens: int
    per_item_token_limit: int
    minimum_authority: str = "derived"

    @property
    def all_domains(self) -> set[str]:
        return set(self.required_domains) | set(self.optional_domains)


@dataclass
class Candidate:
    item: ContextItem
    text: str
    estimated_tokens: int
    authority_score: int
    relevance_score: float
    required_domain: bool
    total_score: float


@dataclass
class Decision:
    item_id: str
    included: bool
    reason: str
    estimated_tokens: int = 0
    score: float = 0.0
