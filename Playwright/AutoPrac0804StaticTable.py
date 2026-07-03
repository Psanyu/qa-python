import pytest
import time

from playwright.sync_api import Page,expect

def test_St1(page: Page):
    page.goto("https://demowebshop.tricentis.com/")



    page.wait_for_timeout(5000)

    page.close()


