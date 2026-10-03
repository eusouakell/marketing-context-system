# Guides

**Descriptive + feedforward**

Guides make the environment legible to the task before or during execution.

## Current Guide surfaces

| Mechanism | Status | Purpose |
|---|---|---|
| context catalog descriptions | implemented | describe available sources/domains |
| task spec | implemented | describes task needs and required domains |
| assembled context bundle | implemented | gives the execution selected authoritative context |
| context-domain documentation | documented | explains meaning and source expectations |
| skills | documented / partial | describe how to perform specialized tasks |
| examples | documented | show expected structures and usage |

## Rule

A Guide informs behavior but does not prove compliance.

If a requirement must be enforced, pair the Guide with a Guard or Check.

## Context principle

Prefer **minimum sufficient authoritative context**.

Do not make "more documentation" the default response to an agent failure. First identify whether the missing mechanism is actually:
- orientation → Guide;
- constraint → Guard;
- observability → Sensor;
- verification → Check.
