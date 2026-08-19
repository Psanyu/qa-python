from playwright.sync_api import Page, expect


def test_DP4(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    start_date = page.locator("#start-date")
    end_date = page.locator("#end-date")
    submit_button = page.locator(".date-picker-box .submit-btn")

    target_start_date = "2026-07-15"
    target_end_date = "2026-07-20"

    # Native HTML date inputs require yyyy-mm-dd format
    start_date.fill(target_start_date)
    end_date.fill(target_end_date)

    expect(start_date).to_have_value(target_start_date)
    expect(end_date).to_have_value(target_end_date)

    print("\nSelected Start Date:", start_date.input_value())
    print("Selected End Date:", end_date.input_value())

    submit_button.click()

    result = page.locator("#result")
    expect(result).not_to_be_empty()

    print("Result:", result.inner_text())

    page.wait_for_timeout(5000)
    page.close()




