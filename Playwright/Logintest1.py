import pytest

from playwright.sync_api import Page, expect

def test_pg1(page:Page):
    page.goto("https://www.google.com/")
    expect(page).to_have_url("https://www.google.com/")


def test_pg2(page: Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")


