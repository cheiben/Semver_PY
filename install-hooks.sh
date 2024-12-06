#!/usr/bin/env bash

set -euo pipefail

main() {
    local repo_hook_file="hooks/pre-push"
    local pre_push_hook=".git/hooks/pre-push"

    # Validate Git repository
    [[ -d ".git/hooks" ]] || {
        echo "Error: Not in a Git repository. Run this script from the repository root." >&2
        exit 1
    }

    # Validate hook source file
    [[ -f "$repo_hook_file" ]] || {
        echo "Error: Hook file '$repo_hook_file' does not exist." >&2
        exit 1
    }

    # Install hook
    mkdir -p "$(dirname "$pre_push_hook")"
    cp "$repo_hook_file" "$pre_push_hook"
    chmod +x "$pre_push_hook"

    echo "pre-push hook installed successfully."
}

main "$@"

##./install-hooks.sh##
