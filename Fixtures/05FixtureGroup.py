import pytest
import sys


from conftest import *


@pytest.mark.smoketest1
@pytest.mark.groupadd
def test_add(setupfile):
    a=5
    b=2
    assert (a+b)

@pytest.mark.smoketest1
@pytest.mark.groupsub
def test_sub(setupfile):
    a=5
    b=2
    assert (a-b)

@pytest.mark.smoketest1
@pytest.mark.groupmul
def test_mul(setupfile):
    a=5
    b=2
    assert (a*b)

@pytest.mark.smoketest1
@pytest.mark.groupdiv
def test_div(setupfile):
    a=5
    b=2
    assert (a/b)

@pytest.mark.sanity
@pytest.mark.groupadd
def test_add2(setupfile):
    c=5
    d=2
    assert (c+d)

@pytest.mark.sanity
@pytest.mark.groupsub
def test_sub2(setupfile):
    pass

@pytest.mark.sanity
@pytest.mark.groupmul
def test_mul2(setupfile):
    pass

@pytest.mark.sanity
@pytest.mark.groupdiv
def test_div2(setupfile):
    pass

@pytest.mark.skipif(sys.platform == "win64", reason="does not run on win64")
def test_something():
    print("this test is skipped on Windows")