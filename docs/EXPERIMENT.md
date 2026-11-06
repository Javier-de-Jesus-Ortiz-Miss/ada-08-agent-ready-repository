# My ADA-08 Experiment Protocol

## Provenance and Baseline

I found this workspace empty and without Git history. I imported the existing customer-search project from `/Users/javierortiz/Downloads/ada-07-agent-skill/project`, rather than designing a new application. I compared the six Python source modules with my original ADA-05 folder under `/Users/javierortiz/Documents/ING SOFT IA/ADA05/ada-05-spec-driven-feature`; all six matched byte for byte. I preserved the imported ADA-07 source and technical reference files in `results/prior/`, with per-file hashes in `results/evidence/source-provenance.json`.

I clarified the existing non-empty textual identifier rule in SPEC/AC-10, created the fixed task, and preserved commit `ada08-baseline` as `ada08-baseline` before my initial audit and any task implementation. I did not deliberately degrade inherited instructions, architecture or tests. I retained the 25-test suite and existing AGENTS. I recorded my initial eight scores in `results/evidence/audit-before.json` before running BEFORE; the next Git commit preserves that ordering.

## Controlled Task and Task Input

I use CR-ADA08-01 and the exact official English task input stored in `docs/EXPERIMENT_PROMPT.txt`. I hash and protect both that input and `TASK_UNDER_TEST.md`. I use the same criteria for both runs. I keep the controlled task input separate from the technical decision log.

## Worktree Isolation

I created `experiment/before` at `work/before` and `experiment/after` at `work/after` from the same baseline. I implemented BEFORE only in its worktree and retained a patch. I confirmed that the untouched AFTER source and inherited tests still matched `results/evidence/functional-baseline.json` afterward. I then overlaid readiness files on AFTER, excluding all BEFORE implementation. I wrote AFTER from its original model file. I copied only the validated AFTER model and task test into the final active source tree.

I compare the same product change and acceptance criteria, rather than judging two different features. I allow equivalent implementation syntax; I compare observable behavior and file scope. I classify the extra `tests/test_repo_contract.py` as readiness infrastructure and distinguish it from the 25 inherited tests and 10 controlled regression cases.

## Constants and Variables

| Variable | What I held constant or recorded |
|---|---|
| Functional start | I retained byte-identical six source modules and inherited test files. |
| Task / official input | I retained identical protected task and input bytes. |
| Agent | I used Codex without resetting agent state between conditions. |
| Model | I did not receive an exact runtime model identifier; I do not infer it from the product name. |
| Tools / permissions | I used local shell, Python, pytest and Git with workspace writes. I used approved network access only to install tools and approved Git metadata writes. |
| Environment | I used Python 3.13 on macOS, pytest 8.4.2, Ruff 0.14.3 and PyYAML 6.0.3 in one `.venv`. I recorded exact versions in `results/evidence/environment.txt`. |
| Readiness treatment | I changed operational docs, navigation, verification scripts, guardrails, lint config and CI. I did not change product code before AFTER. |
| Session memory | I did not reset agent state between conditions. |
| Repetitions | I ran one implementation per condition; I did not estimate variance or statistical significance. |
| Human review | I retain automated command evidence; I record semantic review as a separate validation activity. |
| Remote CI | I authored and structurally checked the workflow. I did not publish, push or observe a GitHub Actions run. |

## Reproduction

I install the pinned tools as described in README and run `./scripts/verify_repo.sh`. I inspect the historical ledgers and patches under `results/evidence/` rather than overwriting them.

I can recover the complete baseline and refs from the delivered bundle:

```bash
git clone ADA-08-history.bundle ada08-review
cd ada08-review
git worktree add -b replay-before ../ada08-replay-before ada08-baseline
git worktree add -b replay-after ../ada08-replay-after ada08-baseline
```

I apply `results/evidence/readiness.patch` only to the replay-AFTER tree before task implementation. I obtain the fixed input from the baseline. I can run `git apply --check results/evidence/before.diff` against baseline and `git apply --check results/evidence/after.diff` against the readiness-only tree, adjusting the evidence path to the delivery root. I can replay the product patches to reproduce functional behavior; I do not confuse patch replay with a new autonomous agent measurement.

I obtain a fully valid behavioral comparison only by running the two prepared trees in independent clean agent sessions, providing the same official input and collecting fresh ledgers. I retain that as an uncompleted experimental condition in this delivery; I do not fabricate it.

## Metrics and Interpretation

I count clarification questions actually asked, context files explicitly read, unsupported assumptions, unexpected command failures, product files outside scope, and executed/skipped validation stages. I distinguish expected red regression failures from operational errors. I use `results/evidence/before-commands.json` and `after-commands.json` as the command-level source of truth.

I do not count task-authoring, PDF extraction, source discovery or dependency setup as BEFORE/AFTER agent friction. I separately disclose initial network DNS failure, the protected `.agents/` write restriction and Git metadata restrictions in `results/evidence/setup-notes.md`. I did not add fake failed commands to inflate the apparent improvement.

## Validity Decision

I mark functional validation PASS when behavior and scope pass. I mark strict experimental protocol PARTIAL because AFTER was not a clean session and the official input was a fixed specification for this continuing agent, not a separate agent invocation. I interpret the readiness score as my rubric assessment supported by artifacts and checks, not as an LLM benchmark or a causal estimate.
