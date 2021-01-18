import argparse
import sys
from typing import List
from tailtrim.tailtrimmer import TailTrimmer


def main(args: List[str]):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--use_swap', action='store_true', help='Use swap file. Helpful for reducing RAM usage for large files.')
    parser.add_argument('-c', '--use_crlf', action='store_true',
                        help='Use CRLF line endings instead of LF ones.')
    parser.add_argument('-e', '--remove_empty_lines', action='store_true',
                        help='Remove empty lines after trimming.')
    parser.add_argument('filenames', nargs=argparse.REMAINDER)
    parsed_args = parser.parse_args()

    use_crlf = parsed_args.use_crlf
    use_swap = parsed_args.use_swap
    remove_empty_lines = parsed_args.remove_empty_lines
    trimmer = TailTrimmer(use_crlf, use_swap, remove_empty_lines)
    for file_name in parsed_args.filenames:
        try:
            trimmer.trim_file(file_name)
        except Exception as e:
            print(e)
            sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
