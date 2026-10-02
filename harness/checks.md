# Checks

**Normative + feedback**

Checks compare an observed state or artifact against an explicit expectation.

Checks can be deterministic, semantic or human-reviewed.

## 1. Deterministic checks

Use code/structure when the criterion can be evaluated exactly.

Current or planned examples:

| Check | Status | Expected consequence |
|---|---|---|
| canonical-source-present | implemented / test-covered | fail |
| source-not-superseded | implemented / test-covered | exclude/fail |
| required-domain-present | implemented / reported | revise/escalate |
| context-budget-respected | implemented | rebuild/fail |
| required-metadata | partial | fail |
| claim-has-evidence | documented | block public use |
| public-claim-approved | documented | block publication |
| confidential-entity-not-exposed | documented | block |
| publication-permission | documented | block |
| internal-link-valid | documented | revise |

A model should not be asked to judge something a deterministic rule can validate.

## 2. Semantic checks

Use model judgment only when the criterion is inherently semantic.

Examples:
- positioning fit;
- audience relevance;
- evidence discipline;
- specificity;
- decision usefulness;
- generic/templated language.

Semantic Checks should use an explicit rubric and, where practical, human calibration.

See [evals.md](evals.md).

## 3. Human checks

Use human review when acceptance depends on accountable judgment rather than an objective assertion.

Examples:
- final publication quality;
- sensitive context interpretation;
- strategic coherence;
- whether a model-introduced claim is actually intended.

## Failure semantics

Every Check should eventually declare:
- input;
- criterion;
- pass/fail or scoring rule;
- severity;
- consequence;
- owner;
- evidence emitted.

A Check without a consequence is often only a Sensor.
