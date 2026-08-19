from playwright.sync_api import Playwright
import datetime
from pathlib import Path


def test_Browser(playwright: Playwright):
    # Setup browser and page
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate
    page.goto("https://www.demoblaze.com/index.html")

    # Timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Screenshot: Partial (visible area only)
    page.screenshot(path=f"screenshots/homepage_{timestamp}.png")

    # Screenshot: Full (entire page)
    page.screenshot(path=f"screenshots/homepage_full_{timestamp}.png", full_page=True)

    #Screenshot: Feature (Samsung Phone)
    samsungPhone_Feature= page.locator("//a[normalize-space()='Samsung galaxy s6']")
    samsungPhone_Feature.wait_for()
    samsungPhone_Feature.scroll_into_view_if_needed()
    samsungPhone_Feature.screenshot(path=f"screenshots/samsung_phone_{timestamp}.png")

    #Screenshot: Feature (NavaLogo)
    navalogo_Element= page.locator("//a[@id='nava']//img")
    navalogo_Element.wait_for()
    navalogo_Element.scroll_into_view_if_needed()
    navalogo_Element.screenshot(path=f"screenshots/navalogo_{timestamp}.png")

    # Cleanup
    page.close()
    context.close()
    browser.close()









