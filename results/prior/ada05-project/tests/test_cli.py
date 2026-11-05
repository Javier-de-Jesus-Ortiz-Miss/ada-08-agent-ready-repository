import os
import subprocess
import sys
from pathlib import Path

import pytest


def run_cli(*arguments):
    env = os.environ.copy()
    src = str(Path(__file__).resolve().parents[1] / "src")
    env["PYTHONPATH"] = os.pathsep.join(filter(None, [src, env.get("PYTHONPATH")]))
    return subprocess.run(
        [sys.executable, "-m", "customer_search", *arguments],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )


def test_cli_prints_customer_fields():
    result = run_cli("ana")
    assert result.returncode == 0
    assert "C001 | Ana López | ana.lopez@example.com" in result.stdout


def test_cli_reports_no_matches():
    result = run_cli("inexistente")
    assert result.returncode == 0
    assert result.stdout.strip() == "No se encontraron clientes."


@pytest.mark.parametrize("term", ["", "   ", "\t\n"])
def test_cli_rejects_blank_term(term):
    result = run_cli(term)
    assert result.returncode == 2
    assert "Error:" in result.stderr
    assert "no vacío" in result.stderr
    assert result.stdout == ""


def test_cli_requires_exactly_one_argument():
    for arguments in [(), ("ana", "bruno")]:
        result = run_cli(*arguments)
        assert result.returncode == 2
        assert "usage:" in result.stderr


def test_cli_trims_outer_spaces_and_preserves_inner_spaces():
    result = run_cli("  ANA LÓPEZ  ")
    assert result.returncode == 0
    assert result.stdout.strip() == "C001 | Ana López | ana.lopez@example.com"
    assert result.stderr == ""
