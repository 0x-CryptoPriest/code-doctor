# Peer Review

Use this file for architectural, behavioral, and PR-quality judgment.

## Checks
- Correctness under the intended inputs.
- Backward compatibility and migration impact.
- Boundary clarity between modules.
- Naming, API shape, and error handling.
- Logging, observability, and rollback risk.
- Scope creep and unrelated churn.
- Diff size, reviewability, ownership, docs, release notes, and rollback plan for broad changes.

## What to flag
- Diff noise that hides the real change.
- Coupling across layers that should stay separate.
- Changes that are hard to revert.
- Missing docs, release notes, or rollout notes when the change is broad.
- Large diffs that should probably be split.
- Policy or ownership gaps when the change touches privileged paths, migrations, billing, auth, data export, or public APIs.

## Broad-change hygiene
- If behavior is public, trace it to docs, task intent, tests, or migration notes.
- If data changes, require migration, backfill, rollback, and compatibility evidence.
- If operational risk changes, require logging, metrics, alerting, or a rollback path that matches repo practice.
- If unrelated churn is mixed in, ask to split unless the churn is necessary for the fix.

## Review style
- Prefer fewer, stronger findings.
- Comment on the code that causes the risk.
- Give the specific reason the change is unsafe, not a generic preference.
