# Marketing Context System

**Executable reference implementation for Context Engineering in marketing knowledge work.**

V2 moves this project beyond a documentation scaffold.

It includes a small stdlib-only context router that catalogs available context, excludes invalid/superseded sources, scores authority and relevance, enforces a context budget, selects the task bundle, records included and excluded sources with reasons, renders the assembled context, and supports a reproducible ablation benchmark.

## Quick start

```bash
python -m marketing_context build \
  --catalog examples/catalog.json \
  --task-spec examples/task-spec.executive-article.json \
  --task "Write an executive article about agent governance in banking" \
  --out .run/context-bundle
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

Render the first benchmark conditions:

```bash
python benchmark/render_pilot.py
```

## Architecture

```text
AVAILABLE CONTEXT
        ↓
VALIDATE
        ↓
SELECT
        ↓
PRIORITIZE
        ↓
COMPRESS
        ↓
ISOLATE
        ↓
ASSEMBLE
        ↓
MANIFEST + CONTEXT BUNDLE
```

## What the router is — and is not

It is a reference implementation for making context decisions inspectable.

It is **not** a claim that keyword overlap is sufficient for production retrieval. The scoring algorithm is intentionally simple so the architecture can be tested independently of a vector database or model provider.

Swap retrieval/ranking later without changing the contract.

## Core distinction

- **Skill** — how to perform the task.
- **Context system** — what the agent should know, trust and load.
- **Harness** — how execution is checked and allowed to progress.

## Research companion

See [Context Engineering for Marketing](https://github.com/eusouakell/context-engineering-for-marketing).

## Scope and governance

The router reads a local catalog and builds context; it does not call an LLM or enforce publishing approvals. Semantic evals, sensors and human gates are documented controls. Token counts use a character-based approximation including rendered source headers; use the model tokenizer for exact limits. Missing required domains are reported in the manifest. Catalog paths must remain within the catalog root.

Workflow: **RESEARCH → PLAN → IMPLEMENT → VERIFY**. Existing [system specification](SYSTEM-SPEC.md), [context domains](contexts/README.md) and [upstream attribution](NOTICE.md) remain part of the architecture.


## Licensing status

This repository currently mixes code, skills and original methodology, so it does **not** yet use one blanket license. See [LICENSING.md](LICENSING.md) for the asset boundaries and decisions that must be made before open-sourcing any part of it. Upstream attribution remains documented in [NOTICE.md](NOTICE.md).
