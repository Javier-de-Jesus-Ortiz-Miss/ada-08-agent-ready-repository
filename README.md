# Customer Search - ADA-08 Agent-Ready Repository

I evolved my existing ADA-05 Customer Search CLI and reused my ADA-07 review artifacts. I did not replace them with a new demonstration application. I imported a working copy into this initially empty workspace; I preserved technical reference files and original source hashes in `results/prior/` and `results/evidence/source-provenance.json`.

## Start Here

I start with [AGENTS.md](AGENTS.md), use [my repository map](docs/REPO_MAP.md) to find code and tests, and use [my fixed task](TASK_UNDER_TEST.md) for the experiment. I keep requirements, specification, architecture and tasks in their named root documents.

## Installation

I use Python 3.11 or later, Bash and Git. I install exact development/build tool versions; my application uses only the Python standard library at runtime.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m pip install --no-deps --no-build-isolation -e .
```

I need network access only to install dependencies or run hosted CI. I run the application and all verification locally without credentials.

## Run

```bash
.venv/bin/python -m customer_search ana
.venv/bin/customer-search example.com
PYTHONPATH=src python3 -m customer_search '  ANA LÓPEZ  '
```

I pass the term as one argument. I preserve Spanish user-facing messages, partial matching, Unicode casefold, input ordering and the documented CLI exit codes. I do not trim customer IDs: I preserve every non-empty textual ID exactly as specified.

## Validation

```bash
./scripts/verify_repo.sh
```

I use this same command for my own work, agent work and `.github/workflows/verify.yml`. I can run it from another directory; it resolves its root from the script location. I can select another installed environment with `PYTHON=/absolute/path/to/python`.

I run individual stages with `.venv/bin/python -m pytest -q`, `.venv/bin/python -m ruff check src tests scripts`, and `.venv/bin/python scripts/check_repo_contract.py`. I do not treat syntax compilation as lint.

## Experiment and Evidence

I preserved `ada08-baseline` before the audit and task. I used `experiment/before` and `experiment/after` worktrees from that same commit. I recorded the protocol, variables and reproducibility commands in [my experiment guide](docs/EXPERIMENT.md). I stored actual command output, exit codes, functional hashes, patches and protected-path mutation results in `results/evidence/`.

I obtained a readiness score of **61/100 BEFORE** and **91/100 AFTER**, a **+30 point delta**, subject to the evidence and limitations in [my audit](REPOSITORY_READINESS_AUDIT.md). I treat the agent experiment as **PARTIAL** because the agent state was not reset between conditions. I do not infer an independent behavioral improvement from that comparison.

## Delivery

I create a self-contained source archive and a Git bundle with `.venv/bin/python scripts/package_delivery.py`. I keep generated deliverables in `outputs/`; I exclude local environments and worktrees. I preserve history and experiment refs in the bundle because a ZIP alone cannot preserve a Git tag.

## Project Documentation

I document repository decisions and validation evidence. I preserve inherited technical artifacts in `results/prior/` and `skills/`, use English for agent-facing contracts and run reports, and retain traceability to the original product requirements.
