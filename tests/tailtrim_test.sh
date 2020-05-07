#!/bin/bash

# Note: this file tests tailtrim.sh, not tailtrim_test.py!
# To run tailtrim_test.py, use virtualenv and run pytest

# This script assumes LF endings are used
# The tests may fail on Windows systems

testfile='testfile.txt'
confirmfile='confirm.txt'
tailtrim_dir='../src'

testTailTrimNoSwap() {
    echo -en "this is a test     \nthis is a test  " > "$testfile"
    echo -en "this is a test\nthis is a test\n" > "$confirmfile"

    . "${tailtrim_dir}/tailtrim.sh" "${testfile}"

    diff "$testfile" "$confirmfile" > /dev/null 2>&1
    assertEquals 0 $?

    rm "$testfile"
    rm "$confirmfile"
}

testTailTrimSwap() {
    echo -n "" > "$testfile"
    echo -n "" > "$confirmfile"
    for i in {1..20000}
    do
        echo -en "this is a test     \nthis is a test  \n" >> "$testfile"
        echo -en "this is a test\nthis is a test\n" >> "$confirmfile"
    done
    echo -en "this is a test     \nthis is a test  " >> "$testfile"
    echo -en "this is a test\nthis is a test\n" >> "$confirmfile"

    . "${tailtrim_dir}/tailtrim.sh" "${testfile}"

    diff "$testfile" "$confirmfile" > /dev/null 2>&1
    assertEquals 0 $?

    rm "$testfile"
    rm "$confirmfile"
}

. ../shunit2-2.1.8/shunit2
