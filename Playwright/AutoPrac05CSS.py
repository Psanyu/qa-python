import pytest
import time

from playwright.sync_api import Page,expect

def test_A1(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    time.sleep(5)
    #tagid
    SE1= page.locator("input#small-searchterms")
    SE1.fill("Simple Computer")
    time.sleep(5)
    # tagclass
    SE2 = page.locator("input.button-1.search-box-button")
    SE2.click()
    time.sleep(5)
    # tagAttr
    SE3 = page.locator("input[value='Add to cart']")
    SE3.click()
    time.sleep(5)
    # tagClassAttr
    SE4 = page.locator("input.button-1[value='Add to cart']")
    SE4.click()
    time.sleep(5)
    page.close()


