# Semantic Versioning Automation

This repository provides an automated solution for managing semantic versioning using Git hooks and Python. It ensures consistency and reduces manual errors by automating version updates during `git push` operations.

## Features
- Automatically bumps version numbers based on `MAJOR.MINOR.PATCH` rules.
- Updates the `VERSION` file and creates Git tags.
- Runs seamlessly with a `pre-push` Git hook.

## Prerequisites
- Python 3.x installed.
- A Git repository initialized in the project directory.

## Setup
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install the Git hooks**:
   Run the provided script to set up the `pre-push` hook:
   ```bash
   ./install-hooks.sh
   ```
   This script will:
   - Create a `.git/hooks/pre-push` file if it doesn’t exist.
   - Copy the `hooks/pre-push` file from the repository.
   - Make the hook executable.

3. **Verify the setup**:
   Ensure the `pre-push` hook is installed:
   ```bash
   ls .git/hooks/pre-push
   ```

## Usage
1. **Make changes and commit**:
   ```bash
   echo "Test file" > test.txt
   git add test.txt
   git commit -m "Test commit"
   ```

2. **Push with version bump**:
   Set the `BUMP_TYPE` environment variable to specify the version update:
   - **Major version**:
     ```bash
     BUMP_TYPE=major git push
     ```
   - **Minor version**:
     ```bash
     BUMP_TYPE=minor git push
     ```
   - **Patch version**:
     ```bash
     BUMP_TYPE=patch git push
     ```

3. **Skipping the hook** (if necessary):
   Use `--no-verify` to bypass the hook:
   ```bash
   git push --no-verify
   ```

## How It Works
- The `pre-push` hook runs before pushing changes to the remote repository.
- It triggers the `bump_version.py` script, which:
  1. Reads the current version from the `VERSION` file.
  2. Bumps the version based on `BUMP_TYPE`.
  3. Updates the `VERSION` file.
  4. Creates an annotated Git tag.

## Example Version Updates
- Current version: `1.2.3`
  - **Major bump**: `2.0.0`
  - **Minor bump**: `1.3.0`
  - **Patch bump**: `1.2.4`

## Troubleshooting
1. **Script not running**:
   - Ensure `install-hooks.sh` is executable:
     ```bash
     chmod +x install-hooks.sh
     ```

2. **Hook not triggering**:
   - Verify the hook is installed and executable:
     ```bash
     ls -l .git/hooks/pre-push
     ```

3. **Skipping the hook**:
   - Use `git push --no-verify` to bypass the hook.

4. **Duplicate tags**:
   - The `bump_version.py` script prevents duplicate tags by checking existing tags.

## Contributing
Feel free to open issues or submit pull requests for improvements and new features.

Author, CheikhM Bxxx

