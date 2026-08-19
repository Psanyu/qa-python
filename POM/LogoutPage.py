from playwright.sync_api import Page, expect

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.logout_link = page.locator(".ico-logout")

    def logout_action(self):
        expect(self.logout_link).to_be_visible()
        self.logout_link.click()
