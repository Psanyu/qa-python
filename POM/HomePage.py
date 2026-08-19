from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.product_list_loc = page.locator("h2.product-title")
        self.add_to_cart_loc = page.locator("input.button-1.add-to-cart-button")
        self.shop_cart_link = page.locator("span.cart-label").filter(has_text="Shopping cart")
        self.accept_terms_loc = page.locator("input#termsofservice")
        self.checkout_loc = page.locator("button#checkout")

    def select_product_action(self, item_name):
        product_name= self.product_list_loc.get_by_role("link", name= item_name, exact=True)
        expect(product_name).to_be_visible()
        product_name.click()
        # Product details page must be loaded
        product_heading = self.page.get_by_role("heading", name=item_name, exact=True)
        expect(product_heading).to_be_visible()

    def add_to_cart_action(self):
        expect(self.add_to_cart_loc).to_be_visible()
        self.add_to_cart_loc.click()
        expect(self.page.locator(".cart-qty")).to_contain_text("(1)")

    def shop_cart_action(self):
        self.shop_cart_link.click()

    def accept_terms_action(self):
        self.accept_terms_loc.click()

    def checkout_action(self):
        self.checkout_loc.click()



