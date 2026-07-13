import pytest
import time

from playwright.sync_api import Page, expect

def test_PT1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    Tablep = page.locator("#productTable")
    expect(Tablep).to_be_visible()

    current_page = 0
    page_links = page.locator("#pagination a")
    total_pages = page_links.count()

    while current_page < total_pages:
        page.locator("#pagination a").nth(current_page).click()

        rows = page.locator("#productTable tbody tr")
        for i in range(rows.count()):
            print("\n", AutoPrac0807Assignment3Table.pyrows.nth(i).inner_text())

        current_page += 1

    page.wait_for_timeout(5000)
    page.close()



