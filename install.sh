#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="code-doctor"
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODEX_SKILLS_DIR="${CODEX_HOME:-"$HOME/.codex"}/skills"
CLAUDE_SKILLS_DIR="${CLAUDE_HOME:-"$HOME/.claude"}/skills"

install_codex=false
install_claude=false
force=false

usage() {
  cat <<'USAGE'
Usage: ./install.sh [--all|--codex|--claude] [--force]

Options:
  --all      Install for Codex and Claude. Default when no target is given.
  --codex    Install to $CODEX_HOME/skills/code-doctor, defaulting to ~/.codex/skills/code-doctor.
  --claude   Install to $CLAUDE_HOME/skills/code-doctor, defaulting to ~/.claude/skills/code-doctor.
  --force    Replace an existing code-doctor install.
  --help     Show this help.
USAGE
}

while (($#)); do
  case "$1" in
    --all)
      install_codex=true
      install_claude=true
      ;;
    --codex)
      install_codex=true
      ;;
    --claude)
      install_claude=true
      ;;
    --force)
      force=true
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

if [[ "$install_codex" == false && "$install_claude" == false ]]; then
  install_codex=true
  install_claude=true
fi

copy_skill() {
  local dest_root="$1"
  local dest="$dest_root/$SKILL_NAME"

  mkdir -p "$dest_root"
  if [[ -e "$dest" || -L "$dest" ]]; then
    if [[ "$force" != true ]]; then
      echo "Destination exists: $dest" >&2
      echo "Re-run with --force to replace it." >&2
      return 1
    fi
    rm -rf "$dest"
  fi

  rsync -a --delete \
    --exclude='.git' \
    --exclude='AGENTS.md' \
    --exclude='.DS_Store' \
    --exclude='__pycache__' \
    --exclude='.pytest_cache' \
    --exclude='.mypy_cache' \
    --exclude='.ruff_cache' \
    --exclude='.build' \
    --exclude='node_modules' \
    "$SOURCE_DIR/" "$dest/"
  echo "Installed $SKILL_NAME to $dest"
}

if [[ "$install_codex" == true ]]; then
  copy_skill "$CODEX_SKILLS_DIR"
fi

if [[ "$install_claude" == true ]]; then
  copy_skill "$CLAUDE_SKILLS_DIR"
fi

echo "Restart Codex or Claude to pick up updated skills."
