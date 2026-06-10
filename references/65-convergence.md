# Convergence and Coverage

Use this file near the end of every non-trivial review or repair.

## Purpose
Reduce second-pass surprise. A later run may still find new issues, but it should be because the scope changed, not because the first pass failed to close its own scope.

## Coverage ledger
Track the review surface:
- Intent anchors read: task, README, ADRs, docs, tests, public API, config.
- Code read: diff files, nearby callers, callees, adapters, migrations, tests.
- Runtime evidence: commands, logs, service state, screenshots, or tool output.
- Explicit exclusions: files, services, credentials, production actions, or broad refactors not reviewed.

## Convergence pass
Before final output, ask:
1. If I ran this review again, which adjacent module would I inspect first?
2. Did the fix change a contract, config fallback, migration path, runtime target, or ownership rule?
3. Did tests improve only the happy path while leaving edge, auth, error, or concurrency paths untested?
4. Did a repair expose a new intent source, ADR, config, or caller that should be checked now?
5. Is any remaining issue truly out of scope, or just inconvenient?

## Output rule
For non-trivial work, add:
- Reviewed: concise list of anchors, files, commands, and risk surfaces checked.
- Not reviewed: explicit exclusions and why.
- Second-pass check: what was rechecked, and whether remaining items are blockers, deferred risks, or out of scope.

## Repeat reviews
When prior review notes exist:
- Read them as an intent anchor.
- Classify new findings as `missed-in-scope`, `new-scope`, `new-evidence`, or `post-fix-regression`.
- Treat `missed-in-scope` as a process failure and tighten the convergence pass.
- Treat `new-scope` as normal only if the first output clearly excluded that surface.
