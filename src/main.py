import sys
import platform
from tailtrim import TailTrimmer

def main(args):
    # valid args:
    # - program_name, file_name
    # - program_name, file_name, swap_file_name
    argc = len(args)
    if argc != 2 and argc != 3:
        print("Invalid number of arguments given.", file=sys.stderr)
        print("Usage: [file_name] ([swap_file_name])", file=sys.stderr)
        sys.exit(1)

    use_crlf = platform.system() == 'Windows'
    trimmer = TailTrimmer(use_crlf)
    file_name = args[1]
    swap_file_name = args[2] if argc == 3 else None

    if argc == 2:
        trimmer.trim_file(file_name)
    else:
        trimmer.trim_file(file_name, swap_file_name)

    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)
