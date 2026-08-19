import pytest
import time

from playwright.sync_api import Page, expect

def test_PT1(page: Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    Tablep = page.locator("#example")
    expect(Tablep).to_be_visible()

    has_more_pages = True
    while has_more_pages:

        rwp=Tablep.locator("tbody tr").all()
        for rwpc in rwp:
            print(rwpc.inner_text())

        next_button = page.locator("//button[@aria-label='Next']")
        is_disabled = next_button.get_attribute("class")
        if "disabled" in is_disabled:
            has_more_pages = False
        else:
            next_button.click()

    page.wait_for_timeout(5000)
    page.close()



