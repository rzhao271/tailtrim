class TailTerminator:
    def __init__(self, use_crlf):
        self._use_crlf = use_crlf

    """
    Returns a terminator.
    If using CRLF endings, return "\r\n".
    Otherwise, return "\n".
    """
    def get_terminator(self):
        if self._use_crlf:
            return "\r\n"
        else:
            return "\n"
