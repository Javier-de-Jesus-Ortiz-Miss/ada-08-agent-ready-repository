# Task Under Test

Change ID: CR-ADA08-01

## Goal

I ask the agent to enforce the existing customer identifier invariant at construction, with focused regression tests.

## Requirements Covered

I reference FR-04 in `REQUIREMENTS.md`, the Domain Model and AC-04 / AC-10 in `SPEC.md`, and T-02 in `TASKS.md`. I leave their normative definitions there.

## Verification

I require a failing regression on the unchanged baseline, a passing regression after implementation, the existing search and CLI suite, and a diff limited to `src/customer_search/models.py` and the new `tests/test_model_validation.py`. I retain command exit codes, logs and a patch.

## Constraints

I use `REQUIREMENTS.md` and `SPEC.md` as my sources of truth. I preserve the frozen model, public constructor and all valid data. I keep runtime dependencies empty. I do not redefine requirements here or change existing tests, data, CLI or search logic.
