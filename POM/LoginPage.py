from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Login Form Locator Variables
        self.login_link = page.locator("a.ico-login")
        self.username_link = page.locator("#Email")
        self.password_link = page.locator("#Password")
        self.login_buttonlink = page.locator("input[value='Log in']")
        #self.username_loclink = page.locator("a.account").nth(0)


    def login_action(self, username, password):
        # Login Form Actions
        expect(self.login_link).to_be_visible()
        self.login_link.click()

        self.username_link.fill(username)
        self.password_link.fill(password)
        self.login_buttonlink.click()

        #Assertion for Login
        #expect(self.username_loclink).to_contain_text(username)
