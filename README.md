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
- emits route-health sensors for required-domain coverage and budget usage;
- supports reproducible ablation experiments.

The current ranking logic is intentionally simple. The point of V0.3 is to make the **decision contract and control boundaries** observable before replacing retrieval with more sophisticated infrastructure.

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
GUIDES
        ↓
GUARDS
        ↓
VALIDATE / SELECT / PRIORITIZE / COMPRESS
        ↓
ASSEMBLE
        ↓
SENSORS
        ↓
CHECKS
        ↓
MANIFEST + CONTEXT BUNDLE
        ↓
EVALS / HUMAN GATES when required
```

This repository implements context-specific controls under the canonical [Agentic Factory](https://github.com/eusouakell/agentic-factory). See the [local Factory mapping](AGENTIC-FACTORY.md) for how the generic control model is realized here.

## Core contracts

**Skill** defines how to perform a task.

**Context system** defines what the agent should know, trust and load.

**Harness** surrounds execution with Guides, Guards, Sensors and Checks.

**Guides** instruct. **Guards** block invalid runtime states. **Sensors** observe. **Checks** make deterministic validations.

Semantic evals and human gates remain separate because they answer different questions.

## What this implementation is not

It is not a production retrieval platform.

It is not evidence that keyword overlap is sufficient for retrieval.

It does not call an LLM by itself.

It does not enforce publishing approval.

It does not claim model-quality improvement before the evaluation exists.

The scoring algorithm is intentionally replaceable so retrieval/ranking can evolve without changing the surrounding context contract.

## Agentic harness

```text
GUIDES + GUARDS
      ↓
TASK / SKILL / AGENT
      ↓
SENSORS
      ↓
CHECKS
```

- **Guides** provide selected context and orientation.
- **Guards** constrain what may proceed.
- **Sensors** expose what happened.
- **Checks** verify observed results against explicit criteria.

The older `evals` and `gates` documents remain as compatibility views; they no longer define separate top-level control classes.

## Inspectable artifacts

Useful entry points:

- [System specification](SYSTEM-SPEC.md)
- [Canonical Agentic Factory](https://github.com/eusouakell/agentic-factory)
- [Local Factory mapping](AGENTIC-FACTORY.md)
- [Guides](guides/README.md)
- [Context domains](contexts/README.md)
- [Harness overview](harness/README.md)
- [Guides](harness/guides.md)
- [Guards](harness/guards.md)
- [Sensors](harness/sensors.md)
- [Checks](harness/checks.md)
- [Example task bundle](examples/task-context-bundle.md)
- [Synthetic benchmark pilot](benchmark/synthetic-marketing-pilot/README.md)

## Current status

V0.3 has executable routing, tests, manifests, runtime guards, deterministic candidate checks, route sensors and a reproducible synthetic pilot structure.

The four-part harness is this repository's implementation of the canonical Factory control taxonomy. Semantic evals and human approval remain downstream controls under validation. Exact model-token accounting and model-quality evaluation remain separate work.

Token counts currently use a character-based approximation including rendered source headers. Missing required domains are reported in the manifest. Catalog paths are constrained to the catalog root.

Workflow: **RESEARCH → PLAN → IMPLEMENT → VERIFY**.

## Provenance and licensing

See [NOTICE.md](NOTICE.md) for upstream attribution.

This repository mixes executable code, skills, examples and original methodology, so it intentionally does **not** use one blanket license yet. [LICENSING.md](LICENSING.md) records the asset boundaries and decisions required before open-sourcing individual parts.
