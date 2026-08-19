import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page          # ← tests run here
        browser.close()     # ← teardown after all tests

def test_google(page):
    page.goto("https://google.com")
    assert "Google" in page.title()

def test_title(page):
    page.goto("https://example.com")
    assert "Example" in page.title()