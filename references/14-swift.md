# Swift Playbook

Use this file for Swift, SwiftUI, iOS, macOS, and Swift concurrency changes.

## Read first
- Package or Xcode project settings, Swift version, deployment targets, tests, concurrency warnings.
- Existing architecture, state management, persistence, and UI navigation patterns.

## Blockers
- UI state mutated off the main actor.
- Unstructured tasks that can outlive the view/model owner without cancellation.
- Force unwraps, unchecked casts, or ignored throwing calls on user/data paths.
- Persistence, networking, or permission changes without migration and failure handling.
- Secrets, tokens, or private data stored or logged insecurely.

## Review checks
- Make actor isolation explicit for UI-facing models.
- Keep async work structured and cancellable; avoid detached tasks unless ownership is clear.
- Preserve public models, Codable shapes, deep links, and stored data compatibility.
- Prefer small domain methods over view-heavy business logic.
- Verify empty, loading, error, permission-denied, and offline states for user-visible changes.

## Repair moves
- Move side effects behind testable modules and keep SwiftUI views mostly declarative.
- Add tests around async ordering, cancellation, persistence migration, and error paths.
- Use the project toolchain; do not assume latest SDK APIs are available.
