import csv
import tempfile
import unittest
from pathlib import Path

from ledger import Ledger


class LedgerPublicTests(unittest.TestCase):
    def make_ledger(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        return Ledger(root / "ledger.db", root / "exports")

    def test_add_list_and_summary_for_single_user(self):
        ledger = self.make_ledger()

        ledger.add_transaction("alice", 12.50, "lunch")
        ledger.add_transaction("alice", 3.00, "coffee")

        rows = ledger.list_transactions("alice")

        self.assertEqual([row["memo"] for row in rows], ["lunch", "coffee"])
        self.assertEqual(ledger.summary_cents("alice"), 1550)

    def test_export_writes_expected_columns(self):
        ledger = self.make_ledger()
        ledger.add_transaction("alice", 4.25, "tea")

        path = ledger.export_csv("alice", "alice.csv", include_deleted=False)

        with path.open(newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(rows[0]["user_id"], "alice")
        self.assertEqual(rows[0]["memo"], "tea")
        self.assertEqual(set(rows[0].keys()), {"id", "user_id", "amount", "memo", "deleted"})


if __name__ == "__main__":
    unittest.main()
