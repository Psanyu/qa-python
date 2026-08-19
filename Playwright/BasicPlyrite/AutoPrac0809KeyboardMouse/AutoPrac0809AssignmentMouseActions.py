from playwright.sync_api import Page, expect

def test_mouse2_draganddrop(page: Page):
    page.goto("https://demo.guru99.com/test/drag_drop.html")

    bank_source = page.locator("#credit2")
    bank_target = page.locator("#bank")
    bank_source.drag_to(bank_target)

    bankamt_source = page.locator("#fourth").nth(1)
    bankamt_target = page.locator("#amt7")
    bankamt_source.drag_to(bankamt_target)

    sales_source = page.locator("#credit1")
    sales_target = page.locator("#loan")
    sales_source.drag_to(sales_target)

    salesamt_source = page.locator("#fourth").nth(1)
    salesamt_target = page.locator("#amt8")
    salesamt_source.drag_to(salesamt_target)

    page.wait_for_timeout(2000)
    page.close()


