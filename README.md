# Marketing Context System

**Executable reference implementation for Context Engineering in marketing knowledge work.**

This repository turns the research ideas from [Context Engineering for Marketing](https://github.com/eusouakell/context-engineering-for-marketing) into an inspectable runtime system.

It answers a concrete question:

> Given all available context, what should this task receive, what should be excluded, and why?

## What it does

The router:

- catalogs available context;
- rejects invalid or superseded sources;
- scores authority and task relevance;
- enforces a context budget;
- selects a task-specific bundle;
- records included and excluded sources with reasons;
- renders the assembled context;
- produces a manifest that can be inspected later;
- supports reproducible ablation experiments.

The current ranking logic is intentionally simple. The point of V0.2 is to make the **decision contract** observable before replacing retrieval with more sophisticated infrastructure.

## Quick start

```bash
python -m marketing_context build \
  --catalog examples/catalog.json \
  --task-spec examples/task-spec.executive-article.json \
  --task "Write an executive article about agent governance in banking" \
  --out .run/context-bundle
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

Render the prepared benchmark conditions:

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

## Core contracts

**Skill** defines how to perform a task.

**Context system** defines what the agent should know, trust and load.

**Harness** checks execution and determines whether work may progress.

Those responsibilities are deliberately separate.

## What this implementation is not

It is not a production retrieval platform.

It is not evidence that keyword overlap is sufficient for retrieval.

It does not call an LLM by itself.

It does not enforce publishing approval.

It does not claim model-quality improvement before the evaluation exists.

The scoring algorithm is intentionally replaceable so retrieval/ranking can evolve without changing the surrounding context contract.

## Inspectable artifacts

Useful entry points:

- [System specification](SYSTEM-SPEC.md)
- [Context domains](contexts/README.md)
- [Harness checks](harness/checks.md)
- [Evals](harness/evals.md)
- [Gates](harness/gates.md)
- [Example task bundle](examples/task-context-bundle.md)
- [Synthetic benchmark pilot](benchmark/synthetic-marketing-pilot/README.md)

## Current status

V0.2 has executable routing, tests, manifests and a reproducible synthetic pilot structure.

Semantic evals, sensors and human gates are documented controls. Exact model-token accounting and model-quality evaluation remain separate work.

Token counts currently use a character-based approximation including rendered source headers. Missing required domains are reported in the manifest. Catalog paths are constrained to the catalog root.

Workflow: **RESEARCH → PLAN → IMPLEMENT → VERIFY**.

## Provenance and licensing

See [NOTICE.md](NOTICE.md) for upstream attribution.

This repository mixes executable code, skills, examples and original methodology, so it intentionally does **not** use one blanket license yet. [LICENSING.md](LICENSING.md) records the asset boundaries and decisions required before open-sourcing individual parts.
