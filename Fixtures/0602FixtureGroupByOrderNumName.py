import pytest


@pytest.mark.order("first")
def test_comp3(setupfile):
    e=5
    f=2
    assert (e > f)==True

@pytest.mark.order("last")
def test_comp4(setupfile):
    e=5
    f=2
    assert (e < f)==False





