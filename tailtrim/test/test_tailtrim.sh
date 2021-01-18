#!/bin/bash

# Note: this file tests tailtrim.sh, not tailtrim_test.py!
# To run tailtrim_test.py, use virtualenv and run pytest 
# from this directory.

testfile='testfile.txt'
confirmfile='confirm.txt'
tailtrim_dir='../..'
test_dir='tailtrim/test'
shunit2_dir='../../shunit2-2.1.8'

setUp() {
    cd "$tailtrim_dir"
    if [ -f "$testfile" ]
        then
        fail "$testfile shouldn't exist before setup"
    fi
    if [ -f "$confirmfile" ]
        then
        fail "$confirmfile shouldn't exist before setup"
    fi
    touch "$testfile"
    touch "$confirmfile"
}

tearDown() {
    if [ -f "$testfile" ]
        then
        rm "$testfile"
    fi
    if [ -f "$confirmfile" ]
        then
        rm "$confirmfile"
    fi
    if [ -d "$test_dir" ]
        then
        cd "$test_dir"
    fi
}

testTailTrimNoSwap() {
    echo -en "this is a test     \nthis is a test  " > "$testfile"
    echo -en "this is a test\nthis is a test\n" > "$confirmfile"

    ./tailtrim.sh "$testfile"
    assertEquals 0 $?

    diff "$testfile" "$confirmfile" > /dev/null 2>&1
    assertEquals 0 $?
}

testTailTrimCrlf() {
    echo -en "this is a test     \nthis is a test  " > "$testfile"
    echo -en "this is a test\r\nthis is a test\r\n" > "$confirmfile"

    ./tailtrim.sh -c "$testfile"
    assertEquals 0 $?

    diff "$testfile" "$confirmfile" > /dev/null 2>&1
    assertEquals 0 $?
}

testTailTrimRemoveEmpty() {
    echo -en "this is a test    \n\n\n\n    \nthis is a test  " > "$testfile"
    echo -en "this is a test\nthis is a test\n" > "$confirmfile"

    ./tailtrim.sh -e "$testfile"
    assertEquals 0 $?

    diff "$testfile" "$confirmfile" > /dev/null 2>&1
    assertEquals 0 $?
}

testTailTrimSwap() {
    for i in {1..20000}
    do
        echo -en "this is a test     \nthis is a test  \n" >> "$testfile"
        echo -en "this is a test\nthis is a test\n" >> "$confirmfile"
    done
    echo -en "this is a test     \n\nthis is a test  " >> "$testfile"
    echo -en "this is a test\n\nthis is a test\n" >> "$confirmfile"

    ./tailtrim.sh -s "$testfile"
    assertEquals 0 $?

    diff "$testfile" "$confirmfile" > /dev/null 2>&1
    assertEquals 0 $?
}

testTailTrimSwapRemoveEmpty() {
    for i in {1..20000}
    do
        echo -en "this is a test     \n\n\n\nthis is a test  \n" >> "$testfile"
        echo -en "this is a test\nthis is a test\n" >> "$confirmfile"
    done
    echo -en "this is a test     \n\n\nthis is a test  " >> "$testfile"
    echo -en "this is a test\nthis is a test\n" >> "$confirmfile"

    ./tailtrim.sh -s -e "$testfile"
    assertEquals 0 $?

    diff "$testfile" "$confirmfile" > /dev/null 2>&1
    assertEquals 0 $?
}

. "$shunit2_dir/shunit2"
