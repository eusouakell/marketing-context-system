# Agency Agents catalog audit

Status: **in progress — full inventory complete, contract-level deep review pending**.

This directory audits the public `msitarzewski/agency-agents` catalog against the local eusouakell Agentic Factory.

## Scope

- 282 README-listed agents inventoried.
- Every agent receives a first-pass role class, capability family and Factory-fit status.
- 49 agents are flagged for contract-level deep review because they may overlap with, strengthen or expose gaps in the current Registry V1.
- Domain-specific agents outside current goals remain accounted for but are not deep-read unless they expose a transferable capability.

## Files

- `catalog.csv` — complete inventory.
- `catalog.json` — complete machine-readable inventory + audit metadata.
- `capability-map.md` — generated first-pass summary.
- `deep-review.md` — contract-level findings (added next).
- `roster-v2-proposal.md` — final recommendation only after deep review.

## Decision rule

No external agent is installed automatically.

The external catalog is a benchmark for discovering capabilities, authority patterns and anti-patterns. The local Registry remains authoritative.
