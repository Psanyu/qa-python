import pytest
from playwright.sync_api import Page, expect, Playwright

search_items=['Laptop', 'Gift card', 'smartphone','monitor']

@pytest.mark.parametrize("item", search_items)
def test_search_item(item, page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(item)
    page.locator("input[value='Search']").click()

    #Assertion
    first_result=page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(item,ignore_case=True)

@pytest.mark.parametrize(
    "item2, expected",
    [
        ("Laptop", "Laptop"),
        ("Gift card", "Gift card"),
        ("smartphone", "smartphone"),
        ("monitor", "No products were found that matched your criteria.")
    ]
)
def test_search_item2(item2, expected, page: Page):

    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(item2)
    page.locator("input[value='Search']").click()

    if item2 == "monitor":
        expect(page.get_by_text(expected)).to_be_visible()
    else:
        first_result = page.locator("h2 a").first
        expect(first_result).to_contain_text(expected, ignore_case=True)
