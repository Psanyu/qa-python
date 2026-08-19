import pytest
from playwright.sync_api import Page, expect, Playwright

@pytest.mark.parametrize(
    "email, password",
    [
        ("admin.test@hmail.com", "Admin@123"),
    ]
)

def test_login(email,password, page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    loginpg_link= page.locator("//a[@class='ico-login']")
    loginpg_link.click()

    #Opening Login page Assertion
    loginpg_heading = page.locator("h1")
    expect(loginpg_heading).to_have_text("Welcome, Please Sign In!")

    #LoginForm Var N Filling
    loginpgvar1_Email= page.locator("#Email")
    loginpgvar1_Email.fill(email)
    loginpgvar2_Pwd = page.locator("#Password")
    loginpgvar2_Pwd.fill(password)

    loginpg_button =page.locator("input[value='Log in']")
    loginpg_button.click()

    #Entering Account Assertion
    Accpg_heading = page.locator("div[class='header-links'] a[class='account']")
    expect(Accpg_heading).to_have_text("admin.test@hmail.com")

    page.wait_for_timeout(2000)

    page.close()

