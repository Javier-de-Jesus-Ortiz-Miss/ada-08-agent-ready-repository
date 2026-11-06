"""I test adversarial repository mutations without modifying my real evidence."""

import importlib.util
import json
from pathlib import Path
import shutil

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('repo_contract', ROOT / 'scripts/check_repo_contract.py')
CONTRACT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CONTRACT)


@pytest.fixture
def repository(tmp_path):
    clone = tmp_path / 'repository'
    shutil.copytree(
        ROOT, clone,
        ignore=shutil.ignore_patterns('.git', '.venv', 'work', 'outputs', '__pycache__',
                                     '.pytest_cache', '.ruff_cache', '*.egg-info'),
    )
    return clone


def test_current_repository_satisfies_contract():
    assert CONTRACT.check(ROOT) == []


def test_missing_essential_file_is_detected(repository):
    (repository / 'SPEC.md').unlink()
    assert any('missing essential file: SPEC.md' in e for e in CONTRACT.check(repository))


def test_protected_data_mutation_is_detected(repository):
    with (repository / 'src/customer_search/data.py').open('a') as stream:
        stream.write('\n# unauthorized alteration\n')
    assert any('protected file changed' in e for e in CONTRACT.check(repository))


def test_removing_manifest_entry_does_not_bypass_guard(repository):
    path = repository / 'docs/protected-paths.json'
    manifest = json.loads(path.read_text())
    manifest['files'].pop('src/customer_search/data.py')
    path.write_text(json.dumps(manifest))
    assert any('cover exactly' in e for e in CONTRACT.check(repository))


def test_directory_symlink_cannot_supply_essential_contract(repository):
    original = repository / 'docs'
    original.rename(repository / 'other-docs')
    original.symlink_to(repository / 'other-docs', target_is_directory=True)
    assert any('symlink is forbidden' in e for e in CONTRACT.check(repository))


def test_heading_in_fence_is_not_a_contract_section(repository):
    path = repository / 'AGENTS.md'
    path.write_text(path.read_text().replace('## Stop Conditions', '```\n## Stop Conditions\n```'))
    assert any('heading missing/duplicated' in e for e in CONTRACT.check(repository))


def test_duplicate_contract_heading_is_detected(repository):
    path = repository / 'AGENTS.md'
    path.write_text(path.read_text() + '\n## Stop Conditions\nI stop.\n')
    assert any('heading missing/duplicated' in e for e in CONTRACT.check(repository))


def test_unknown_acceptance_reference_is_detected(repository):
    path = repository / 'TASK_UNDER_TEST.md'
    path.write_text(path.read_text().replace('AC-10', 'AC-99'))
    assert any('unresolved AC references' in e for e in CONTRACT.check(repository))


def test_broken_navigation_link_is_detected(repository):
    path = repository / 'docs/REPO_MAP.md'
    path.write_text(path.read_text() + '\nI use [missing](missing.md).\n')
    assert any('broken or escaping local link' in e for e in CONTRACT.check(repository))


def test_search_cannot_import_cli(repository):
    path = repository / 'src/customer_search/search.py'
    path.write_text(path.read_text() + '\nfrom . import cli\n')
    assert any('architecture dependency violation' in e for e in CONTRACT.check(repository))


def test_domain_cannot_open_a_file(repository):
    path = repository / 'src/customer_search/models.py'
    path.write_text(path.read_text() + '\nopen("unexpected.txt", "w")\n')
    assert any('domain side-effect call' in e for e in CONTRACT.check(repository))


def test_runtime_dependency_cannot_be_added_silently(repository):
    path = repository / 'pyproject.toml'
    path.write_text(path.read_text().replace('dependencies = []', 'dependencies = ["requests"]'))
    assert any('runtime dependencies must remain empty' in e for e in CONTRACT.check(repository))


def test_sensitive_file_is_detected_without_reading_its_contents(repository):
    (repository / '.env').write_text('EXAMPLE_ONLY=not-a-real-secret\n')
    assert any('forbidden sensitive root path' in e for e in CONTRACT.check(repository))


def test_ci_cannot_replace_shared_gate(repository):
    path = repository / '.github/workflows/verify.yml'
    path.write_text(path.read_text().replace('run: ./scripts/verify_repo.sh', 'run: python -m pytest'))
    assert any('single shared verification' in e for e in CONTRACT.check(repository))


def test_ci_cannot_gain_write_permissions(repository):
    path = repository / '.github/workflows/verify.yml'
    path.write_text(path.read_text().replace('contents: read', 'contents: write'))
    assert any('CI permissions' in e for e in CONTRACT.check(repository))
