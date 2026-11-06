#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
if [[ -n "${PYTHON:-}" ]]; then
  VERIFY_PYTHON="$PYTHON"
elif [[ -x "$REPO_ROOT/.venv/bin/python" ]]; then
  VERIFY_PYTHON="$REPO_ROOT/.venv/bin/python"
else
  VERIFY_PYTHON="python3"
fi
export PYTHONHASHSEED=0
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYTHONDONTWRITEBYTECODE=1

"$VERIFY_PYTHON" -c 'import sys; assert sys.version_info >= (3, 11), "Python 3.11+ required"'
echo "[1/3] Running tests"
"$VERIFY_PYTHON" -m pytest -q -p no:cacheprovider
echo "[2/3] Running lint"
"$VERIFY_PYTHON" -m ruff check src tests scripts
echo "[3/3] Checking repository contract"
"$VERIFY_PYTHON" scripts/check_repo_contract.py
echo "VERIFY_REPO: PASS"
