# Restructure Pass

Use this file when code structure is poor, repetitive, or hard to maintain.

## Goal
Preserve every existing capability while improving:
- clarity
- cohesion
- duplication
- safety
- brevity
- testability

## Default moves
- Extract duplicated logic into one helper.
- Move repeated validation or formatting into a shared function.
- Split oversized functions into smaller single-purpose helpers.
- Replace ad hoc branching with a clearer data flow.
- Prefer the shorter implementation if it is equally safe and easier to verify.
- If repeated caller logic exists, move it behind the module interface instead of copying fixes across callers.

## Function review
For each function, ask:
1. Can this be shorter without losing behavior?
2. Can this be safer with fewer edge cases?
3. Can this be faster without adding complexity?
4. Can this be easier to read and maintain?

If the answer is yes, replace it with the better implementation.

## Module review
For each changed module, ask:
1. Does every caller need to know too much about ordering, validation, config, errors, or data shape?
2. Would deleting this module remove complexity, or would the same complexity reappear across callers?
3. Are tests forced to reach past the public interface to prove behavior?
4. Is there an extra interface or adapter with only one real implementation?

If caller knowledge is high or behavior is scattered, use `references/85-architecture-deepening.md`.

## Guardrails
- Do not remove capabilities.
- Do not change public behavior unless the task explicitly allows it.
- Do not broaden the scope just to make code look elegant.
- Keep refactors local and reviewable.

## After restructure
- Rebuild the project intent map.
- Re-run the relevant tests and checks.
- Verify that no public behavior regressed.
