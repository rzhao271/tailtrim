#!/bin/bash

# First, gather all the files
# Expand all directories
files=""

# Start processing each file
for file in "$files"
do
    if []; then
        # If the file is small, directly trim it
        python3 tailtrim.py "$file"
    else
        # The file is large, swap it
        trimtmp_file="${file}.trimtmp~"
        cp "$file" "$trimtmp_file"
        python3 tailtrim.py "$file" "$trimtmp_file"
        rm "$trimtmp_file"
    fi
done