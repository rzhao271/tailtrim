# TailTrim

[![Travis (.com) branch](https://img.shields.io/travis/com/rzhao271/tailtrim/master)](https://travis-ci.com/github/rzhao271/tailtrim)

## About

TailTrim is a Python 3 library for text files.

Given a text file, it trims trailing whitespace for each line (including the newline separator),
and reappends newlines onto the end of them. It does not remove blank lines.

The newlines appended (CRLF or LF) depend on the parameter passed into `TailTrimmer`.

The repository also comes with an executable bash script.
