import pytest
import time

from playwright.sync_api import Page,expect



def test_L4(page:Page):
    page.goto("http://localhost/opencart/")
    # get_by_title
    time.sleep(5)

    time.sleep(5)
    page.close()


