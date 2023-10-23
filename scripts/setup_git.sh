#!/bin/bash

# Parse the conf.ini file
username=$(awk -F '=' '/^\[git\]/{f=1} f==1 && /^username/{print $2; exit}' config/conf.ini | tr -d '[:space:]')
repo_name=$(awk -F '=' '/^\[git\]/{f=1} f==1 && /^repo_name/{print $2; exit}' config/conf.ini | tr -d '[:space:]')

# Check if git has already been initialized
if [ -d ".git" ]; then
    echo "Git has already been initialized in this directory."
else
    # Use the extracted values
    echo "# $repo_name" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin "https://github.com/$username/$repo_name.git"
    git push -u origin main
fi
