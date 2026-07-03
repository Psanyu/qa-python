import pytest
import time

from playwright.sync_api import Page,expect

def test_S1Verifi(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    usernm= page.locator("//input[@name='username']")
    usernm.fill("Admin")
    pwd= page.locator("//input[@name='password']")
    pwd.fill("admin123")
    loginbtn = page.locator("//button[@type='submit']")
    loginbtn.click()
    page.wait_for_timeout(5000)
    PIM = page.get_by_role("link", name="PIM")
    PIM.click()
    page.locator("form i").nth(2).click()
    options=page.locator("//div[@role='listbox']//span")
    count1=options.count()
    print(count1)
    expect(options).to_have_count(28)
    print("All Options:"+str(options.all_text_contents()))

    for iN in range(count1):
        OptText=options.nth(iN).text_content()
        if str(OptText) == "Automaton Tester":
            options.nth(iN).click()
            break


    page.wait_for_timeout(5000)

    page.close()


