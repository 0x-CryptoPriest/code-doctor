# Acceptance and UI

Use this file for product behavior, AC, and UI checks.

## Checks
- The change matches the ticket, PRD, or acceptance criteria.
- User-visible, API, CLI, migration, and data changes are traceable to an intent source.
- User-visible behavior is covered by tests or a reproducible check.
- UI layout is stable across target widths and content lengths.
- Text does not overflow or overlap.
- Interactive states, empty states, and error states exist where needed.
- Accessibility basics are not regressed.

## Review moves
- Call out exact acceptance criteria that are not met.
- If no acceptance source exists and behavior could reasonably vary, mark `Intent Risk`.
- Separate implementation detail from product requirement.
- Prefer screenshot or storybook evidence when the change affects UI.
