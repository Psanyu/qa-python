import pytest

@pytest.fixture
def setup(scope="class"):
   print("setup browser....")
   yield
   print("  teardown browser....")

def test_1(setup):
    print("mytest_1")

def test_2(setup):
    print("mytest_2")
