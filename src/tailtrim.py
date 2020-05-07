from tailterminator import TailTerminator

class TailTrimmer:
    def __init__(self, use_crlf):
        terminator = TailTerminator(use_crlf)
        self._terminator_str = terminator.get_terminator()

    """
    Trims a file.

    Keyword arguments:
    file_name -- the file name of the file getting trimmed
    swap_file_name -- the file name of the swap file (default None)
        The swap file is a copy of the original file, and
        can be created to speed up the trimming process for large files
    """
    def trim_file(self, file_name, swap_file_name=None):
        if file_name is None:
            return

        terminator = self._terminator_str
        if swap_file_name is not None:
            assert swap_file_name != file_name
            # Assumption: the swap file contains the original contents
            # so we read from it and write back to the original file
            with open(swap_file_name, 'r') as read_file:
                with open(file_name, 'w') as write_file:
                    while True:
                        line = read_file.readline()
                        if len(line) == 0:
                            break # reached EOF
                        trimmed_line = line.rstrip() + terminator
                        write_file.write(trimmed_line)
        else:
            file_lines = []
            with open(file_name, 'r') as f:
                file_lines = f.readlines()
            file_lines = [line.rstrip() + terminator for line in file_lines]
            with open(file_name, 'w') as f:
                f.writelines(file_lines)
