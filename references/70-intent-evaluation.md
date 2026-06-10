# Intent Evaluation

Use this file on every review and every repair pass.

## Build the intent map
Start from high-level project anchors:
- README / docs
- ADRs / design notes
- task or issue docs
- tests and fixtures
- public API / routes / CLI
- config files

Keep it lightweight. Do not sweep the whole repo unless the anchors are weak or contradictory.

## Intent block
Before findings, write a short intent block:
- Goal
- Non-goals
- Constraints
- Success criteria

## Review rule
Judge code against both:
1. The explicit/derived intent
2. The technical correctness and quality gates

If implementation is technically correct but misses intent, mark it as `Intent Miss`.

## Priority order
1. Task / issue / PR description
2. Repo docs / ADRs / README
3. Tests / fixtures
4. Existing public behavior
5. Nearby code

If these conflict, follow the order above.

## Ambiguity rule
- Infer conservatively.
- Mark unresolved ambiguity as `Intent Risk`.
- Ask only when the ambiguity changes behavior, scope, data migration, authorization, or API contract.

## Hard blocker
`Intent Miss` is a blocker even if the code compiles and tests pass.

## Repair loop
Rebuild the intent map on every repair pass.
Re-check the changed code against the new intent before deciding that the work is done.
