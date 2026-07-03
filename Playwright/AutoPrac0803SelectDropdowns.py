import pytest
import time

from playwright.sync_api import Page,expect

def test_S1Verifi(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    prodOpt = page.locator(".product-title")
    print("inner Text:", prodOpt.nth(1).inner_text())
    print("Text Content:",prodOpt.nth(1).text_content())

    prodOptAll = page.locator(".product-title")
    print("inner Text:", prodOptAll.all_inner_texts())
    print("Text Content:",prodOptAll.all_text_contents())

    prodLocAll = prodOpt.all()
    for i, loc in enumerate(prodLocAll):
        print("inner Text:", i, loc.inner_text())

    page.wait_for_timeout(5000)

    page.close()


