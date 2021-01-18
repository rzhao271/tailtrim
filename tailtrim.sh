#!/bin/sh

# Pass the args directly to Python
which python3 > /dev/null 2>&1
if [ $? = 0 ]
    then
    python3 "main.py" "$@"
else
    python "main.py" "$@"
fi
