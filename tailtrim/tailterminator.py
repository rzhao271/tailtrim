class TailTerminator:
    def __init__(self, use_crlf: bool):
        self._use_crlf = use_crlf

    def get_terminator(self) -> str:
        '''
        Returns a terminator.
        If using CRLF endings, return \\r\\n.
        Otherwise, return \\n.
        '''
        if self._use_crlf:
            return '\r\n'
        else:
            return '\n'
