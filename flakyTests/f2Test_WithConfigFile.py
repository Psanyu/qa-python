from playwright.sync_api import Page, expect

def test_URL(page: Page):
    page.goto("https://www.demoblaze.com/index.html")
    page.wait_for_timeout(3000)
    store_logo = page.locator("#nava")
    expect(store_logo).to_be_visible()
    page.close()

def test_Title(page: Page):
    page.goto("https://www.demoblaze.com/index.html")
    page.wait_for_timeout(3000)
    expect(page).to_have_title("STORE")
    page.close()

def test_Login(page: Page):
    page.goto("https://www.demoblaze.com/index.html")
    page.wait_for_timeout(2000)

    #Login Form Locator Variables
    login = page.locator("#login2")
    username = page.locator("#loginusername")
    password = page.locator("#loginpassword")
    login_button = page.locator("button:has-text('Log in')")
    username_loc = page.locator("#nameofuser")
    logout = page.locator("#logout2")

    #Login Form Actions
    expect(login).to_be_visible()
    login.click()

    username.fill('pavnol')
    password.fill('test@123')
    login_button.click()

    page.wait_for_timeout(4000)
    expect(username_loc).to_contain_text("Welcome pavnol")

    expect(logout).to_be_visible()
    logout.click()

    page.close()

