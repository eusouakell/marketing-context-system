# Sensors

**Descriptive + feedback**

Sensors observe what happened in a run or what changed in the context system.

A Sensor **does not automatically decide pass/fail**.

## Current Sensor surfaces

| Sensor | Status | Signal |
|---|---|---|
| context manifest | implemented | what sources/domains were selected |
| inclusion/exclusion reasons | implemented | why each source entered or stayed out |
| approximate context size | implemented | payload growth / budget use |
| missing required domains | implemented | absent requested context |
| source metadata/status | implemented | state/authority data used by router |
| stale-source signal | documented | source age may need review |
| decision-conflict signal | documented | potentially conflicting authority |
| stale-evidence signal | documented | evidence may no longer support current claim |
| orphan-document signal | documented | artifact has no expected relationship |
| unsupported-claim signal | documented | claim appears to lack evidence |
| duplicate-canonical-concept signal | documented | possible authority duplication |

## Sensor → Check promotion

A signal becomes a Check only when an explicit expectation and consequence exist.

Examples:

```text
Sensor: context payload = 18,200 approximate tokens
Check: configured budget <= 16,000
Result: FAIL → rebuild bundle
```

```text
Sensor: evidence age = 20 months
Check: evidence for this claim class must be <= 12 months
Result: BLOCK / ESCALATE
```

Keep observations and policy thresholds separate so the same Sensor can support different tasks.
