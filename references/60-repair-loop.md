# Repair Loop

Use this file when the task is not only to review but also to repair.

## Loop
1. Identify the highest-signal defect or design flaw.
2. Run the Fix Gate: evidence, impact, smallest fix, validation.
3. Make the smallest change that fixes the actual problem.
4. Keep the fix aligned with local patterns and existing APIs.
5. Re-run the narrowest relevant checks: tests, lint, typecheck, or screenshot verification.
6. Review the new state again.
7. Run the convergence pass in `references/65-convergence.md`.
8. Repeat until there are no remaining high-signal issues in the reviewed scope.

## Stop conditions
- Remaining issues are cosmetic or subjective.
- Further change would be speculative without more context.
- The next fix would be too broad for the current task.
- Validation is blocked by missing repo setup or missing tool access.
- A broader second pass would require a new scope, service action, credentials, or production operation.

## Guardrails
- Do not pile on unrelated refactors.
- Do not widen the blast radius just to make the code look cleaner.
- Preserve behavior unless the change is explicitly a behavior fix.
- Keep each pass small enough to verify.
- After each repair, re-check the diff for new public behavior, brittle tests, weakened validation, or intent drift.
- Do not claim the whole project is clean unless the whole project was actually reviewed.
- Do not delete redundant-looking code unless dependency, migration, fixture, and public-contract risk were checked.
- If validation cannot be run, keep the fix smaller and report the exact unverified risk.
