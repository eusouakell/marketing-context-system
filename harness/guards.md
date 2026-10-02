# Guards

**Normative + feedforward**

Guards constrain execution before an invalid or consequential action is accepted.

## Current Guard surfaces

| Mechanism | Status | Failure consequence |
|---|---|---|
| invalid/superseded source exclusion | implemented | source cannot enter selected bundle |
| required-domain policy | implemented / reported | missing domain is surfaced before downstream use |
| context budget | implemented | selection is constrained to configured budget |
| catalog-root path boundary | implemented | source path outside allowed root is rejected |
| source-state rules | implemented | disallowed source states are excluded |
| strategic/publication approval rules | documented | human escalation required |
| confidentiality/public-proof rules | documented | do not proceed without authorization |

## Design rule

A text instruction such as "do not expose confidential entities" is only a documented Guard until the runtime can actually constrain or pause that action.

Label maturity accurately.

## Human Guards

Human approval is a Guard when it occurs **before** a consequential action such as:
- publishing a new public claim;
- changing positioning/ICP;
- releasing sensitive evidence;
- overriding a governance control.

Human review of a completed artifact against quality criteria is classified as a Check instead.
