# TailTrim

[![Travis (.com) branch](https://img.shields.io/travis/com/rzhao271/tailtrim/main)](https://travis-ci.com/github/rzhao271/tailtrim)

## About

TailTrim is a Python 3 library that trims trailing whitespace for text files.
The repository also comes with an executable bash script.

## Motivation

Well, I realized VS Code already has a `Format Document` command, so there's not as much use for this library now.

Writing up this library introduced me to the following, though:

- bash
    - shunit2
- Python
    - argparse
    - docstrings
    - modules
    - pytest
    - subprocess

so it was worth.

## Usage

```
usage: main.py [-h] [-s] [-c] [-e] ...

positional arguments:
  filenames

optional arguments:
  -h, --help            show this help message and exit
  -s, --use_swap        Use swap file. Helpful for reducing RAM usage for large files.
  -c, --use_crlf        Use CRLF line endings instead of LF ones.
  -e, --remove_empty_lines
                        Remove empty lines after trimming.
```

All optional arguments default to `False`.
