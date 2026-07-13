import pytest
import time

from playwright.sync_api import Page,expect

def test_St1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    dyTab = page.locator("#taskTable")

    row = dyTab.locator("tbody tr")
    rw_count = row.count()

    for i in range(rw_count):
        cols= row.nth(i).locator("td")
        for j in range(cols.count()):
            cell = cols.nth(j)

            if cell.text_content() == "System":
                print("Row1")
                print(row.nth(i).inner_text())

            if cell.text_content() == "Firefox":
                print("Row2")
                print(row.nth(i).inner_text())

            if cell.text_content() == "Internet Explorer":
                print("Row3")
                print(row.nth(i).inner_text())

            if cell.text_content() == "Chrome":
                print("Row4")
                print(row.nth(i).inner_text())

    displayval = page.locator("#displayValues p", has_text="CPU load")
    t1 = displayval.inner_text()
    print("Display for CPU load:","\n", t1)

    displayval = page.locator("#displayValues p", has_text="Memory Size")
    t2 = displayval.inner_text()
    print("Display for Memory Size:", "\n", t2)

    displayval = page.locator("#displayValues p", has_text="Network speed")
    t3 = displayval.inner_text()
    print("Display for Network speed:", "\n", t3)

    displayval = page.locator("#displayValues p", has_text="Disk space")
    t4 = displayval.inner_text()
    print("Display for Disk space:", "\n", t4)

    page.wait_for_timeout(5000)
    page.close()
