# Marketing Context System — System Specification

## Purpose

Create a portable knowledge and context system that can be maintained by humans and AI agents without depending on chat memory.

## Principles

1. Domain knowledge is organized by bounded context.
2. Canonical knowledge is separated from derived views.
3. Progressive disclosure is preferred over context dumping.
4. Decisions remain separate from current state.
5. Evidence remains separate from claims.
6. Deterministic enforcement precedes probabilistic evaluation when the criterion is mechanically testable.
7. Agents research before modifying canonical knowledge.
8. Task skills consume context; they do not define canonical truth.
9. Strategic changes require explicit human approval.
10. Automation grows from observed failure modes.

## Workflow

```text
RESEARCH → PLAN → IMPLEMENT → VERIFY
```

## Harness model

The runtime uses four control classes:

```text
GUIDES + GUARDS
      ↓
EXECUTION
      ↓
SENSORS
      ↓
CHECKS
      ↓
HUMAN DECISION WHEN REQUIRED
```

- **Guides** describe relevant context before/during execution.
- **Guards** constrain invalid or consequential actions before they proceed.
- **Sensors** record what happened or what changed.
- **Checks** compare observed state/output against explicit expectations.

For verification, prefer deterministic Checks before semantic Checks. Human review remains where accountable judgment is required.

See [harness/README.md](harness/README.md).

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
