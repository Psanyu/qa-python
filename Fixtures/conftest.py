import pytest

@pytest.fixture (scope="module")
def setupfile():
   print("setup browser....")
   return("sucess")