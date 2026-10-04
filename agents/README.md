# Agent Registry V1

This directory is the canonical registry for **specialist agents** in the eusouakell Agentic Factory.

The factory deliberately separates:

- **control plane** — routing, retries, handoffs, state and escalation;
- **agents** — bounded specialist capabilities;
- **Guides** — instructions and domain contracts;
- **Guards** — hard runtime boundaries;
- **Sensors** — observations;
- **Checks** — deterministic validations;
- **Evals** — judgment that is not safely reducible to a boolean;
- **Human gates** — decisions that remain human.

## Important architectural rule

**The Orchestrator is not an agent persona.**

It is control-plane logic. Specialist agents cannot promote themselves, call arbitrary agents, widen tool scope or bypass a failed Guard/Check.

## V1 roster

### Engineering / review
- Frontend Engineer
- Security Auditor
- Production Readiness Evaluator

### Visual Studio
- Flame UI Composer
- Motion Web Director
- Motion Video Director
- Editorial Typography Director
- Photo Art Director
- Generative Photography Specialist
- Inclusive Visual Reviewer

The first roster intentionally does **not** attempt to reproduce the full Agency Agents catalog. It captures capabilities that map to current work and identified gaps.

## Registry contract

The machine-readable source is [registry.json](registry.json).

Each agent must declare:

- purpose and trigger;
- inputs and outputs;
- allowed tools;
- write authority;
- Guides, Guards, Sensors, Checks and Evals;
- human gate;
- retry and escalation policy;
- provenance;
- lifecycle status.

No production agent may have direct authority to merge to `main`, publish autonomously or silently modify canonical brand/knowledge rules.

## Lifecycle

`pilot` → `active` → `retired`

Promotion requires:
1. at least one real task;
2. evidence that the role boundary reduced ambiguity or rework;
3. no unresolved authority collision;
4. explicit human approval.

## Domain contracts

The registry owns **who can do what**.

Domain repositories own **what is true**:
- Flame / Cereja Knowledge System — visual and knowledge authority;
- Cereja Editorial Engine — editorial packets, format contracts and gates;
- Marketing Context System — routing/context controls.

Agents consume those contracts. They do not replace them.
