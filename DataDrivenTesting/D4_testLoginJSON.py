import pytest
from playwright.sync_api import Page, expect, Playwright
import json

#Read json file
file = open("Plyrite/DataDrivenTesting/testdata/login.json","r")
login_data = json.load(file)

@pytest.mark.parametrize("email, password, validity",[(data["email"],data["password"],data["validity"]) for data in login_data])

def test_login(email,password, validity, page: Page):
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

    #validation
    if validity == "valid":
        # Entering Account Assertion
        Accpg_heading = page.locator("div[class='header-links'] a[class='account']")
        expect(Accpg_heading).to_have_text("admin.test@hmail.com")
        #Logout
        logout_Link= page.locator(".ico-logout")
        expect(logout_Link).to_be_visible(timeout=2000)
        logout_Link.click()
    else:
        err_Link= page.locator(".validation-summary-errors")
        expect(err_Link).to_be_visible(timeout=2000)

    page.wait_for_timeout(2000)

    page.close()

