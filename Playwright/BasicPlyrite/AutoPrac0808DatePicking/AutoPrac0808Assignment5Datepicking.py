from playwright.sync_api import Page, expect

def select_date(page, target_year, target_month, target_day, is_future):

    page.locator("#datepicker").click()

    while True:
        current_month = page.locator(".ui-datepicker-month").text_content()

        current_year = page.locator(".ui-datepicker-year").text_content()

        if current_month == target_month and current_year == target_year:
            break

        if is_future == False:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()


    alldates = page.locator(".ui-datepicker-calendar td").all()

    for dt in alldates:
        date = dt.text_content()
        if date == target_day:
            dt.click()
            break



def test_DP1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

#Approach1
    dateInput= page.locator("#datepicker")
    dateInput.fill("2020-07-30")
    expect(dateInput).to_have_value("2020-07-30")

    page.wait_for_timeout(5000)
    page.close()

def test_DP2(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

 # Approach2
    dateInput = page.locator("#datepicker")
    is_future = True
    target_year = "2020"
    target_month = "July"
    target_day = "30"

    select_date(page, target_year, target_month, target_day, is_future)

    print("\n", "Selected Date :", dateInput.input_value())

    page.wait_for_timeout(5000)
    page.close()

def test_DP3(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

 # Approach3
    dateIP3 = page.locator("#txtDate")
    #is_future = True
    target_year = "2026"
    target_month = "Jul"
    target_month2 = "07"
    target_day = "15"

    dateIP3.click()

    #select year
    page.locator(".ui-datepicker-year").select_option(label=target_year)


    #select month
    page.locator(".ui-datepicker-month").select_option(label=target_month)

    #select day
    dTable = page.locator(".ui-datepicker-calendar")
    days = dTable.locator("td:not(.ui-datepicker-other-month) a")
    days_count= days.count()

    for index in range(days_count):
        day = days.nth(index)
        if day.inner_text() == target_day:
            day.click()
            break

    selected_date = dateIP3.input_value()
    print("\nSelected Date:", selected_date)

    expect(dateIP3).to_have_value(f"{target_day}/{target_month2}/{target_year}")

    page.wait_for_timeout(5000)
    page.close()




