# My Traceability Matrix

I keep normative requirements and acceptance criteria in their root sources. I use this matrix to locate evidence rather than redefine behavior.

| Requirement | AC | Task | Implementation I inspect | Executable evidence I run |
|---|---|---|---|---|
| FR-01 | AC-01 | T-03 | `search.py` | `test_partial_name_search`, `test_partial_email_search` |
| FR-02 | AC-02 | T-03 | `search.py` | `test_partial_name_search` |
| FR-03 | AC-03 | T-03 | `search.py` | `test_case_insensitive_and_trimmed`, `test_unicode_casefold_matches_name_and_email` |
| FR-04 | AC-04 | T-02, T-04 | `models.py`, `cli.py` | `test_model_has_required_fields`, `test_cli_prints_customer_fields` |
| FR-04 | AC-10 | T-02, T-05 | `models.py` | `test_customer_rejects_invalid_id`, `test_customer_preserves_nonempty_text_id`, `test_customer_remains_frozen` |
| FR-05 | AC-05 | T-04 | `cli.py` | `test_cli_reports_no_matches`, `test_no_matches_returns_empty_list` |
| FR-06 | AC-06 | T-04 | `search.py`, `cli.py` | `test_empty_term_is_rejected`, `test_non_text_term_is_rejected`, `test_cli_rejects_blank_term`, `test_cli_requires_exactly_one_argument` |
| NFR-01 | AC-07 | T-05 | `tests/` | I run the entire pytest suite. |
| NFR-02 | AC-08 | T-01 | `pyproject.toml`, `src/` | I run the CLI without network; I check empty runtime dependencies. |
| NFR-03 | AC-09 | T-06 | `README.md` | I execute the documented install and verify commands. |

I retain additional tests for internal spaces, generators and order in `test_search.py` and `test_cli.py`. I retain separate logs for BEFORE and AFTER so I do not mistake historical claims for current execution. I link guardrail evidence through `tests/test_repo_contract.py` and the command ledgers in `results/evidence/`.
