# Checks

**Normative + feedback**

Checks compare an observed state or artifact against an explicit expectation.

Checks can be deterministic, semantic or human-reviewed.

## 1. Deterministic Checks

Use code or structure when the criterion can be evaluated exactly.

| Check | Status | Current consequence |
|---|---|---|
| context-budget-respected | implemented + test-covered | manifest pass/fail; router already constrains selection |
| required-domains-present | implemented + test-covered | manifest pass/fail; downstream blocking not yet automated |
| required-metadata | partial/documented | revise/fail where implemented |
| claim-has-evidence | documented | block public use when implemented |
| public-claim-approved | documented | block publication when implemented |
| confidential-entity-not-exposed | documented | block when implemented |
| publication-permission | documented | block when implemented |
| internal-link-valid | documented | revise when implemented |

Source eligibility, source status, domain scope, kind allowlists, authority thresholds and context budget **before assembly** are Guards, not Checks.

A model should not be asked to judge something a deterministic rule can validate.

## 2. Semantic Checks

Use model judgment only when the criterion is inherently semantic.

Examples:

- positioning fit;
- audience relevance;
- evidence discipline;
- specificity;
- decision usefulness;
- generic or templated language.

Semantic Checks should use an explicit rubric and, where practical, human calibration.

See [evals.md](evals.md).

## 3. Human Checks

Use human review when acceptance depends on accountable judgment rather than an objective assertion.

Examples:

- final publication quality;
- sensitive context interpretation;
- strategic coherence;
- whether a model-introduced claim is actually intended.

## Sensor → Check contract

A Sensor reports an observation. A Check adds the expectation and consequence.

```text
Sensor: missing_required_domains = ["evidence"]
Check: required-domains-present
Result: FAIL
```

## Failure semantics

Every Check should eventually declare:

- input;
- criterion;
- pass/fail or scoring rule;
- severity;
- consequence;
- owner;
- evidence emitted.

A Check without an expectation or consequence is often only a Sensor.
