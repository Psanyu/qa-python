import pytest

from conftest import *
@pytest.fixture (scope="module")

def test_1S(setupfile):
    print("mytest_1")

def test_2S(setupfile):
    print("mytest_2")