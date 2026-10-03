from __future__ import annotations

from .models import AUTHORITY_WEIGHTS, Candidate, ContextItem, TaskSpec


def candidate_exclusion_reason(item: ContextItem, spec: TaskSpec) -> str | None:
    """Return the deterministic reason an item cannot enter candidate ranking."""
    if not item.is_eligible:
        return f"status={item.status} is not eligible"
    if item.domain not in spec.all_domains:
        return f"domain={item.domain} is outside task scope"
    if item.kind not in spec.allowed_kinds:
        return f"kind={item.kind} is not allowed"

    minimum_weight = AUTHORITY_WEIGHTS.get(spec.minimum_authority, 0)
    if item.authority_weight < minimum_weight:
        return f"authority={item.authority} below minimum"
    return None


def missing_required_domains(spec: TaskSpec, selected: list[Candidate]) -> list[str]:
    present = {candidate.item.domain for candidate in selected}
    return sorted(set(spec.required_domains) - present)
