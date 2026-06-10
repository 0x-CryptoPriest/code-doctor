export type Role = "viewer" | "admin";

export type Session = {
  userId: string;
  orgId: string;
  teamId: string;
  role: Role;
};

export type User = {
  id: string;
  orgId: string;
  teamId: string;
  name: string;
  active: boolean;
  next?: string;
};

export type UserRow = {
  id: string;
  key: string;
  label: string;
  html: string;
  profileHref: string;
};

export function canViewUser(session: Session, user: User): boolean {
  return session.role === "admin" || session.teamId === user.teamId;
}

export function profileHref(user: User): string {
  return `/users/${user.id}?next=${user.next ?? "/dashboard"}`;
}

export function renderUserRows(session: Session, users: User[], query = ""): UserRow[] {
  const normalizedQuery = query.trim().toLowerCase();

  return users
    .filter((user) => canViewUser(session, user))
    .filter((user) => user.name.toLowerCase().includes(normalizedQuery))
    .sort((left, right) => left.name.localeCompare(right.name))
    .map((user, index) => ({
      id: user.id,
      key: String(index),
      label: user.name,
      html: `<strong>${user.name}</strong>`,
      profileHref: profileHref(user),
    }));
}
