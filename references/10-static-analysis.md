# Static Analysis

Use this file for lint, type, compile, and structural checks.

## Read first
- Repo lint, format, type, compile, test, security, coverage, and CI config.
- Existing quality-gate thresholds and ignore/baseline files.

## Checks
- Prefer repo-local rules, overrides, and baselines.
- Treat compile or type failures as blockers.
- Treat warning-only lint as a real issue when the repo policy says so.
- Flag unsafe casts, broad exception handling, dead branches, unused code, and hidden side effects.
- Flag repeated logic or copied validation that should be centralized.

## Complexity
- Circle complexity above 10 is a refactor candidate.
- Above 15 needs clear justification.
- Split only when the refactor reduces risk or clarifies a boundary.

## Good review moves
- Point to the exact function or expression.
- Explain the behavioral risk, not just the style issue.
- Suggest the smallest fix that aligns with existing project patterns.
