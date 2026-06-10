# Python Ledger Fixture Intent

The ledger stores transactions for multiple users in one SQLite database.

Required behavior:
- Users can create, list, soft-delete, summarize, and export only their own transactions.
- Deleted transactions are hidden by default and scoped to the same owner when included.
- Money is exact to cents.
- Export filenames must stay inside the configured export directory.
- Audit logs may record event type and user, but not full memo text because memos can contain secrets.
- The fixture uses only Python stdlib.

Non-goals:
- No web server, ORM, async worker, or external service.
- No encryption or account-management model.
