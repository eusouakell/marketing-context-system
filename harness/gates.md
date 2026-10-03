# Human decision gates

This file remains for compatibility with the earlier repository structure.

In the canonical four-part harness model, a human decision is classified by **when and why it occurs**:

- **Guard** — pauses a consequential action before it proceeds;
- **Check** — reviews an observed artifact/result against acceptance criteria.

See [README.md](README.md), [guards.md](guards.md) and [checks.md](checks.md).

## Human Guards

Require explicit approval before:
- positioning change;
- ICP change;
- new public performance claim;
- sensitive evidence publication;
- offer-architecture change;
- governance override.

## Human Checks

Use review after generation for:
- publication quality;
- strategic coherence;
- sensitive interpretation;
- final acceptance where automated checks are insufficient.

## Authority rule

A semantic eval cannot silently override a human Guard.

Likewise, a human approval should not erase failed deterministic evidence; an override must be explicit and traceable.
