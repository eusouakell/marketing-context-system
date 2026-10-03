from __future__ import annotations

import json
from pathlib import Path

from .guards import resolve_catalog_path
from .models import ContextItem, TaskSpec


def load_catalog(path: str | Path) -> tuple[Path, list[ContextItem]]:
    p = Path(path)
    data = json.loads(p.read_text(encoding="utf-8"))
    root = p.parent
    items = []
    for raw in data["items"]:
        items.append(
            ContextItem(
                id=raw["id"],
                domain=raw["domain"],
                kind=raw["kind"],
                authority=raw["authority"],
                status=raw["status"],
                path=raw["path"],
                title=raw["title"],
                tags=tuple(raw.get("tags", [])),
                effective_date=raw.get("effective_date"),
                max_tokens=raw.get("max_tokens"),
            )
        )
    return root, items


def load_task_spec(path: str | Path) -> TaskSpec:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return TaskSpec(
        id=data["id"],
        required_domains=tuple(data["required_domains"]),
        optional_domains=tuple(data.get("optional_domains", [])),
        allowed_kinds=tuple(data["allowed_kinds"]),
        context_budget_tokens=int(data["context_budget_tokens"]),
        per_item_token_limit=int(data["per_item_token_limit"]),
        minimum_authority=data.get("minimum_authority", "derived"),
    )


def read_item(root: Path, item: ContextItem) -> str:
    return resolve_catalog_path(root, item).read_text(encoding="utf-8")
