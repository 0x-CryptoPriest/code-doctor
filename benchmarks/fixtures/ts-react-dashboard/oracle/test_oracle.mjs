import assert from "node:assert/strict";
import path from "node:path";
import test from "node:test";
import { pathToFileURL } from "node:url";

const candidateDir = process.env.CANDIDATE_DIR;
const moduleUrl = pathToFileURL(path.join(candidateDir, "src", "UserDashboard.ts")).href;
const { renderUserRows } = await import(moduleUrl);

test("viewer cannot see users from another organization with same team id", () => {
  const session = { userId: "viewer-1", orgId: "org-a", teamId: "shared-team", role: "viewer" };
  const users = [
    { id: "u1", orgId: "org-a", teamId: "shared-team", name: "Alice", active: true },
    { id: "u2", orgId: "org-b", teamId: "shared-team", name: "Mallory", active: true },
  ];

  const rows = renderUserRows(session, users);

  assert.deepEqual(rows.map((row) => row.id), ["u1"]);
});

test("admin is still scoped to their organization", () => {
  const session = { userId: "admin-1", orgId: "org-a", teamId: "admin", role: "admin" };
  const users = [
    { id: "u1", orgId: "org-a", teamId: "team-a", name: "Alice", active: true },
    { id: "u2", orgId: "org-b", teamId: "team-b", name: "Mallory", active: true },
  ];

  const rows = renderUserRows(session, users);

  assert.deepEqual(rows.map((row) => row.id), ["u1"]);
});

test("inactive users are hidden", () => {
  const session = { userId: "viewer-1", orgId: "org-a", teamId: "team-a", role: "viewer" };
  const users = [{ id: "u1", orgId: "org-a", teamId: "team-a", name: "Dormant", active: false }];

  assert.deepEqual(renderUserRows(session, users), []);
});

test("rendering does not mutate caller array order", () => {
  const session = { userId: "viewer-1", orgId: "org-a", teamId: "team-a", role: "viewer" };
  const users = [
    { id: "u2", orgId: "org-a", teamId: "team-a", name: "Zoey", active: true },
    { id: "u1", orgId: "org-a", teamId: "team-a", name: "Alice", active: true },
  ];

  renderUserRows(session, users);

  assert.deepEqual(users.map((user) => user.id), ["u2", "u1"]);
});

test("rows use stable user ids as keys", () => {
  const session = { userId: "viewer-1", orgId: "org-a", teamId: "team-a", role: "viewer" };
  const users = [
    { id: "u2", orgId: "org-a", teamId: "team-a", name: "Zoey", active: true },
    { id: "u1", orgId: "org-a", teamId: "team-a", name: "Alice", active: true },
  ];

  const rows = renderUserRows(session, users);

  assert.deepEqual(rows.map((row) => row.key), ["u1", "u2"]);
});

test("raw display HTML is not preserved in render output", () => {
  const session = { userId: "viewer-1", orgId: "org-a", teamId: "team-a", role: "viewer" };
  const users = [
    { id: "u1", orgId: "org-a", teamId: "team-a", name: "<img src=x onerror=alert(1)>", active: true },
  ];

  const rows = renderUserRows(session, users);
  const html = String(rows[0]?.html ?? "");

  assert.equal(html.includes("<img"), false);
  assert.equal(html.includes("onerror"), false);
});

test("profile links reject external next targets", () => {
  const session = { userId: "viewer-1", orgId: "org-a", teamId: "team-a", role: "viewer" };
  const users = [
    {
      id: "u1",
      orgId: "org-a",
      teamId: "team-a",
      name: "Alice",
      active: true,
      next: "//evil.test/phish",
    },
  ];

  const rows = renderUserRows(session, users);

  assert.equal(rows[0].profileHref.includes("evil.test"), false);
});
