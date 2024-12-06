#!/usr/bin/env python3
import sys
import re
import subprocess
from typing import List, Literal

class VersionBumper:
    """Manages version bumping for a Git repository."""

    @staticmethod
    def validate_version_format(version: str) -> bool:
        """
        Validate that the version string follows semantic versioning format.
        
        Args:
            version (str): Version string to validate
        
        Returns:
            bool: True if version is valid, False otherwise
        """
        return bool(re.match(r'^\d+\.\d+\.\d+$', version))

    @staticmethod
    def bump_version(version: str, part: Literal['major', 'minor', 'patch']) -> str:
        """
        Increment the specified part of the version.
        
        Args:
            version (str): Current version string
            part (str): Version part to increment ('major', 'minor', or 'patch')
        
        Returns:
            str: New version string
        
        Raises:
            ValueError: If an invalid version part is provided
        """
        major, minor, patch = map(int, version.split('.'))
        
        version_increments = {
            'major': (major + 1, 0, 0),
            'minor': (major, minor + 1, 0),
            'patch': (major, minor, patch + 1)
        }
        
        if part not in version_increments:
            raise ValueError("Invalid version part. Use 'major', 'minor', or 'patch'.")
        
        new_major, new_minor, new_patch = version_increments[part]
        return f"{new_major}.{new_minor}.{new_patch}"

    @staticmethod
    def get_existing_tags() -> List[str]:
        """
        Retrieve existing Git tags in the repository.
        
        Returns:
            List[str]: List of existing tags
        
        Raises:
            subprocess.CalledProcessError: If git command fails
        """
        result = subprocess.run(
            ["git", "tag"], 
            check=True, 
            capture_output=True, 
            text=True
        )
        return result.stdout.splitlines()

    @classmethod
    def bump_and_tag(cls, version_file: str, part: str) -> None:
        """
        Main method to bump version, update file, and create Git tag.
        
        Args:
            version_file (str): Path to the version file
            part (str): Version part to increment
        """
        try:
            # Read current version
            with open(version_file, 'r') as f:
                current_version = f.read().strip()
            
            # Validate version format
            if not cls.validate_version_format(current_version):
                raise ValueError("Invalid version format in VERSION file.")
            
            # Bump version
            new_version = cls.bump_version(current_version, part)
            new_tag = f"v{new_version}"
            
            # Check for existing tags
            existing_tags = cls.get_existing_tags()
            if new_tag in existing_tags:
                print(f"Tag {new_tag} already exists. Aborting.")
                sys.exit(1)
            
            # Update version file
            with open(version_file, 'w') as f:
                f.write(new_version)
            
            # Git operations
            subprocess.run(["git", "add", version_file], check=True)
            subprocess.run(
                ["git", "commit", "-m", f"Bump version to {new_version}"], 
                check=True
            )
            subprocess.run(
                ["git", "tag", "-a", new_tag, "-m", f"Release {new_version}"], 
                check=True
            )
            
            print(f"Version bumped to {new_version}")
        
        except (IOError, subprocess.CalledProcessError, ValueError) as e:
            print(f"Error: {e}")
            sys.exit(1)

def main():
    """
    Script entry point. 
    Validates and processes command-line arguments.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 bump_version.py [major|minor|patch]")
        sys.exit(1)
    
    part = sys.argv[1]
    VersionBumper.bump_and_tag('VERSION', part)

if __name__ == "__main__":
    main()