import pytest
from tailtrim.tailterminator import TailTerminator


def test_using_crlf():
    term = TailTerminator(True)
    assert term.get_terminator() == '\r\n'


def test_not_using_crlf():
    term = TailTerminator(False)
    assert term.get_terminator() == '\n'
