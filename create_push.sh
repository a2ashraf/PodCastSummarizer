#!/bin/bash

# Prompt user for GitHub repository name and description
read -p "Enter the name of the repository: " REPO_NAME
read -p "Enter a description for the repository: " REPO_DESC

# Initialize a Git repository if it doesn't already exist
if [ ! -d .git ]; then
    echo "Initializing a new git repository..."
    git init
else
    echo "Git repository already initialized."
fi

# Add files to the Git repository
echo "Adding files to the repository..."
git add .

# Commit the changes with the default message
echo "Creating an initial commit..."
git commit -m "Initial commit"

# Create the GitHub repository using GitHub CLI
echo "Creating a public repository on GitHub..."
gh repo create "$REPO_NAME" --public -d "$REPO_DESC"

# Add GitHub as the remote origin using SSH
echo "Adding GitHub remote via SSH..."
git remote add origin "git@github.com:a2ashraf/$REPO_NAME.git"

# Push the changes to the GitHub repository
echo "Pushing changes to GitHub..."
git branch -M main
git push -u origin main

echo "Repository successfully created and code pushed to GitHub!"
