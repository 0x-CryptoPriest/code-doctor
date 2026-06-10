import Foundation

func expect(_ condition: @autoclosure () -> Bool, _ message: String) {
    if !condition() {
        fatalError(message)
    }
}

let ledger = Ledger()
ledger.add(id: "t1", ownerID: "alice", amountCents: 1200, note: "lunch")
ledger.add(id: "t2", ownerID: "alice", amountCents: 300, note: "coffee")

expect(ledger.visibleEntries(for: "alice").map(\.id) == ["t1", "t2"], "expected alice entries")
expect(ledger.totalCents(for: "alice") == 1500, "expected alice total")

ledger.delete(id: "t1", by: "alice")
expect(ledger.visibleEntries(for: "alice").map(\.id) == ["t2"], "delete should hide entry")
