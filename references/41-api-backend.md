# Backend API Playbook

Use this file for HTTP, RPC, queue, database, migration, and service-boundary changes.

## Intent checks
- Identify the caller, trust level, data owner, compatibility contract, and rollback path.
- Confirm whether behavior is public API, internal API, admin-only, async job, or migration.

## Blockers
- Missing authentication or authorization at the server-side decision point.
- Cross-tenant or cross-user data access.
- Non-idempotent retries, duplicate writes, or unsafe partial failures.
- Missing transaction boundary around multi-step state changes.
- Unbounded queries, missing pagination, or N+1 behavior on user-controlled sizes.
- Schema or contract changes without migration, backfill, versioning, or rollback notes.

## Review checks
- Validate input at the boundary and enforce invariants in the domain layer.
- Use precise status codes and machine-readable errors where the repo already does.
- Make rate limits, timeouts, retries, and idempotency explicit.
- Log request correlation and decision outcomes without secrets or PII.
- Keep domain rules out of transport adapters when possible.

## Repair moves
- Add regression tests for ownership, retry, empty, limit, and concurrent write paths.
- Add migration tests or compatibility tests when persisted data or public contracts change.
- Prefer one deep module that owns the state transition over duplicated route-level logic.
