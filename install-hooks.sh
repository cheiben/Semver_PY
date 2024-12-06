#!/bin/bash

echo "Installing Git hooks..."
cp -r hooks/* .git/hooks/
chmod +x .git/hooks/*
echo "Git hooks installed successfully."


## Setting Up Git Hooks

#After cloning the repository, run the following command to set up Git hooks:

#```bash
# chmod +x ./install-hooks.sh  ```
