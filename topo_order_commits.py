#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Inside a directory, when the script topo_order_commits.py (which doesnt have to reside in the same directory) is invoked, the script should first determine where the top level Git directory is. The top level Git directory is the one containing the .git directory. One can do this by looking for .git in the current directory, and if it doesnt exist search the parent directory, etc. This discovery process should only go up, and never descend into a child directory. Output a diagnostic Not inside a Git repository to standard error and exit with status 1 if .git cannot be found when the search went all the way to the / directory.
"""

import sys
import os

class CommitNode:
    def __init__(self, commit_hash):
        """
        :type commit_hash: str
        """
        self.commit_hash = commit_hash
        self.parents = set()
        self.children = set()

def find_git_repository():
    target_directory = ".git"
    current_directory = os.getcwd()

    while True:
        git_directory = os.path.join(current_directory, target_directory)

        if os.path.exists(git_directory):
            return git_directory

        # Move up to the parent directory
        parent_directory = os.path.dirname(current_directory)

        # Check if we have reached the root directory
        if parent_directory == current_directory:
            print("Not inside a Git repository", file=sys.stderr)
            sys.exit(1)

        current_directory = parent_directory

# Example usage


def main():
    found_git_repository = find_git_repository()
    print(f"Found Git repository at: {found_git_repository}") 
    # Your script logic goes here

if __name__ == "__main__":
    sys.exit(main())
