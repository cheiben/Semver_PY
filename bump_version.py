import sys
import re
import subprocess

def bump_version(version, part):
    major, minor, patch = map(int, version.split('.'))
    if part == 'major':
        major += 1
        minor = 0
        patch = 0
    elif part == 'minor':
        minor += 1
        patch = 0
    elif part == 'patch':
        patch += 1
    else:
        raise ValueError("Invalid version part. Use 'major', 'minor', or 'patch'.")
    return f"{major}.{minor}.{patch}"

def get_existing_tags():
    try:
        # Retrieve all existing tags in the repository
        result = subprocess.run(["git", "tag"], check=True, stdout=subprocess.PIPE, text=True)
        tags = result.stdout.splitlines()
        return tags
    except subprocess.CalledProcessError as e:
        print(f"Error fetching tags: {e}")
        sys.exit(1)

if __name__ == "__main__":
    version_file = 'VERSION'
    if len(sys.argv) != 2:
        print("Usage: python3 bump_version.py [major|minor|patch]")
        sys.exit(1)

    part = sys.argv[1]  # major, minor, or patch
    try:
        # Read the current version from the VERSION file
        with open(version_file, 'r') as f:
            current_version = f.read().strip()
        if not re.match(r'^\d+\.\d+\.\d+$', current_version):
            raise ValueError("Invalid version format in VERSION file.")
        
        # Bump the version
        new_version = bump_version(current_version, part)
        new_tag = f"v{new_version}"

        # Check for existing tags
        existing_tags = get_existing_tags()
        if new_tag in existing_tags:
            print(f"Tag {new_tag} already exists. Aborting.")
            sys.exit(1)

        # Update the VERSION file
        with open(version_file, 'w') as f:
            f.write(new_version)
        print(f"Version bumped to {new_version}")

        # Commit the updated VERSION file and create a new Git tag
        subprocess.run(["git", "add", version_file], check=True)
        subprocess.run(["git", "commit", "-m", f"Bump version to {new_version}"], check=True)
        subprocess.run(["git", "tag", new_tag], check=True)
        subprocess.run(["git", "tag", "-a", new_tag, "-m", f"Release {new_version}"], check=True)


    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
