# Gold Review Output

Intent
Goal: Let owners export only their own active ledger entries as CSV.
Non-goals: No schema redesign, no new export format, no async job system.
Constraints: Preserve existing CLI flags, local SQLite storage, and CSV column order.
Success criteria: Cross-user entries cannot leak; traversal filenames are rejected; existing export tests pass.

Coverage
Reviewed: Export path, owner filtering, CSV output, nearby public tests, fixture intent.
Not reviewed: Broader import flow and money summary because they are outside the export change.
Second-pass check: Rechecked adjacent deleted-entry and path handling; no additional export blockers found.

Findings

P0 Intent Miss - `ledger.py:88`
Evidence: `export_csv(user_id, filename)` accepts `user_id` but `list_transactions(..., include_deleted=True)` drops the user filter.
Impact: A user export can include another user's deleted or active records, which violates the ownership intent even if the CSV generation works.
Fix: Keep the owner predicate in every export query, including include-deleted paths, and add a regression test with two users.

P1 Security - `ledger.py:92`
Evidence: `self.export_dir / filename` is used without resolving and checking containment.
Impact: `../outside.csv` can write outside the export directory.
Fix: Resolve the target path, require it to stay under the resolved export directory, and reject traversal.

P2 Test Gap - `tests/test_public.py:11`
Evidence: The tests cover a single user only.
Impact: The ownership bug can return without failing tests.
Fix: Add a two-user export test and a traversal rejection test.

Residual risk: Money rounding was not reviewed in this pass because the changed diff only touched export behavior.
