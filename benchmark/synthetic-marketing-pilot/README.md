# Synthetic marketing briefing: offline verification pilot

This is a deterministic demonstration of source selection, claim review and a human publication gate. The brief was authored in this Codex conversation; run.py does not generate content, call a model or run a quality benchmark. It does not replace the existing marketing_context router.

All corpus entries describe the fictional Estudio Aurora. Synthetic policy authority applies only inside this fixture. The unsupported ROI proposition remains a review item, not an empirical claim. Publication stays HOLD with no human approval.

## Run

Run `python -m unittest discover -s benchmark/synthetic-marketing-pilot -v` from the repository root. Tests use an injected counting function to verify budget boundaries; they do not assert actual tokenizer accuracy.

To regenerate manifest.json, install tiktoken==0.14.0 in your own Python environment, prepare the o200k_base tokenizer cache separately, set TIKTOKEN_CACHE_DIR, and run `python benchmark/synthetic-marketing-pilot/run.py`. The runner blocks tokenizer downloads. No API key is required. Missing cache fails rather than making a network request.

## Evidence and limitations

manifest.json records the static selected-knowledge count and budget. Skill instruction tokens are the previously measured SKILL.md count, not an inference request token count. Total session tokens remain unknown. Unit tests check expected fixture behavior and invalid inputs. Human editorial assessment is still needed; keyword/field checks cannot determine whether all prose claims are supported.

No baseline versus TLC comparison has been executed. A single fixture cannot establish benefits, cost savings, editorial quality or model reliability. Paid A/B/C/D benchmark remains pending by user choice.

Specification workflow was informed by TLC Spec-Driven v3.3.0 by Felipe Rodrigues / Tech Leads Club, CC BY 4.0, at https://github.com/tech-leads-club/agent-skills/commit/120b67676388241b314699fa8fa9af25ada6d1d4. No upstream skill content is bundled here; project artifacts are newly written.
