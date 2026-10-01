# Example

The example is synthetic and intentionally includes a **superseded campaign file** with language that conflicts with the canonical positioning.

The router should exclude it before model execution.

Run:

```bash
python -m marketing_context build \
  --catalog examples/catalog.json \
  --task-spec examples/task-spec.executive-article.json \
  --task "Write a 600-word executive article for banking CTOs about agent governance" \
  --out .run/example
```

Inspect `.run/example/context.md` and `.run/example/manifest.json`.

The manifest is part of the evidence: it records not only what entered context, but what was excluded and why.
