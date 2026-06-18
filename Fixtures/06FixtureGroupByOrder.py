import pytest
from numpy.ma.core import less_equal
from pycparser.c_ast import If


@pytest.mark.order(1)
def test_mod(setupfile):
    a=5
    b=2
    assert a%b == 1

@pytest.mark.order(3)
def test_comp(setupfile):
    a=5
    b=2
    assert (a > b)==True

@pytest.mark.order(2)
def test_comp2(setupfile):
    a=5
    b=2
    assert (a < b)==False

@pytest.mark.order(first)
def test_comp3(setupfile):
    e=5
    f=2
    assert (e > f)==True

@pytest.mark.order(last)
def test_comp4(setupfile):
    e=5
    f=2
    assert (e < f)==False





