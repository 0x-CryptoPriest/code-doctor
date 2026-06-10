import Foundation

public struct LedgerEntry: Equatable, Identifiable {
    public let id: String
    public let ownerID: String
    public let amountCents: Int
    public let note: String
    public var deleted: Bool
}

public final class Ledger {
    public private(set) var entries: [LedgerEntry] = []
    public private(set) var auditLog: [String] = []

    public init() {}

    public func add(id: String, ownerID: String, amountCents: Int, note: String) {
        let entry = LedgerEntry(
            id: id,
            ownerID: ownerID,
            amountCents: amountCents,
            note: note,
            deleted: false
        )
        entries.append(entry)
        auditLog.append("add \(id) for \(ownerID): \(note)")
    }

    public func visibleEntries(for ownerID: String, includeDeleted: Bool = false) -> [LedgerEntry] {
        if includeDeleted {
            return entries
        }
        return entries.filter { $0.ownerID == ownerID && !$0.deleted }
    }

    public func delete(id: String, by ownerID: String) {
        guard let index = entries.firstIndex(where: { $0.id == id }) else {
            return
        }
        entries[index].deleted = true
        auditLog.append("delete \(id) by \(ownerID)")
    }

    public func totalCents(for ownerID: String) -> Int {
        visibleEntries(for: ownerID).reduce(0) { total, entry in
            total + entry.amountCents
        }
    }
}
