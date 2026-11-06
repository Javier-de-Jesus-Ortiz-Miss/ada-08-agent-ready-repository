# BEFORE Agent Run

## Run Context

I used Codex with local shell/Python/Git and workspace permissions. I did not receive an exact runtime model identifier. I based my isolated worktree on `ada08-baseline` (`ada08-baseline`) and used CR-ADA08-01 with the fixed input in `docs/EXPERIMENT_PROMPT.txt`. I report this as a controlled local execution, not as an independent clean-session invocation.

## Clarification Questions

I recorded zero repository-context questions during this task run. I distinguish setup approvals from clarification questions. I do not infer an improvement from zero questions in both conditions.

## Repository Exploration

I retain the explicit context reads and file inventory in `results/evidence/before-commands.json` and its referenced output logs. I count context reads separately from files merely listed by rg and from files read by validation tools.

## Incorrect Assumptions

I recorded zero observed incorrect product assumptions in this run. I do not treat the inherited constructor defect as an assumption made by the agent. I do not claim to observe hidden reasoning or unrecorded repository access.

## Failed / Unknown Commands

I distinguish the expected red regression exit 1 from unexpected operational failures. I retain each executed command, expected exit code and actual exit code in my ledger; I do not invent failures for missing BEFORE capabilities.

## Out-of-Scope Changes

I limited the product patch to `src/customer_search/models.py` and `tests/test_model_validation.py`. I retained readiness changes separately from task changes. I retained a full patch and scope output in `results/evidence/before.diff` and `before-scope.txt`.

## Validation Evidence

I retain baseline tests, the red constructor regression, the complete green suite, and a CLI smoke run in the ledger and output files. I interpret an expected failing regression as evidence that the test detects the defect, not as a failed final implementation.

## Final Result

I record **functional PASS** and **strict protocol PARTIAL**. I separate my final functional outcome from strict experimental validity. I mark the clean-session protocol PARTIAL because I retained shared agent state. I use my final measured metrics below as the source of truth.

## Measured Metrics

I observed the following quantities from the retained ledger and scope patch:

| Metric I counted | Value |
|---|---:|
| Repository clarification questions | 0 |
| Context files explicitly read | 11 |
| Observed incorrect assumptions | 0 |
| Unexpected failed / unknown commands | 0 |
| Expected red regression command | 1 |
| Cases failing in that expected red run | 6 |
| Out-of-scope product files modified | 0 |
| Task files modified | 2 |
| Commands retained in my ledger | 8 |
| Passing test cases before task implementation | 25 |
| Passing test cases after task implementation | 35 |

I read 11 context files explicitly; I do not equate an rg inventory with reading every file. I read the inherited eleven files: AGENTS, README, REQUIREMENTS, SPEC, ARCHITECTURE, TASKS, TASK_UNDER_TEST, pyproject.toml, models.py, test_search.py and test_cli.py.

## Commands and Exit Codes

I preserve timestamps, normalized working directories and argument records in [my command ledger](evidence/before-commands.json). I show the command purposes below; I label expected failure separately.

| Step I executed | Command I recorded | Actual exit | Expected exit | Evidence I retained |
|---|---|---:|---:|---|
| exploration | `rg --files -g !results/prior/** -g !skills/**` | 0 | 0 | [output](evidence/before-exploration.txt) |
| context | `Python explicit context reads (full argv in ledger)` | 0 | 0 | [output](evidence/before-context.txt) |
| baseline-tests | `.venv/bin/python -m pytest -q` | 0 | 0 | [output](evidence/before-baseline-tests.txt) |
| capabilities | `Python readiness-file presence probe (full argv in ledger)` | 0 | 0 | [output](evidence/before-capabilities.txt) |
| red-regression | `.venv/bin/python -m pytest -q tests/test_model_validation.py` | 1 | 1 | [output](evidence/before-red-regression.txt) |
| green-tests | `.venv/bin/python -m pytest -q` | 0 | 0 | [output](evidence/before-green-tests.txt) |
| cli | `PYTHONPATH=src .venv/bin/python -m customer_search ana` | 0 | 0 | [output](evidence/before-cli.txt) |
| scope | `git status --short` | 0 | 0 | [output](evidence/before-scope.txt) |

## Validation Coverage and Skips

I confirmed a baseline of 25 passing cases. I added ten focused task cases; I observed six invalid-ID cases fail and four compatibility/immutability cases pass before the fix. I then observed 35 passing cases after the fix. I obtained CLI output `C001 | Ana López | ana.lopez@example.com` and exit 0.

I did not run a canonical lint, repository checker or CI in BEFORE because none existed in that baseline. I recorded their absence through a successful file-presence probe rather than a fabricated failed command. I did not count dependency setup or source discovery as controlled task errors.

## Final Assessment

I mark **functional result: PASS** because the acceptance regression, inherited tests, CLI behavior and scoped patch passed. I mark **strict experimental protocol: PARTIAL** because I did not use an independent independent agent state. I do not present a functional PASS as proof of clean-session comparability or a causal readiness effect.
