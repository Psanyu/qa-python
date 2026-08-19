from playwright.sync_api import Page


def select_date(page: Page, month: str, year: str, day: str):
    # Month name to number mapping (0-11)
    months = {'Jan': '0', 'Feb': '1', 'Mar': '2', 'Apr': '3', 'May': '4', 'Jun': '5',
              'Jul': '6', 'Aug': '7', 'Sep': '8', 'Oct': '9', 'Nov': '10', 'Dec': '11'}

    # Select month and year dropdowns
    page.locator('.ui-datepicker-month').select_option(months[month])
    page.locator('.ui-datepicker-year').select_option(year)
    page.wait_for_timeout(300)

    # Click the day
    page.locator(f".ui-datepicker-calendar a:has-text('{day}')").click()


def test_datepicker(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#txtDate").click()
    page.wait_for_timeout(500)

    select_date(page, "Oct", "2024", "15")

    print("Selected Date:", page.locator("#txtDate").input_value())
    page.wait_for_timeout(2000)
    page.close()




