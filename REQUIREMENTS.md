# Requirements - Customer Search

## User Story

I need to find an existing customer by a single name or email search term.

## Functional Requirements

- **FR-01 - Unified search:** I accept one term and search both customer names and email addresses.
- **FR-02 - Partial match:** I return a customer when the term is a substring of either field; I do not require an exact match.
- **FR-03 - Case independence:** I return the same matches regardless of the casing of the query or data.
- **FR-04 - Identifiable results:** I show at least the customer identifier, name and email for each result.
- **FR-05 - No matches:** I report that no customers were found and do not show unrelated records.
- **FR-06 - Query validation:** I reject empty or whitespace-only terms and provide a useful corrective message.

## Nonfunctional Requirements

- **NFR-01 - Automated tests:** I verify search and validation through executable pytest tests.
- **NFR-02 - Local execution:** I run without external services or paid APIs.
- **NFR-03 - Reproducible environment:** I document installation, execution and testing with Python 3.11+.

## Resolved Questions

- **Q-01:** I use the small fictional dataset included in the project.
- **Q-02:** I preserve the input record order.

## Constraints and Assumptions

- **C-01:** I retain the original project scope and use free tools.
- **C-02:** I preserve the historical ADA-05 requirement to use Antigravity CLI in the archived original. For ADA-08 I use Codex and record the tool identifier in the experiment protocol.
- **C-03:** I keep an AI usage log for decisions that affect the product or repository.
- **A-01:** I use a Python CLI with in-memory data, no database and no HTTP API.
- **A-02:** I search existing records; I exclude customer creation, editing and deletion.

## Change Control

I preserve the inherited FR/NFR IDs and behavior. I translate this active contract into English and first person for ADA-08. I clarify the existing non-empty textual customer ID invariant only in the Domain Model and AC-10 of `SPEC.md`; I do not introduce a separate filtering or persistence feature. I retain original documents in `results/prior/ada05-project/`.
