# Synthetic marketing brief validation

**Verdict: PASS for this frozen deterministic fixture.** All six acceptance criteria have artifact evidence and a verified check. This does not validate model quality, a framework comparison, or all possible prose claims.

Date: 2026-10-01. Verifier: independent sub-agent, distinct from author.
Spec: `benchmark/synthetic-marketing-pilot/spec.md`.
Scope: `benchmark/synthetic-marketing-pilot/{corpus.json,brief.json,run.py,test_pilot.py,manifest.json}`. Line citations below use this directory as their prefix.

## Acceptance evidence

| Criterion | Expected outcome | Exact evidence and assertion | Result |
| --- | --- | --- | --- |
| BRIEF-01 | Exactly brand, audience, editorial-policy with IDs and reasons | `test_pilot.py:20`: `assertEqual([i["id"] for i in report["selected"]], ["brand", "audience", "editorial-policy"])`; `test_pilot.py:21`: `assertTrue(all(i["reason"] for i in report["selected"]))`; `manifest.json:4`, `manifest.json:15`, `manifest.json:26` | PASS |
| BRIEF-02 | Exclude old campaign, reason superseded | `test_pilot.py:22`: `assertEqual(report["excluded"], [{"id": "old-campaign", "reason": "superseded"}])`; `manifest.json:39` | PASS |
| BRIEF-03 | Synthetic inputs; no external evidence citation | `test_pilot.py:25`: `assertTrue(self.brief["synthetic"])`; `test_pilot.py:26`: `assertTrue(all(i["synthetic"] for i in self.corpus["items"]))`; `test_pilot.py:27`: `assertEqual(self.brief["external_evidence"], [])`; rejection at `test_pilot.py:29`; explicit reader notice at `brief.json:15` | PASS for supplied artifact |
| BRIEF-04 | Quantified ROI proposition stays unsupported | `test_pilot.py:32`: `assertEqual(self.brief["unsupported_claims"], ["Usar IA dobra o ROI"])`; rejection at `test_pilot.py:34`; proposition at `brief.json:11`; outline `brief.json:7` through `brief.json:9` contains no asserted quantified business outcome | PASS for supplied proposition |
| BRIEF-05 | HOLD; human approval null | `test_pilot.py:37`: `assertEqual(self.brief["publication_status"], "HOLD")`; `test_pilot.py:38`: `assertIsNone(self.brief["human_approval"])`; rejection at `test_pilot.py:40`; `brief.json:13`, `brief.json:14` | PASS |
| BRIEF-06 | Tokenizer, selected knowledge count, 1500 budget outcome separate from skill tokens | `test_pilot.py:48` asserts count 1500; `test_pilot.py:49` asserts encoding o200k_base; `test_pilot.py:50` asserts budget 1500; `test_pilot.py:51` asserts within_budget; `test_pilot.py:52` asserts separate skill count 3783; `test_pilot.py:54` rejects 1501. `manifest.json:45` through `manifest.json:50` records actual 106 knowledge tokens, budget 1500, skill tokens 3783, unknown session total | PASS; actual count independently rerun |

The independent offline token check used bundled Python, tiktoken 0.14.0 from work/token-tools and work/token-cache, with tiktoken.load.read_file overridden to reject downloads. Calling prepare with the real o200k_base encoder produced selected_knowledge_tokens=106 and a complete object equal to manifest.json. No manifest rewrite occurred. The skill count 3783 is a previously measured input recorded by the implementation, not independently remeasured here and not total session telemetry.

## Gate and edge checks

Command: `python -m unittest discover -s outputs/synthetic-marketing-pilot -v`.
Result: 7 passed, 0 failed, 0 skipped. New feature files have no historical test count available; no assertion weakening was assessed against committed history.

Empty fixture fails with KeyError (`test_pilot.py:44`). Budget excess fails rather than truncating (`test_pilot.py:54`, `run.py:35`). Missing empirical evidence remains an explicit unsupported item (`brief.json:11`, `brief.json:12`). Invalid section IDs fail (`test_pilot.py:58`). Missing-file preparation was not separately tested; the main entry reads required files directly at `run.py:52`, `run.py:53`.

All seven tests map to BRIEF-01/02, BRIEF-03, BRIEF-04, BRIEF-05, missing-source edge, BRIEF-06/budget edge, and source traceability. There are no routes or service layers to verify.

## Discrimination sensor

Three temporary copies only; each copy was deleted by TemporaryDirectory cleanup. Every mutation exited 1 with one failed test.

| Mutation in scratch | Failure evidence | Outcome |
| --- | --- | --- |
| `run.py:34`: tokens > 1500 changed to tokens > 1501 | `test_pilot.py:54`: expected ValueError was not raised | KILLED |
| `run.py:25`: publication gate condition replaced by False | `test_pilot.py:40`: expected ValueError was not raised | KILLED |
| `run.py:19`: superseded reason replaced by not required | `test_pilot.py:22`: exclusion object mismatch | KILLED |

SHA256 hashes of the five real scoped source/artifact files matched before and after all mutations. The gate test can create ordinary Python bytecode caches; isolation claims concern the five scoped files. No fault was applied to the real implementation. No GitHub mutation occurred.

## Precision gaps and limits

The spec does not define what makes a selection reason adequate beyond its presence. BRIEF-03 does not specify per-source labeling versus a global synthetic notice; this artifact supplies both corpus flags and a global notice. BRIEF-04 specifies a semantic rule but no quantified-claim detection scheme. The runner protects the single known ROI string at `run.py:27`; it does not classify arbitrary future prose. BRIEF-06 does not define how skill-token provenance must be verified. These are precision/provenance limits, not evidence that this fixed artifact violates its criteria.

A human still must assess editorial clarity and semantics before publication. This verification is deterministic fixture checking only: no LLM quality benchmark, no baseline/framework comparison, no causal claim, and no total session token telemetry. Field and keyword assertions cannot establish grounding of every possible future claim.

## Process and quality deviations

The required validate.md was read completely. coding-principles.md was inspected: the scoped implementation is small and focused; no unnecessary abstraction or service layer was added. Unused test import copy is a minor cleanup observation, not a behavior failure.

There is no tasks.md, so no task-completion ledger or prescribed Build gate could be checked. The parent supplied the explicit unittest command. The current directory is not a Git repository and these are new local files, so no committed diff or test-history comparison was available. Scope was limited to the named files, with SHA256 isolation evidence as the status equivalent.

By parent instruction this report is stored in benchmark/synthetic-marketing-pilot/validation.md rather than the skill's feature-folder location. Spec status/traceability were not edited. validate_state.py and lessons.py were not run because this verifier may write only the report and scratch; the parent must handle closing gates and record grounded precision lessons if asserting full TLC workflow completion. Full skill-process compliance is therefore not claimed.

Parent-reported remote publication after verification: commit 242e76eac3649de92315891d1514491224342cfc, parent 624eeb7e76b137b2601e679d9dea3094b40c0a89, paths benchmark/synthetic-marketing-pilot/. This verifier did not inspect the remote diff or perform any remote action; its evidence remains the local named files.
