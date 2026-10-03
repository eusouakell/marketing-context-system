# Semantic evals

Semantic evals are a subtype of **Checks**.

They belong here for compatibility with the earlier repository structure, but the canonical harness taxonomy is documented in [README.md](README.md) and [checks.md](checks.md).

## When to use

Use semantic evaluation only after deterministic rules that can be evaluated exactly have passed.

## Executive-content rubric

Score 0–2 per dimension:

- positioning fit;
- audience relevance;
- evidence discipline;
- specificity;
- decision usefulness.

Total: 0–10.

## Boundary

A semantic eval may:
- score;
- flag;
- recommend revision;
- provide evidence for a human reviewer.

It may not silently:
- redefine canonical knowledge;
- approve a new public claim;
- override a failed deterministic Check;
- authorize a sensitive action.

Calibration against human judgment remains required before treating a score as a stable quality threshold.
