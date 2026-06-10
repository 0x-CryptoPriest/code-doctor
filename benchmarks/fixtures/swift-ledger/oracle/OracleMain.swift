import Foundation

func expect(_ condition: @autoclosure () -> Bool, _ message: String) {
    if !condition() {
        fatalError(message)
    }
}

do {
    let ledger = Ledger()
    ledger.add(id: "t1", ownerID: "alice", amountCents: 1200, note: "private")
    ledger.delete(id: "t1", by: "bob")
    expect(ledger.visibleEntries(for: "alice").map(\.id) == ["t1"], "delete must require owner")
}

do {
    let ledger = Ledger()
    ledger.add(id: "a1", ownerID: "alice", amountCents: 100, note: "alice")
    ledger.add(id: "b1", ownerID: "bob", amountCents: 200, note: "bob")
    ledger.delete(id: "a1", by: "alice")
    let ownerIDs = Set(ledger.visibleEntries(for: "alice", includeDeleted: true).map(\.ownerID))
    expect(ownerIDs == ["alice"], "includeDeleted must stay scoped to owner")
}

do {
    let ledger = Ledger()
    ledger.add(id: "bad", ownerID: "alice", amountCents: -500, note: "bad")
    expect(ledger.visibleEntries(for: "alice") == [], "negative amounts must be rejected")
    expect(ledger.totalCents(for: "alice") == 0, "negative amounts must not affect total")
}

do {
    let ledger = Ledger()
    ledger.add(id: "t1", ownerID: "alice", amountCents: 100, note: "token=secret")
    expect(!ledger.auditLog.contains { $0.contains("secret") }, "audit log must not store full note")
}
