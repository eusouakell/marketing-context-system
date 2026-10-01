from __future__ import annotations

import argparse
import json
from pathlib import Path

from .catalog import load_catalog, load_task_spec
from .router import ContextRouter


def build_command(args: argparse.Namespace) -> int:
    root, items = load_catalog(args.catalog)
    spec = load_task_spec(args.task_spec)
    result = ContextRouter(root, items, spec).route(args.task)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "context.md").write_text(result["context"] + "\n", encoding="utf-8")
    (out / "manifest.json").write_text(
        json.dumps({k: v for k, v in result.items() if k != "context"}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {out / 'context.md'}")
    print(f"wrote {out / 'manifest.json'}")
    print(f"context tokens (estimated): {result['budget']['used_tokens']}/{result['budget']['limit_tokens']}")
    return 0


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="marketing-context")
    sub = parser.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build", help="build a task-specific context bundle")
    build.add_argument("--catalog", required=True)
    build.add_argument("--task-spec", required=True)
    build.add_argument("--task", required=True)
    build.add_argument("--out", required=True)
    build.set_defaults(func=build_command)
    return parser


def main() -> int:
    parser = make_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
