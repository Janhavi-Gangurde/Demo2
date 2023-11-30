#!/bin/bash

# Prompt the user for a file path
read -p "Enter the path to the file: " filepath

# Check if the file exists
if [ -e "$filepath" ]; then
    echo "File exists: $filepath"
    
    # Determine the file type
    if [ -f "$filepath" ]; then
        filetype="Regular file"
    elif [ -d "$filepath" ]; then
        filetype="Directory"
    elif [ -L "$filepath" ]; then
        filetype="Symbolic link"
    else
        filetype="Unknown"
    fi
    echo "File type: $filetype"
    
    # Check file permissions
    permissions=$(ls -l "$filepath")
    echo "File permissions: $permissions"
else
    echo "File does not exist: $filepath"
fi

