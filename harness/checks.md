# Deterministic checks

Initial checks:

- canonical-source-present;
- source-not-superseded;
- required-domain-present;
- claim-has-evidence;
- public-claim-approved;
- confidential-entity-not-exposed;
- context-budget-respected.

A model should not be asked to decide something that a deterministic rule can validate.

## Existing architecture requirements


Use deterministic checks when the rule can be evaluated through structure, metadata, exact comparison, status or registry.

Initial checks:

- canonical-source-present;
- required-metadata;
- source-not-superseded;
- claim-has-evidence;
- public-claim-approved;
- confidential-entity-not-exposed;
- publication-permission;
- internal-link-valid.

A failed blocking check returns the task to implementation or human review.
