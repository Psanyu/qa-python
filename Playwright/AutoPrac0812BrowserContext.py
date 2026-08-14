from playwright.sync_api import Playwright, expect
import re


def test_Browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page1 = context.new_page()
    page2 = context.new_page()

    # Page 1
    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(3000)
    # Use regex for flexible matching
    expect(page1).to_have_title(re.compile("Playwright"))

    # Page 2
    page2.goto("https://www.selenium.dev/", wait_until="domcontentloaded")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title(re.compile("Selenium"))

    # Cleanup
    page1.close()
    page2.close()
    browser.close()






