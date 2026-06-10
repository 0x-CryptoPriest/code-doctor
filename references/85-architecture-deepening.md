# Architecture Deepening

Use this file when code is correct but the structure makes change, testing, or review harder than it should be.

## Vocabulary
- Module: any function, class, package, or slice with a public surface and implementation.
- Interface: everything callers must know: types, invariants, ordering, errors, config, data shape, and performance expectations.
- Implementation: the code hidden behind the interface.
- Depth: how much useful behavior sits behind a small interface.
- Adapter: a concrete implementation used to cross a real variation point.
- Leverage: capability callers get without learning more details.
- Locality: change, bugs, and verification concentrated in one place.

## Signals
- Callers repeat validation, branching, formatting, retries, authorization, or mapping.
- A module mostly passes data through while callers still carry the real complexity.
- Understanding one behavior requires bouncing through many tiny files.
- Tests prove behavior by reaching into internals instead of using the public interface.
- A new interface or adapter has only one real implementation and no concrete test or runtime variation.
- A pure helper was extracted for testability, but the bug risk lives in how every caller invokes it.

## Checks
- Deletion test: if deleting the module removes complexity, it was shallow; if complexity reappears across callers, it was useful.
- Interface test: callers and tests should prove behavior through the same public interface.
- Adapter test: one adapter is usually speculative; two justified adapters make the variation real.
- Locality test: a bug fix should land in one module, not across many callers.

## Repair moves
- Move repeated caller logic behind the module interface.
- Merge shallow modules when their split creates more caller knowledge than leverage.
- Keep internal seams private; do not expose them only for tests.
- For owned remote dependencies, keep domain logic in the module and inject the transport as an adapter.
- For true external dependencies, inject a narrow adapter and test behavior with a fake or mock adapter.
- Replace tests on shallow internals with behavior tests at the deepened interface once coverage is equivalent.

## Guardrails
- Do not invent an interface before a real variation exists.
- Do not hide behavior that callers legitimately need to control.
- Do not rewrite broad architecture during a narrow bug fix unless the current structure blocks a correct fix.
- Preserve public behavior unless the intent says to change it.
