# Deterministic checks

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
