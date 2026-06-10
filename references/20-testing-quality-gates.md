# Testing and Quality Gates

Use this file for unit, integration, e2e, and coverage checks.

## Read first
- Test files near the changed code
- CI config, coverage reports, and package scripts

## Checks
- Unit tests stay isolated from real network, database, and third-party services.
- New behavior has tests for success paths, edge cases, and regressions.
- Test failures should be deterministic.
- Prefer repo-native fixtures and mocks.
- Note missing integration or e2e coverage when the change is user-visible.

## Fallback gates
- Use repo thresholds first.
- If no thresholds exist, a practical fallback is:
  - core logic: line coverage >= 80%
  - shared libraries: line coverage >= 90%
  - branch coverage >= 75%
- Do not override stricter repo policy.

## Review moves
- Ask whether the test proves the bug cannot return.
- Call out tests that exercise only the happy path.
- Call out brittle tests that depend on timing, order, or external state.
