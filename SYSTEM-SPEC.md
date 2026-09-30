# Marketing Context System — System Specification

## Purpose

Create a portable knowledge and context system that can be maintained by humans and AI agents without depending on chat memory.

## Principles

1. Domain knowledge is organized by bounded context.
2. Canonical knowledge is separated from derived views.
3. Progressive disclosure is preferred over context dumping.
4. Decisions remain separate from current state.
5. Evidence remains separate from claims.
6. Deterministic enforcement precedes probabilistic evaluation.
7. Agents research before modifying canonical knowledge.
8. Task skills consume context; they do not define canonical truth.
9. Strategic changes require explicit human approval.
10. Automation grows from observed failure modes.

## Workflow

```text
RESEARCH → PLAN → IMPLEMENT → VERIFY
```

## Verification order

```text
Deterministic checks
→ Semantic evals
→ Human gate when required
```

## Context domains

- Brand
- Market
- Audience
- Offer
- Content
- Proof
- Go-to-Market
- Governance

Separate adjacent contexts:

- Design System
- Vendor / Platform Knowledge
- Harness

## Non-negotiables

- Derived content cannot silently become canonical.
- Missing evidence cannot be invented.
- Newer timestamps do not override source authority.
- Strategic changes require a decision.
- The model should not judge what a deterministic rule can validate.
