import pytest
import time

from numpy.ma.core import less_equal
from playwright.sync_api import Page,expect

def test_X1(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    #SE1 = page.locator("/html/body/div[4]/div[1]/div[1]/div[3]/form/input[1]")
    XP1=page.locator("input[name='q']")
    expect(XP1).to_be_visible()
    XP1.fill("Computer")

    XP2 = page.locator("//input[@type='submit'][@value='Search']")
    expect(XP2).to_be_visible()
    XP2.click()

    # Assert search results loaded
    expect(page.locator(".search-results")).to_be_visible()

    XP3=page.locator("//h2//a[contains(@href,'computer')]")
    products_count=XP3.count()
    print(products_count)
    print("first",XP3.first.text_content())
    print("last", XP3.last.text_content())
    productTitles=XP3.all_text_contents()
    for i in productTitles:
      print(i)

    XP4=page.locator("//h2//a[starts-with(@href,'/build')]")
    products_count2=XP4.count()
    print(products_count2)
    print("first",XP4.first.text_content())
    print("last", XP4.last.text_content())
    productTitles2=XP4.all_text_contents()
    for j in productTitles2:
      print(j)

    XP5 = page.locator("//a[contains(@href,'+nopcommerce')]")
    expect(XP5).to_have_text("Google+")
    XP5.click()

    print(XP5.inner_text())

    time.sleep(5)

    page.close()

def test_X2DynamicButton(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    buttonDy = page.locator("//button[@name='start' or @name='stop']")
    for i in range(5):
      if(buttonDy.inner_text()=="START"):
          buttonDy.click()
          expect(buttonDy).to_have_text("STOP")
          time.sleep(5)
      else:
          buttonDy.click()
          expect(buttonDy).to_have_text("START")
          time.sleep(5)

    page.close()


