from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from marketing_context.catalog import load_catalog, load_task_spec, read_item
from marketing_context.router import ContextRouter

TASK = "Write a 600-word executive article for banking CTOs about agent governance."
OUT = ROOT / "benchmark/generated"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    catalog_root, items = load_catalog(ROOT / "examples/catalog.json")
    spec = load_task_spec(ROOT / "examples/task-spec.executive-article.json")
    routed = ContextRouter(catalog_root, items, spec).route(TASK)

    prompt = f"""# Task\n\n{TASK}\n\nUse only information you can support. Do not invent metrics or case evidence.\n"""
    full_dump = "\n\n---\n\n".join(
        f"## {i.title}\nSource-ID: {i.id}\n\n{read_item(catalog_root, i)}" for i in items
    )
    verification = """# Verification before finalizing\n\n1. Do not use superseded sources as authority.\n2. Do not introduce unsupported ROI, speed or superiority claims.\n3. Preserve canonical positioning.\n4. Make the article useful to banking CTOs.\n5. Distinguish observation from recommendation.\n6. Keep the final answer between 500 and 700 words.\n"""

    files = {
        "A-prompt-only.md": prompt,
        "B-full-dump.md": prompt + "\n# Context\n\n" + full_dump,
        "C-routed-context.md": prompt + "\n# Routed context\n\n" + routed["context"],
        "D-routed-plus-verification.md": prompt + "\n# Routed context\n\n" + routed["context"] + "\n\n" + verification,
    }
    for name, content in files.items():
        (OUT / name).write_text(content.strip() + "\n", encoding="utf-8")

    (OUT / "routed-manifest.json").write_text(
        json.dumps({k: v for k, v in routed.items() if k != "context"}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"rendered {len(files)} conditions in {OUT}")


if __name__ == "__main__":
    main()
