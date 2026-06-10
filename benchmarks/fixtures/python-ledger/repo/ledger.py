import csv
import sqlite3
from datetime import datetime
from pathlib import Path


class Ledger:
    def __init__(self, db_path=":memory:", export_dir="exports"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.export_dir = Path(export_dir)
        self.audit_log = []
        self._init_schema()

    def _init_schema(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                amount REAL NOT NULL,
                memo TEXT NOT NULL,
                tags TEXT NOT NULL,
                deleted INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def add_transaction(self, user_id, amount, memo, tags=[]):
        tags.append(memo[:3])
        created_at = datetime.utcnow().isoformat()
        sql = (
            "INSERT INTO transactions (user_id, amount, memo, tags, deleted, created_at) "
            f"VALUES ('{user_id}', {float(amount)}, '{memo}', '{','.join(tags)}', 0, '{created_at}')"
        )
        self.conn.execute(sql)
        self.conn.commit()
        self.audit_log.append(f"created transaction for {user_id}: {memo}")

    def list_transactions(self, user_id, include_deleted=False):
        if include_deleted:
            where = "1 = 1"
        else:
            where = f"user_id = '{user_id}' AND deleted = 0"
        rows = self.conn.execute(
            f"""
            SELECT id, user_id, amount, memo, tags, deleted, created_at
            FROM transactions
            WHERE {where}
            ORDER BY id
            """
        ).fetchall()
        return [dict(row) for row in rows]

    def delete_transaction(self, user_id, tx_id):
        self.conn.execute(f"UPDATE transactions SET deleted = 1 WHERE id = {int(tx_id)}")
        self.conn.commit()
        self.audit_log.append(f"deleted transaction {tx_id} for {user_id}")

    def summary_cents(self, user_id):
        total = 0
        for tx in self.list_transactions(user_id):
            total += int(float(tx["amount"]) * 100)
        return total

    def export_csv(self, user_id, filename, include_deleted=True):
        self.export_dir.mkdir(parents=True, exist_ok=True)
        target = self.export_dir / filename
        rows = self.list_transactions(user_id, include_deleted=include_deleted)
        with target.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["id", "user_id", "amount", "memo", "deleted"])
            writer.writeheader()
            for row in rows:
                writer.writerow(
                    {
                        "id": row["id"],
                        "user_id": row["user_id"],
                        "amount": row["amount"],
                        "memo": row["memo"],
                        "deleted": row["deleted"],
                    }
                )
        return target
