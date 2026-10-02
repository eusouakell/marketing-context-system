# Agentic harness

This directory defines the operating harness around the Marketing Context System.

It uses four control classes:

| | Feedforward | Feedback |
|---|---|---|
| **Descriptive** | [Guides](guides.md) | [Sensors](sensors.md) |
| **Normative** | [Guards](guards.md) | [Checks](checks.md) |

The model is intentionally about **responsibility**, not file format.

A Markdown file can be a Guide. A JSON Schema can be a Guard. A manifest can be a Sensor. A unit test or semantic grader can be a Check.

## Runtime relationship

```text
KNOWLEDGE AUTHORITY
        ↓
CONTEXT ROUTER
        ↓
GUIDES + GUARDS
        ↓
TASK / SKILL / AGENT
        ↓
SENSORS
        ↓
CHECKS
        ↓
HUMAN DECISION WHEN REQUIRED
```

## Status vocabulary

Every harness mechanism should be labeled with one of:

- **documented** — contract exists;
- **implemented** — executable mechanism exists;
- **automated** — runs without a person initiating the individual check;
- **validated** — effectiveness has been tested against representative cases.

Do not use "implemented" for a Markdown rule that no runtime mechanism enforces.

## Current maturity

The reference implementation is strongest in context routing and deterministic validation.

Current examples:
- Guides: task specs, context bundle, domain descriptions;
- Guards: catalog validity, source-state exclusions, context budget and required-domain rules;
- Sensors: manifest, include/exclude reasons, approximate context size;
- Checks: unit tests and deterministic assertions around router behavior.

Semantic evals and human approval contracts are documented but are not yet a production evaluation service.

## Compatibility files

Older documents named `evals.md` and `gates.md` remain for compatibility.

They now map to:
- semantic evals → **Checks**;
- human gates → **Guards** when they pause a consequential action before it happens, or **Checks** when they review an observed output.

This avoids maintaining a second competing taxonomy.
