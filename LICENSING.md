# Licensing boundaries

Status: **license selection pending**.

This repository mixes executable code, test fixtures, skills, documentation and original methodology. It should not receive one blanket license until those asset classes are separated deliberately.

## Current state

No additional open-source or Creative Commons license is granted for the repository as a whole yet.

Public visibility allows inspection through GitHub, but reuse rights remain undefined except where third-party material carries its own license.

## Proposed asset boundaries

### Executable implementation

Candidate paths:
- `marketing_context/`
- `tests/`
- executable benchmark/evaluation scripts
- packaging metadata required to run the implementation

Decision still required:
- choose an open-source code license, if we want this reference implementation to be reusable.

### Research, architecture and methodology

Candidate paths:
- `SYSTEM-SPEC.md`
- `contexts/`
- `harness/`
- conceptual benchmark documentation
- methodology/architecture sections in Markdown

Decision still required:
- determine what can be openly reused versus what should remain noncommercial/proprietary.

### Skills

Candidate paths:
- `skills/`

Decision still required:
- determine whether skills are implementation examples, reusable public assets or part of the commercial method.

### Examples and synthetic fixtures

Candidate paths:
- `examples/`
- `benchmark/synthetic-marketing-pilot/`
- generated benchmark artifacts

These can likely follow the code/research license of the artifact they demonstrate, but should be marked explicitly.

### Third-party material

See [NOTICE.md](NOTICE.md).

Third-party source material and adapted content keep their applicable upstream terms. Do not relicense them merely because they appear in this repository.

## Governance rule

Before selecting licenses:

1. classify each top-level path;
2. identify copied/adapted third-party material;
3. decide whether the executable implementation should be open source;
4. decide whether methodology/skills should allow commercial reuse;
5. add scoped license notices;
6. add automated checks so new files inherit or declare the correct class.

Until then, avoid adding a root `LICENSE` that could be read as covering the entire repository.
