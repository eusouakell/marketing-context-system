# Agent Registry moved

The canonical Agent Registry, specialist contracts, audit provenance and registry validation now live in:

https://github.com/eusouakell/agentic-factory

This directory is a compatibility pointer. The canonical Agent Registry lives in `eusouakell/agentic-factory`.

## Current boundary

Marketing Context System owns:

- context routing;
- authority/relevance selection;
- required-domain logic;
- context budgets;
- manifests;
- context-specific Guards / Sensors / Checks;
- context ablation experiments.

Agentic Factory owns:

- Agent Registry V2;
- specialist agent contracts;
- control-plane model;
- generic authority model;
- registry governance and provenance.

Do not add new agent contracts or registry state here.
