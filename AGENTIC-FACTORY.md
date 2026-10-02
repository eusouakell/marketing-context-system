# Agentic Factory — Guides / Guards / Sensors / Checks

This repository uses four operational control types. The purpose is to make agent behavior inspectable without collapsing instructions, enforcement, observation and validation into one "harness" bucket.

| Layer | Responsibility | Current implementation |
|---|---|---|
| Guides | Tell the agent how to approach a task and which context contract applies | `guides/`, `SYSTEM-SPEC.md`, context/task specs |
| Guards | Block invalid or unsafe runtime states before routing proceeds | `marketing_context/guards.py` |
| Sensors | Observe runtime state without deciding pass/fail | `marketing_context/sensors.py`, manifest `sensors` block |
| Checks | Deterministically validate candidate eligibility and route invariants | `marketing_context/checks.py`, unit tests |

## Boundaries

### Guides
Guides are instructional. They may specify workflow or required context, but they do not create canonical truth and cannot weaken enforcement.

### Guards
Guards are fail-fast boundaries. Current runtime guards validate task-spec invariants and keep catalog reads inside the catalog root.

### Sensors
Sensors expose what happened. The route manifest now reports selected/excluded item counts, required-domain coverage and budget utilization.

A sensor is evidence for diagnosis; it is not approval.

### Checks
Checks are deterministic rules that can return a stable answer without model judgment. Candidate eligibility by status, domain, kind and authority belongs here.

## What remains outside the four layers

**Semantic evals** measure qualities that deterministic checks cannot prove.

**Human gates** retain authority for strategic or publication decisions.

That sequence remains:

```text
GUIDE
  ↓
GUARDS
  ↓
EXECUTION
  ↓
SENSORS
  ↓
DETERMINISTIC CHECKS
  ↓
SEMANTIC EVALS
  ↓
HUMAN GATE when required
```

## Migration status

V1 changes runtime boundaries without deleting the existing `harness/` documentation paths. Those files remain stable references while the new executable boundaries are validated.

A later cleanup may relocate or deprecate legacy harness docs only after link and consumer impact is known.
