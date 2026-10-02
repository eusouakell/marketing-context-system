from __future__ import annotations

from .checks import missing_required_domains
from .models import Candidate, Decision, TaskSpec


def route_sensor_snapshot(
    spec: TaskSpec,
    selected: list[Candidate],
    decisions: list[Decision],
    used_tokens: int,
) -> dict:
    """Expose route health as inspectable observations, not hidden scoring."""
    missing = missing_required_domains(spec, selected)
    total_required = len(spec.required_domains)
    present_required = total_required - len(missing)
    limit = spec.context_budget_tokens

    return {
        "selected_items": len(selected),
        "excluded_items": sum(1 for decision in decisions if not decision.included),
        "required_domain_coverage": {
            "present": present_required,
            "total": total_required,
            "missing": missing,
        },
        "budget_utilization": round(used_tokens / limit, 4) if limit else 0.0,
    }
