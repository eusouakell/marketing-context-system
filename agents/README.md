# Agent Registry V2

This directory is the canonical registry for **specialist agents** in the eusouakell Agentic Factory.

The Factory deliberately separates:

- **control plane** — routing, retries, handoffs, state and escalation;
- **agents** — bounded specialist capabilities;
- **Guides** — instructions and domain contracts;
- **Guards** — hard runtime boundaries;
- **Sensors** — observations;
- **Checks** — deterministic validations;
- **Evals** — judgment that is not safely reducible to a boolean;
- **Human gates** — decisions that remain human.

## Architectural rule

**The Orchestrator is not an agent persona.**

Routing and authority remain in the control plane. Agents cannot promote themselves, call arbitrary agents, widen tool scope or bypass a failed Guard/Check.

## Roster model

V2 has two registered tiers:

### Core — 7
Core agents are broadly reusable and may be considered in normal Factory routing when their explicit trigger is met.

- Research Synthesist
- Frontend Engineer
- Code Reviewer
- Security Auditor
- Accessibility Auditor
- Production Readiness Evaluator
- Flame UI Composer

### On demand — 14
These are activated only when the task explicitly matches their specialist trigger.

- Motion Web Director
- Motion Video Director
- Editorial Typography Director
- Photo Art Director
- Generative Photography Specialist
- Inclusive Experience Reviewer
- Experience Researcher
- Test Automation Engineer
- Workflow Architect
- Repository Analyst
- Agent Tooling Engineer
- Knowledge Systems Architect
- Discoverability Architect
- Data Visualization Engineer

## Conditional / future capabilities

The Agency Agents audit identified additional valuable capabilities — identity/access, privacy, SRE/platform, document compilation, proposal strategy, paid media, model QA and others.

They are **not registered yet**.

A future capability only enters the registry when a real project creates a concrete trigger and its authority boundary is clear.

## What is intentionally not an agent

Some useful upstream roles became system controls instead of personas:

- orchestration → **control plane**;
- git workflow discipline → **Guide / repository policy**;
- minimal-change discipline → **Guard**;
- prompt versioning/testing → **Guide + eval infrastructure**;
- experiment tracking → **Sensors / protocol**;
- brand guardianship → **canonical brand system + human gate**;
- channel post writing → **Editorial Engine + format Guides**;
- meeting notes / executive summaries → **skills**.

## Registry contract

The machine-readable source is [registry.json](registry.json).

Each agent must declare:

- tier and lifecycle status;
- purpose and trigger;
- inputs and outputs;
- allowed tools;
- write authority;
- Guides, Guards, Sensors, Checks and Evals;
- human gate;
- retry and escalation policy;
- provenance.

No agent may have direct authority to merge to `main`, publish autonomously or silently modify canonical brand/knowledge rules.

## Lifecycle

`pilot` → `active` → `retired`

Promotion requires:
1. at least one real task;
2. evidence that the role boundary reduced ambiguity or rework;
3. no unresolved authority collision;
4. explicit human approval.

## Audit provenance

The V2 design is grounded in the full Agency Agents audit:

- 282 agents inventoried;
- 80 roster-relevant contracts reviewed at contract level;
- no upstream agent files installed;
- upstream MIT license recorded;
- local contracts rewritten around local authority boundaries.

See [agents/audit/agency-agents/](audit/agency-agents/).

## Domain contracts

The registry owns **who can do what**.

Domain repositories own **what is true**:
- Cereja Knowledge System / Flame — visual and knowledge authority;
- Cereja Editorial Engine — editorial packets, format contracts and publication gates;
- Marketing Context System — context routing and current Factory runtime.

Agents consume those contracts. They do not replace them.
