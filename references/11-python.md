# Python Playbook

Use this file for Python application, library, CLI, data, and test changes.

## Read first
- `pyproject.toml`, `setup.cfg`, `tox.ini`, `ruff`, `mypy`, `pytest`, package layout, CI.
- Nearby tests and fixtures before changing behavior.

## Blockers
- SQL, shell, template, pickle, YAML, path, or deserialization injection.
- Broad `except` that hides correctness, security, or data loss.
- Mutable defaults, shared global state, or implicit cache state that crosses requests/tests.
- Money or exact user-visible quantities represented with unsafe floating-point behavior.
- Naive datetimes in persisted or cross-time-zone behavior.
- Blocking I/O inside async request paths.

## Review checks
- Preserve public imports, CLI flags, serialized formats, and exception contracts.
- Prefer repo-native validation models and typed boundaries; do not add a new validation stack casually.
- Use `pathlib` plus base-directory containment for file access.
- Use parameterized SQL and argument-list subprocess calls; avoid `shell=True`.
- Keep resource ownership explicit: context managers for files, DB connections, locks, and temp dirs.
- Prefer deterministic tests over sleeps, live network, real clocks, or shared temp paths.

## Repair moves
- Patch the narrow failing behavior first, then simplify duplicated validation.
- Add regression tests for the exact bug and one adjacent edge case.
- If a helper exists only to make tests easy, consider testing through the caller-facing module instead.
