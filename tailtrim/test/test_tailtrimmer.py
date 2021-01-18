import os
import pytest
from tailtrim.tailtrimmer import TailTrimmer

_filename = 'single.txt'


@pytest.fixture(scope='function')
def init_single_file():
    with open(_filename, 'w') as f:
        f.write('Test  \n')
        f.write('Test\n')
        f.write('\n')
        f.write(' \n')
        f.write(' abac ')
    yield
    # teardown
    os.remove(_filename)


@pytest.fixture(scope='function')
def init_file_with_swap():
    with open(_filename, 'w') as f:
        f.write('Test  \n')
        f.write('Test\n')
        f.write('\n')
        f.write(' \n')
        f.write(' abac ')
    os.system(f'cp {_filename} {_filename}.swp')
    yield
    # teardown
    os.remove(_filename)
    os.remove(f'{_filename}.swp')


def test_tailtrim_null_file():
    trimmer = TailTrimmer(True, True, False)
    try:
        trimmer.trim_file(None)
        assert False
    except AssertionError:
        raise
    except:
        pass


def test_tailtrim_single_file_lf(init_single_file):
    trimmer = TailTrimmer(False, False, False)
    trimmer.trim_file(_filename)
    with open(_filename, 'rb') as f:
        filetext = f.read().decode('ascii')
    assert filetext == 'Test\nTest\n\n\n abac\n'


def test_tailtrim_single_file_crlf(init_single_file):
    trimmer = TailTrimmer(True, False, False)
    trimmer.trim_file(_filename)
    with open(_filename, 'rb') as f:
        filetext = f.read().decode('ascii')
    assert filetext == 'Test\r\nTest\r\n\r\n\r\n abac\r\n'


def test_tailtrim_single_file_empty(init_single_file):
    trimmer = TailTrimmer(False, False, True)
    trimmer.trim_file(_filename)
    with open(_filename, 'rb') as f:
        filetext = f.read().decode('ascii')
    assert filetext == 'Test\nTest\n abac\n'


def test_tailtrim_double_file_samename(init_file_with_swap):
    try:
        trimmer = TailTrimmer(False, True, False)
        trimmer.trim_file(_filename)
        assert False
    except AssertionError:
        raise
    except:
        pass

def test_tailtrim_double_file_lf(init_single_file):
    trimmer = TailTrimmer(False, True, False)
    trimmer.trim_file(_filename)
    with open(_filename, 'rb') as f:
        filetext = f.read().decode('ascii')
    assert filetext == 'Test\nTest\n\n\n abac\n'


def test_tailtrim_double_file_crlf(init_single_file):
    trimmer = TailTrimmer(True, True, False)
    trimmer.trim_file(_filename)
    with open(_filename, 'rb') as f:
        filetext = f.read().decode('ascii')
    assert filetext == 'Test\r\nTest\r\n\r\n\r\n abac\r\n'


def test_tailtrim_double_file_empty(init_single_file):
    trimmer = TailTrimmer(False, True, True)
    trimmer.trim_file(_filename)
    with open(_filename, 'rb') as f:
        filetext = f.read().decode('ascii')
    assert filetext == 'Test\nTest\n abac\n'
