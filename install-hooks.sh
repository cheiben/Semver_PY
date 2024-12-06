#!/bin/bash

echo "Installing Git hooks..."

# Ensure we are in a Git repository
if [ ! -d ".git/hooks" ]; then
    echo "Error: Not in a Git repository. Run this script from the root of a Git repository."
    exit 1
fi

# Path to the pre-push file in your repository
REPO_HOOK_FILE="hooks/pre-push"

# Ensure the source pre-push file exists in the repository
if [ ! -f "$REPO_HOOK_FILE" ]; then
    echo "Error: The file '$REPO_HOOK_FILE' does not exist in your repository."
    exit 1
fi

# Path to the destination pre-push hook
PRE_PUSH_HOOK=".git/hooks/pre-push"

# Create the pre-push file in .git/hooks if it doesn't exist
if [ ! -f "$PRE_PUSH_HOOK" ]; then
    echo "Creating pre-push hook in .git/hooks..."
    touch "$PRE_PUSH_HOOK"
fi

# Copy the content from hooks/pre-push in the repository to .git/hooks/pre-push
cp "$REPO_HOOK_FILE" "$PRE_PUSH_HOOK"

# Ensure the pre-push hook is executable
chmod +x "$PRE_PUSH_HOOK"

echo "pre-push hook installed successfully."

## Setting Up Git Hooks
#After cloning the repository, run the following command to set up Git hooks:

# chmod +x ./install-hooks.sh  ```
