import assert from "node:assert/strict";
import test from "node:test";

import { renderUserRows } from "../src/UserDashboard.ts";

test("renders matching users in sorted order", () => {
  const session = { userId: "viewer-1", orgId: "org-a", teamId: "team-a", role: "viewer" };
  const users = [
    { id: "u2", orgId: "org-a", teamId: "team-a", name: "Zoey", active: true },
    { id: "u1", orgId: "org-a", teamId: "team-a", name: "Alice", active: true },
  ];

  const rows = renderUserRows(session, users, "");

  assert.deepEqual(rows.map((row) => row.label), ["Alice", "Zoey"]);
});

test("admin can render users", () => {
  const session = { userId: "admin-1", orgId: "org-a", teamId: "team-admin", role: "admin" };
  const users = [{ id: "u1", orgId: "org-a", teamId: "team-b", name: "Bea", active: true }];

  const rows = renderUserRows(session, users, "bea");

  assert.equal(rows.length, 1);
  assert.equal(rows[0].profileHref, "/users/u1?next=/dashboard");
});
