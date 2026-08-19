from playwright.sync_api import Page, expect

class Order_Confirm_Page:
    def __init__(self, page: Page):
        self.page = page
        self.order_confirm_text = page.locator("div.section.order-completed")
        self.order_number = page.locator("ul.details").get_by_text("Order number:")


    def order_confirm_action(self):
        expect(self.order_confirm_text).to_contain_text("Your order has been successfully processed!")
        print("Order Number is", self.order_number.inner_text())

