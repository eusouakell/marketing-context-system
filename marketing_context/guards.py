from __future__ import annotations

from pathlib import Path

from .models import AUTHORITY_WEIGHTS, ContextItem, TaskSpec


def validate_task_spec(spec: TaskSpec) -> None:
    """Fail fast on task-spec states that should never reach routing."""
    if spec.context_budget_tokens < 0 or spec.per_item_token_limit < 0:
        raise ValueError("context budgets must be non-negative")

    overlap = set(spec.required_domains) & set(spec.optional_domains)
    if overlap:
        joined = ", ".join(sorted(overlap))
        raise ValueError(f"domains cannot be both required and optional: {joined}")

    if spec.minimum_authority not in AUTHORITY_WEIGHTS:
        raise ValueError(f"unknown minimum authority: {spec.minimum_authority}")


def resolve_catalog_path(root: Path, item: ContextItem) -> Path:
    """Keep catalog reads inside the declared catalog root."""
    resolved_root = root.resolve()
    target = (resolved_root / item.path).resolve()
    if not target.is_relative_to(resolved_root):
        raise ValueError("context path must stay inside the catalog root")
    return target
