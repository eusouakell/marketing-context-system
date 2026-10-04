# Agent Registry moved

The canonical Agent Registry, specialist contracts, audit provenance and registry validation now live in:

https://github.com/eusouakell/agentic-factory

This directory remains only as a compatibility pointer during the extraction cleanup.

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
