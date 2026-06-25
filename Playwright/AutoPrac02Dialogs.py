import pytest
from playwright.sync_api import Page,expect

def test_N4(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    myurl=page.url

#How to use page.on with dialogue box event with lambda
    page.on("dialog",lambda dialog:dialog.accept())
    page.wait_for_timeout(5000)
    page.locator("#alertBtn").click()
    page.wait_for_timeout(3000)
    page.locator("#confirmBtn").click()
    page.wait_for_timeout(5000)
    page.locator("#name").fill("Test1")
    page.wait_for_timeout(5000)
    page.close()

def test_N5(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    myurl=page.url

#How to use page.on with dialogue box event with lambda and altered inner text in dialog box
    page.on("dialog",lambda dialog:dialog.accept("John"))
    page.wait_for_timeout(5000)
    page.locator("#promptBtn").click()
    text = page.locator("#demo").inner_text()
    print(text,"This is output text")

    expect(page.locator("#demo")).to_have_text("Hello John! How are you today?")
    page.wait_for_timeout(5000)


    page.close()

