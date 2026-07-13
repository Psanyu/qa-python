import pytest
import time

from playwright.sync_api import Page, expect

def test_PT2(page: Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    dropdown = page.locator("#dt-length-0")
    dropdown.select_option(label="25")
    rwpt = page.locator("#example tbody tr")
    expect(rwpt).to_have_count(25)

    page.wait_for_timeout(5000)
    page.close()
