import pytest
import time

from playwright.sync_api import Page,expect

#get_by_alt_text

def test_L1(page:Page):
    page.goto("http://localhost/opencart/")
    time.sleep(5)
    logo = page.get_by_alt_text("Your Store")
    #print(logo.inner_text())
    expect(logo).to_be_visible(timeout=3000)
    # get_by_text
    listname=page.get_by_text("Featured")
    expect(listname).to_be_visible(timeout=3000)
    page.close()


def test_L2(page:Page):
    page.goto("http://localhost/opencart/")
    time.sleep(5)
    # page.locator
    E1=page.locator(".fa-solid.fa-phone")
    E1.click()
    # get_by_label
    time.sleep(5)
    F1=page.get_by_label("Your name")
    F1.fill("Test1")
    time.sleep(5)
    F2=page.get_by_label("E-Mail Address")
    F2.fill("test1@mail.com")
    time.sleep(5)
    F3=page.get_by_label("Enquiry")
    F3.fill("None ....... This is a Test")
    time.sleep(5)
    # get_by_role
    E2=page.get_by_role("button",name="Submit")
    E2.click()
    time.sleep(5)
    page.close()

def test_L3(page:Page):
    page.goto("http://localhost/opencart/")
    time.sleep(5)
    # page.get_by_placeholder
    S1=page.get_by_placeholder("Search")
    S1.fill("macbook")
    S2 = page.locator("button.btn-light.btn-lg")
    S2.click()
    time.sleep(5)
    # page.get_by_title
    S3=page.get_by_title("Your Store")
    print(S3.inner_text())
    time.sleep(5)
    # page.get_by_testid
    S4=page.get_by_test_id("button-search")
    S4.click()
    time.sleep(5)
    page.close()


