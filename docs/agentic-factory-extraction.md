# Agentic Factory extraction plan

Status: **approved direction / migration not started**.

## Decision

Do **not** rename `marketing-context-system`.

Create a new repository:

```text
eusouakell/agentic-factory
```

The repositories represent different abstractions:

- **Marketing Context System** answers: *what should this task know, trust and load?*
- **Agentic Factory** answers: *who may do what, with which controls, evidence and approval?*

The Factory may consume the Context System. It is not the Context System.

## Target topology

```text
agentic-factory
├── agents/
│   ├── registry.json
│   ├── contracts/
│   ├── audit/
│   └── validate_registry.py
├── control-plane/
│   └── README.md
├── controls/
│   └── README.md
├── governance/
│   ├── authority-model.md
│   └── provenance.md
├── integrations/
│   ├── marketing-context-system.md
│   ├── cereja-knowledge-system.md
│   └── cereja-editorial-engine.md
├── tests/
└── README.md
```

## Boundary map

### Move to `agentic-factory` as canonical

| Current asset | Target | Notes |
|---|---|---|
| `agents/registry.json` | `agents/registry.json` | canonical roster |
| `agents/contracts/**` | `agents/contracts/**` | canonical agent authority contracts |
| `agents/audit/**` | `agents/audit/**` | provenance and roster decisions |
| `agents/validate_registry.py` | `agents/validate_registry.py` | registry check |
| `tests/test_agent_registry.py` | `tests/test_agent_registry.py` | registry CI |
| `AGENTIC-FACTORY.md` | root architecture doc | rewrite links to be repo-neutral |
| generic control taxonomy | `controls/README.md` | Guides / Guards / Sensors / Checks / Evals / Human Gates |
| orchestration principles | `control-plane/README.md` | routing, retries, handoffs, state, escalation |

### Stay in `marketing-context-system`

| Asset | Reason |
|---|---|
| `marketing_context/**` | executable context router |
| `contexts/**` | context-domain architecture |
| `examples/**` | context-routing examples |
| `benchmark/**` | context-ablation/reference implementation |
| `evals/context-ablation.md` | context-system experiment |
| `evals/brand-consistency.md` | marketing/content-specific eval |
| `harness/**` | current context-system implementation/maturity views |
| `guides/README.md` | currently references task specs, context bundle and context domains |
| `SYSTEM-SPEC.md` | context-system specification |

The context-system harness remains a **consumer/implementation of the Factory control model**, not the canonical definition of the Factory.

## What should not be copied wholesale

Do not move `harness/**` verbatim into the new repository.

Those files mix:
- generic control concepts;
- current Marketing Context System mechanisms;
- context-router maturity/status.

The new Factory should define the generic control contract once. Marketing Context System keeps its implementation-specific mapping.

## Migration sequence

### Phase 1 — Seed
1. Create empty public `eusouakell/agentic-factory` repository.
2. Add Factory README, authority model and control-plane contract.
3. Copy Registry V2, agent contracts, audit artifacts, validator and tests.
4. Add provenance/notice for external audit material.
5. Add CI for registry validation.

### Phase 2 — Verify
1. Registry V2 validates in the new repo.
2. Contract paths resolve.
3. Audit artifacts remain linked.
4. No agent has direct `main`, `publish` or `production` authority.
5. Core/on-demand counts remain 7 / 14.

### Phase 3 — Integrate
1. Add integration docs for Marketing Context System, Cereja Knowledge System and Cereja Editorial Engine.
2. Update those repositories to link to the new canonical Factory.
3. Keep domain authority in domain repos.

### Phase 4 — Deprecate duplicates
Only after the new repo is validated and linked:

1. replace `marketing-context-system/agents/` with a compatibility pointer or remove it in a dedicated PR;
2. remove registry-specific CI/tests from Marketing Context System;
3. keep context-specific harness/runtime;
4. update README architecture diagrams;
5. verify no dead links.

## Compatibility principle

Use **copy → validate → redirect/deprecate → remove**.

Do not delete the old canonical copy in the same step that creates the new one.

## Git history

Preferred if practical: preserve meaningful provenance through commit references and migration notes. A full history rewrite is not required.

Every migrated canonical file should record:

- source repository;
- source path;
- source commit or migration PR;
- migration date.

## Licensing / provenance

Agency Agents audit material is derived from an MIT-licensed upstream catalog and must retain appropriate attribution.

Local agent contracts are original eusouakell Agentic Factory contracts.

Do not apply a blanket repo license until asset-level licensing boundaries are explicitly reviewed.

## Definition of Done

Extraction is complete when:

- `eusouakell/agentic-factory` exists and is the canonical home of Registry V2;
- CI is green in the new repo;
- consumers link to the new canonical Factory;
- Marketing Context System no longer owns a duplicate active registry;
- context routing still passes its own CI;
- no canonical authority moved out of Núcleo, Flame or Editorial Engine.
