import tempfile
import unittest
from pathlib import Path

from ledger import Ledger


class LedgerOracleTests(unittest.TestCase):
    def make_ledger(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        return Ledger(root / "ledger.db", root / "exports"), root

    def test_delete_requires_owner(self):
        ledger, _ = self.make_ledger()
        ledger.add_transaction("alice", 5.00, "alice-private")
        tx_id = ledger.list_transactions("alice")[0]["id"]

        ledger.delete_transaction("bob", tx_id)

        self.assertEqual(len(ledger.list_transactions("alice")), 1)

    def test_include_deleted_stays_scoped_to_owner(self):
        ledger, _ = self.make_ledger()
        ledger.add_transaction("alice", 1.00, "alice")
        ledger.add_transaction("bob", 2.00, "bob")
        ledger.delete_transaction("alice", ledger.list_transactions("alice")[0]["id"])

        rows = ledger.list_transactions("alice", include_deleted=True)

        self.assertEqual({row["user_id"] for row in rows}, {"alice"})

    def test_user_id_cannot_inject_query(self):
        ledger, _ = self.make_ledger()
        ledger.add_transaction("alice", 1.00, "alice")
        ledger.add_transaction("bob", 2.00, "bob")

        rows = ledger.list_transactions("alice' OR '1'='1")

        self.assertEqual(rows, [])

    def test_negative_amount_is_rejected(self):
        ledger, _ = self.make_ledger()

        with self.assertRaises(ValueError):
            ledger.add_transaction("alice", -1.00, "refund shaped like income")

    def test_money_is_exact_to_cents(self):
        ledger, _ = self.make_ledger()
        ledger.add_transaction("alice", 0.29, "rounding trap")

        self.assertEqual(ledger.summary_cents("alice"), 29)

    def test_export_rejects_path_traversal(self):
        ledger, root = self.make_ledger()
        ledger.add_transaction("alice", 1.00, "export me")

        with self.assertRaises(ValueError):
            ledger.export_csv("alice", "../outside.csv")

        self.assertFalse((root / "outside.csv").exists())

    def test_audit_log_does_not_store_full_memo(self):
        ledger, _ = self.make_ledger()

        ledger.add_transaction("alice", 1.00, "password=secret-token")

        self.assertFalse(any("secret-token" in entry for entry in ledger.audit_log))


if __name__ == "__main__":
    unittest.main()
