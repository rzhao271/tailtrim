import os
from subprocess import run
from tailtrim.tailterminator import TailTerminator


class TailTrimmer:
    '''
    An object that trims tailing spaces of files.
    use_crlf: use CRLF line endings instead of LF ones.
    use_swap: use swap files to aid in trimming large or long files.
    remove_empty_lines: remove empty lines.
    '''

    def __init__(self, use_crlf: bool, use_swap: bool, remove_empty_lines: bool):
        terminator = TailTerminator(use_crlf)
        self._terminator_str = terminator.get_terminator()
        self._use_swap = use_swap
        self._remove_empty_lines = remove_empty_lines

    def trim_file(self, file_name: str):
        '''
        Trims a file with name file_name.
        '''
        if file_name is None or len(file_name) == 0:
            raise Exception('File name cannot be empty.')
        if not os.path.exists(file_name):
            raise Exception(f'Invalid file name: {file_name}')

        terminator = self._terminator_str
        if self._use_swap:
            swap_file_name = f'{file_name}.swp'
            if os.path.exists(swap_file_name):
                raise Exception(
                    f'A swap file with name {swap_file_name} already exists!')
            res = run(["cp", file_name, swap_file_name])
            res.check_returncode()
            with open(swap_file_name, 'r', 1) as read_file:
                with open(file_name, 'w', newline='') as write_file:
                    for line in read_file:
                        trimmed_line = line.rstrip()
                        if not self._remove_empty_lines or len(trimmed_line):
                            trimmed_line += terminator
                            write_file.write(trimmed_line)
            os.remove(swap_file_name)
        else:
            file_lines = []
            with open(file_name, 'r') as f:
                file_lines = f.readlines()
            file_lines = [line.rstrip(
            ) + terminator for line in file_lines if not self._remove_empty_lines or len(line.rstrip())]
            with open(file_name, 'w', newline='') as f:
                f.writelines(file_lines)
