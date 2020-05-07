import os
import sys
sys.path.append("../src/")

import pytest
from tailtrim import TailTrimmer

filename = "single.txt"
filename_tmp = f"{filename}.swp"

@pytest.fixture(scope="function")
def init_single_file():
    with open(filename, "w") as f:
        f.write("Test  \n")
        f.write("Test\n")
        f.write("\n")
        f.write(" \n")
        f.write(" abac ")
    yield
    #teardown
    os.remove(filename)

@pytest.fixture(scope="function")
def init_double_file():
    with open(filename, "w") as f:
        f.write("Test  \n")
        f.write("Test\n")
        f.write("\n")
        f.write(" \n")
        f.write(" abac ")
    os.system(f"cp {filename} {filename_tmp}")
    yield
    #teardown
    os.remove(filename)
    os.remove(filename_tmp)

def test_tailtrim_null_file():
    trimmer = TailTrimmer(True)
    trimmer.trim_file(None)
    trimmer.trim_file(None, None)
    trimmer = TailTrimmer(False)
    trimmer.trim_file(None)
    trimmer.trim_file(None, None)

def test_tailtrim_single_file_lf(init_single_file):
    trimmer = TailTrimmer(False)
    trimmer.trim_file(filename)
    filetext = None
    with open(filename, "rb") as f:
        filetext = f.read().decode('ascii')
    assert filetext == "Test\nTest\n\n\n abac\n"

def test_tailtrim_single_file_crlf(init_single_file):
    trimmer = TailTrimmer(True)
    trimmer.trim_file(filename)
    filetext = None
    with open(filename, "rb") as f:
        filetext = f.read().decode('ascii')
    assert filetext == "Test\r\nTest\r\n\r\n\r\n abac\r\n"

def test_tailtrim_double_file_samename(init_double_file):
    try:
        trimmer = TailTrimmer(False)
        trimmer.trim_file(filename, filename)
        assert False
    except:
        assert True

def test_tailtrim_double_file_lf(init_double_file):
    trimmer = TailTrimmer(False)
    trimmer.trim_file(filename, filename_tmp)
    filetext = None
    with open(filename, "rb") as f:
        filetext = f.read().decode('ascii')
    assert filetext == "Test\nTest\n\n\n abac\n"

def test_tailtrim_double_file_crlf(init_double_file):
    trimmer = TailTrimmer(True)
    trimmer.trim_file(filename, filename_tmp)
    filetext = None
    with open(filename, "rb") as f:
        filetext = f.read().decode('ascii')
    assert filetext == "Test\r\nTest\r\n\r\n\r\n abac\r\n"
