from playwright.sync_api import Playwright, expect

def test_Screenshots(playwright: Playwright):
    # Setup browser and page
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Starting the trace
    context.tracing.start(screenshots=True, snapshots=True)

    #Page
    page = context.new_page()

    # Navigate
    page.goto("https://www.demoblaze.com/index.html")

    page.locator("#login2").click()
    page.locator("#loginusername").fill('pavnol')
    page.locator("#loginpassword").fill('test@123')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome pavnol")

    #Stop Tracing
    context.tracing.stop(path="trace.zip")

    # Cleanup
    context.close()
    browser.close()









