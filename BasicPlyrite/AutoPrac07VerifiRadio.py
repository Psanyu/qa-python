import pytest
import time

from playwright.sync_api import Page,expect

def test_V1Verifi(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # textbox Verification
    text1 = page.locator("//input[@placeholder='Enter Name']")
    expect(text1).to_be_visible()
    text1.fill("ABX")
    # to_have_text is for already present text labels on page
    #to_have_value is for value of a textbox
    expect(text1).to_have_value("ABX")

    #radiobutton
    gbb = page.locator("//input[@value='female']")
    expect(gbb).to_be_visible()
    expect(gbb).to_be_enabled()
    gbb.check()
    page.wait_for_timeout(5000)



    # checkbox button
    cbutton = page.locator("//input[@type='checkbox' and (@value='sunday' or @value='tuesday' or @value='thursday')]")

    for i in range(cbutton.count()):
        page.wait_for_timeout(3000)
        cb = cbutton.nth(i)
        if (cb.is_checked()==False):
           cb.click()
           expect(cb).to_be_checked()

    # checkbox button2
    odddays = ['Monday','Wednesday','Friday']

    for day in odddays:
        chkbx = page.get_by_label(day)
        page.wait_for_timeout(3000)
        if (chkbx.is_checked()==False):
           chkbx.check()
           expect(chkbx).to_be_checked()

    # checkbox button3 unselect
    evendays = ['Sunday','Tuesday', 'Thursday']

    for day2 in evendays:
       chkbx2 = page.get_by_label(day2)
       page.wait_for_timeout(3000)
       if (chkbx2.is_checked()==True):
          chkbx2.uncheck()
          expect(chkbx2).not_to_be_checked()


    page.close()


