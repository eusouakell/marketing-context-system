# Marketing Context System

**A context operating system for AI-native marketing work.**

This project is the implementation-oriented companion to [context-engineering-for-marketing](https://github.com/eusouakell/context-engineering-for-marketing).

It provides a reusable structure for organizing marketing knowledge, routing context to agents, applying task skills and verifying outputs.

## Design goal

Make AI-assisted marketing:

- more consistent;
- less dependent on chat memory;
- traceable to sources;
- resistant to stale context;
- explicit about human decisions;
- measurable through evals.

## System

```text
CANONICAL KNOWLEDGE
        ↓
BOUNDED CONTEXTS
        ↓
CONTEXT ROUTER
        ↓
TASK SKILL
        ↓
AGENT
        ↓
DETERMINISTIC CHECKS
        ↓
SEMANTIC EVALS
        ↓
HUMAN GATES
        ↓
ARTIFACT
```

## Knowledge hierarchy

```text
SPEC
→ CONCEPTS
→ DECISIONS + EVIDENCE
→ VIEWS
→ APPLICATIONS
```

This is an initial documentation scaffold. The context domains below are a proposed structure; their canonical knowledge files and executable router/checks are not included in this release. See the [context-domain index](contexts/README.md).

## Repository

```text
SYSTEM-SPEC.md
contexts/
  brand/
  market/
  audience/
  offer/
  content/
  proof/
  go-to-market/
  governance/
harness/
  checks.md
  sensors.md
  gates.md
skills/
  brand-context/
  executive-content/
  competitive-intelligence/
evals/
  brand-consistency.md
  context-ablation.md
examples/
  task-context-bundle.md
```

## Relationship to Marketing Skills

This system was influenced by working with agent-skill collections, including Corey Haines' open-source `marketingskills` project.

The distinction is intentional:

- **task skill**: how to perform a marketing task;
- **context system**: what the agent should know, trust and load before the task;
- **harness**: how the result is checked and whether it may progress.

This repository does not claim authorship of upstream Marketing Skills content.

See [NOTICE.md](NOTICE.md).

## Inspect the scaffold

Start with [the system spec](SYSTEM-SPEC.md), follow [the worked task-context bundle](examples/task-context-bundle.md), then inspect [checks](harness/checks.md), [sensors](harness/sensors.md), [human gates](harness/gates.md) and [semantic evaluation](evals/brand-consistency.md).

The workflow is **RESEARCH → PLAN → IMPLEMENT → VERIFY**. The [ablation protocol](evals/context-ablation.md) describes how to test the architecture; measured results are not yet published.
