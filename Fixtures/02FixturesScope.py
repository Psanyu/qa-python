import pytest

@pytest.fixture (scope="module")
def setup():
   print("setup browser....")
   yield
   print("setup finished")


def test_1(setup):
    print("mytest_1")

def test_2(setup):
    print("mytest_2")
