import pytest
import sys

from conftest import *

@pytest.mark.skip
def test_1S(setupfile):
    print("mytest_1")

def test_2S(setupfile):
    print("mytest_2")

@pytest.mark.skipif(sys.platform == "win64", reason="does not run on win64")
def test_something():
    print("this test is skipped on Windows")