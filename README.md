# TailTrim

## About

TailTrim is a Python 3 library that trims the end of files
and appends newlines onto the end of them.

The repository also comes with an executable script.

## Command Flags

The command flags that can be used with `tailtrim.sh` are as follows:

```
-d [dirname] to include a directory
-i [pattern] to include a pattern of files
-e [pattern] to exclude a pattern of files
-r for recursively modifying files within the included directories
```

## Limitations

The entire file is read into Python at once.
This script will not work with very large files.
