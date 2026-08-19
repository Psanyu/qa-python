import pytest
from playwright.sync_api import Page, expect

def test_pg1(page:Page):
    page.goto("http://localhost/opencart/index.php?route=account/login&language=en-gb")
    myurl = page.url
    print(page.title())
    expect(page).to_have_url("http://localhost/opencart/index.php?route=account/login&language=en-gb")


def test_pg2(page: Page):
    page.goto("http://localhost/opencart/index.php?route=account/login&language=en-gb")
    myurl = page.url
    expect(page).to_have_title("Account Login")


