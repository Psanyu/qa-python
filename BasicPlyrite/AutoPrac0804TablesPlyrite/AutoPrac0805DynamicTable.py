import pytest
import time

from playwright.sync_api import Page,expect

import pytest
import time

from playwright.sync_api import Page, expect

def test_St1(page: Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    Table = page.locator("table.table tbody")
    expect(Table).to_be_visible()

    rw = Table.locator('tr').all()
    cpu_ld = None
    for r in rw:
        processnm = r.locator("td").nth(0).inner_text().strip()
        if processnm == "Chrome":
            cpu_ld = r.locator("td:has-text('%')").first.inner_text()
            print(cpu_ld)
            break

    expect(page.locator('#chrome-cpu')).to_contain_text(cpu_ld)

    page.wait_for_timeout(5000)
    page.close()

