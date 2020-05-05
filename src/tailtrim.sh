#!/bin/bash

# First, gather all the files
files="$1"

# Start processing each file
for file in "$files"
do
    filesize=(du --block=1 "$file" | awk '{print $1;}')
    if [ $filesize -lt $((1048576*16)) ]
    then
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