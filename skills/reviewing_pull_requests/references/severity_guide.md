# Finding Severity Guide

## MUST FIX
Requirement/AC violation, introduced regression, required failing test, security or data integrity issue that prevents safe approval. Include evidence and a concrete next step.

## SHOULD FIX
Significant maintainability, architecture, testability or evidence clarity problem while the implemented feature can work. State why it matters and avoid presenting preferences as blockers.

## OPTIONAL
Non-blocking improvements with no change to approved behavior/safety. Do not manufacture style findings to populate this section.

## Evidence and uncertainty
Every finding contains Requirement / AC, File, Evidence, Problem, Recommended next step. If no normative requirement applies, write N/A with a reason. Use unique IDs RF-01, RF-02, ... across categories. Empty categories contain `None.`. Unsupported concerns belong in Open Questions. All reports require Human decision required: YES even with zero blockers.
