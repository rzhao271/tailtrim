#!/bin/bash

# First, gather all the files
files="$1"
curdir="${BASH_SOURCE%/*}"

# Start processing each file
for file in "$files"
do
    full_file="$(pwd)/${file}"
    filesize=$(du --block=1 "$file" | awk '{print $1;}')
    if [ $filesize -lt 524288 ]
    then
        # If the file is small, directly trim it
        python3 "${curdir}/main.py" "$full_file"
    else
        # The file is large, swap it
        trimtmp_file="${full_file}.trimtmp~"
        cp "$full_file" "$trimtmp_file"
        python3 "${curdir}/main.py" "$full_file" "$trimtmp_file"
        rm "$trimtmp_file"
    fi
done
