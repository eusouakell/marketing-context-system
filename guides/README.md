# Guides

Guides tell an agent **how to approach a task** and what context contract applies. They do not enforce truth or silently override canonical knowledge.

Current guide-like assets include:

- `SYSTEM-SPEC.md` — system-wide operating principles;
- `contexts/README.md` — bounded-context guidance;
- `examples/task-spec.executive-article.json` — executable task-context contract;
- task-specific skills that consume the routed context bundle.

## Boundary

A Guide may recommend workflow, structure, sequencing or context needs.

A Guide may **not**:

- bypass a Guard;
- convert derived material into canonical truth;
- weaken a deterministic Check;
- interpret a Sensor as a pass/fail decision by itself.

Operational sequence:

```text
GUIDE
  ↓
GUARDS
  ↓
ROUTE / EXECUTE
  ↓
SENSORS
  ↓
CHECKS
  ↓
EVALS / HUMAN GATES when required
```
