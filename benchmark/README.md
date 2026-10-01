# Marketing Context Benchmark v0.1

The benchmark is designed to test whether context routing earns its complexity.

## Conditions

- **A — prompt-only**
- **B — full-dump**
- **C — routed-context**
- **D — routed-context + verification**

## Pilot

Render the controlled condition inputs:

```bash
python benchmark/render_pilot.py
```

This creates:

```text
benchmark/generated/
  A-prompt-only.md
  B-full-dump.md
  C-routed-context.md
  D-routed-plus-verification.md
  routed-manifest.json
```

The script does not call an LLM.

Run each condition against the **same model and settings**, then save outputs as:

```text
benchmark/outputs/
  A.md
  B.md
  C.md
  D.md
```

Then:

```bash
python benchmark/evaluate_pilot.py
```

The evaluator computes deterministic signals and creates a human/semantic scoring template.

No result should be published until the four outputs actually exist.
