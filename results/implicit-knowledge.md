# My Implicit Knowledge Register

I recorded these gaps after BEFORE and before implementing readiness improvements. I distinguish existing explicit product rules from operational knowledge that still required indirect discovery.

## IK-01 - Validation Has Multiple Undocumented Obligations

**What I found:** I could discover pytest through README and pyproject, but I had no canonical lint, contract or full verification command. I would have had to decide what "done" meant beyond the existing test suite.

**How I discovered it:** I read AGENTS, README and pyproject and recorded four absent readiness files in `before-capabilities.txt`.

**Risk I identified:** I could declare completion with passing behavior tests while leaving invalid contracts, changed evidence or architecture violations.

**Remediation I implemented:** I made `scripts/verify_repo.sh` the shared tests/lint/contract gate and wired CI directly to it. I fixed versions in `requirements-dev.txt`.

**Evidence I retain:** I retain the BEFORE capability probe, AFTER full-gate output, and a mutation test that rejects replacement of the CI gate.

## IK-02 - The Customer Identifier Rule Was Easy to Miss

**What I found:** I found the non-empty textual identifier rule in SPEC's Domain Model, but the original constructor accepted invalid IDs and no dedicated test named that invariant.

**How I discovered it:** I read models and SPEC; I observed six expected failures in the new red regression.

**Remediation I implemented:** I fixed the same invariant in both task runs, mapped FR-04/AC-10 to `tests/test_model_validation.py`, and added task-oriented navigation. I classify the model fix as the controlled product task, not as a readiness change before AFTER.

**Evidence I retain:** I retain both red logs, green logs and limited task patches.

## IK-03 - Prior Evidence Must Stay Historical

**What I found:** I needed to know that prior ADA logs and review skills were evidence, not current instructions or fresh validation. Existing project rules did not protect their bytes.

**Risk I identified:** I could overwrite historical authorship, confuse old test counts with current runs, or modify demo data to make a test pass.

**Remediation I implemented:** I archived prior artifacts, hashed them, listed protected paths, and checked exact manifest coverage. I kept the original skill voice and version unchanged.

**Evidence I retain:** I retain `source-provenance.json`, `docs/protected-paths.json`, and mutations that detect changed protected data and a removed manifest entry.

## IK-04 - Architecture Instructions Were Not Executable

**What I found:** I already had a useful architecture document, but no gate would reject a new CLI import from search or direct file access in the model.

**Remediation I implemented:** I added static checks for declared local dependencies, nonstandard runtime imports and direct domain side effects. I documented that this detects specific violations and is not a Python sandbox.

**Evidence I retain:** I retain negative tests for a CLI import and an open call without executing those mutated modules.

## IK-05 - A Passing Script Does Not Prove a Clean Experiment

**What I found:** I could reproduce source trees with Git but could not infer independent agent state from worktree isolation. I also could not infer a remote CI run from a YAML file.

**Remediation I implemented:** I recorded functional hashes, session-memory limitations, exact command ledgers and a separate protocol outcome. I explicitly kept clean-session replication pending.

**Evidence I retain:** I retain `comparability.json`, both run reports and `docs/EXPERIMENT.md`.
