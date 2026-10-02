# Guards

**Normative + feedforward**

Guards constrain execution before an invalid or consequential action is accepted.

## Current Guard surfaces

| Guard | Status | Failure consequence |
|---|---|---|
| eligible-source-state | implemented | inactive/superseded source cannot enter the bundle |
| task-domain-scope | implemented | out-of-scope domain cannot enter the bundle |
| allowed-kind | implemented | disallowed artifact kind cannot enter the bundle |
| minimum-authority | implemented | source below the task threshold cannot enter the bundle |
| context-budget | implemented | selection cannot exceed the configured budget |
| catalog-root-boundary | implemented | source path outside the catalog root is rejected |
| strategic/publication approval | documented | human escalation required |
| confidentiality/public-proof authorization | documented | do not proceed without authorization |

The router emits the applied Guard set and blocked item IDs in the run manifest.

## Design rule

A text instruction such as "do not expose confidential entities" is only a **documented Guard** until the runtime can actually constrain, pause or reject that action.

Label maturity accurately.

## Required context

Required-domain selection is prioritized before optional context is filled.

If a required domain is still missing after routing, that absence is observed by a **Sensor** and evaluated by the `required-domains-present` **Check**. The current reference router reports the failure; it does not yet stop a downstream consumer automatically.

## Human Guards

Human approval is a Guard when it occurs **before** a consequential action such as:

- publishing a new public claim;
- changing positioning or ICP;
- releasing sensitive evidence;
- overriding a governance control.

Human review of a completed artifact against quality criteria is classified as a Check instead.
