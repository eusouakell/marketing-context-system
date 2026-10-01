# Synthetic marketing brief Specification

## Problem Statement

A marketing agent needs a small, traceable context bundle rather than an unrestricted document dump. This local pilot examines whether explicit acceptance criteria improve the reviewability of a synthetic briefing. It does not measure model quality or establish framework superiority.

## Goals

- Produce one reviewable brief and a context manifest from a frozen synthetic corpus.
- Record unsupported claims and preserve a human publication gate.
- Count static input/output tokens with o200k_base before claiming context savings.

## Out of Scope

| Feature | Reason |
| --- | --- |
| Paid API benchmark | User selected no API cost |
| Real client knowledge | Public portfolio must exclude proprietary content |
| Production publication | Draft requires human editorial approval |
| Router replacement | Existing executable router is already available upstream |
| Independent causal comparison | Same-chat sequential generation is contaminated by shared context |

## Assumptions & Open Questions

| Assumption / decision | Chosen default | Rationale | Confirmed? |
| --- | --- | --- | --- |
| Brand | Fictional Estudio Aurora | Avoid client/IP disclosure | Local implementation choice |
| Deliverable | Brief for a newsletter on choosing useful AI context | Fits marketing and knowledge work territory | Local implementation choice |
| Source authority | Synthetic approved policy is authoritative only within the fixture | Does not imply real-world evidence | Local implementation choice |
| Context budget | 1500 o200k_base tokens for the selected knowledge text | Small pilot; skill/tool overhead reported separately | Local implementation choice |
| Publishing | HOLD until Kell reviews | Existing human-gate requirement | Yes |
| Remaining dimensions | N/A for a static local artifact with no API/auth/payment/concurrency | No runtime service or production state transitions | Local implementation choice |

Open questions: none; local choices are logged above and are not asserted as Kell's brand positions.

## User Stories

### P1: Review a grounded draft

As a marketing strategist, I want a brief whose decisions point to sources so I can review claims and approve publication explicitly.

Acceptance Criteria:
1. WHEN the frozen fixture is selected THEN the manifest SHALL include exactly brand, audience and editorial-policy, with source IDs and selection reasons (BRIEF-01).
2. IF the corpus contains a superseded campaign THEN the manifest SHALL exclude that campaign and record superseded as the reason (BRIEF-02).
3. The brief SHALL identify every input source as synthetic and SHALL NOT cite synthetic content as external evidence (BRIEF-03).
4. IF a draft proposes a quantified business benefit without external evidence THEN the brief SHALL record that proposition under unsupported_claims rather than as an established result (BRIEF-04).
5. The artifact SHALL keep publication_status equal to HOLD and human_approval equal to null (BRIEF-05).
6. WHEN static token counting completes THEN the report SHALL record tokenizer name, selected knowledge token count and the 1500-token budget outcome separately from skill instruction tokens (BRIEF-06).

Independent Test: inspect the manifest against the frozen fixture; reject included superseded content, absent source IDs, invented evidence and a release status without approval.

## Edge Cases

- Empty or missing fixture: fail preparation; do not invent a replacement source.
- Budget exceeded: report failure; do not truncate knowledge silently.
- Missing empirical evidence: preserve the gap and avoid numerical outcome claims.

## Requirement Traceability

| Requirement ID | Story | Phase | Status |
| --- | --- | --- | --- |
| BRIEF-01 | P1 | Specify | Pending |
| BRIEF-02 | P1 | Specify | Pending |
| BRIEF-03 | P1 | Specify | Pending |
| BRIEF-04 | P1 | Specify | Pending |
| BRIEF-05 | P1 | Specify | Pending |
| BRIEF-06 | P1 | Specify | Pending |

## Success Criteria

All six criteria have artifact evidence and a verified check before declaring the pilot executed. Independent verification and semantic/human review must be reported accurately; structural validation alone is insufficient.

## Attribution and status

Specification process follows TLC Spec-Driven v3.3.0 by Felipe Rodrigues / Tech Leads Club, CC BY 4.0, pinned at 120b67676388241b314699fa8fa9af25ada6d1d4. This project-specific specification is newly written. Status: Specify only; implementation and comparative evaluation have not run.
