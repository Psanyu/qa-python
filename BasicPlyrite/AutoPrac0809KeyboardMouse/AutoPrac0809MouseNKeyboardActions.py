from numpy.ma.core import filled
from playwright.sync_api import Page, expect

def test_mousehover(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    pointme = page.locator("button.dropbtn")
    pointme.scroll_into_view_if_needed()

    page.wait_for_timeout(5000)

    pointme.hover()

    laptop = page.locator('.dropdown-content a').nth(0)
    laptop.scroll_into_view_if_needed()

    page.wait_for_timeout(5000)
    laptop.click()

    page.wait_for_timeout(2000)
    page.close()

def test_mouse_rightclick(page: Page):
    page.goto("http://swisnl.github.io/jQuery-contextMenu/demo.html")

    button = page.locator(".context-menu-one")
    button.click(button="right")

    page.wait_for_timeout(5000)
    page.close()

def test_mouse_doubleclick(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    btncopy = page.locator("button[ondblclick='myFunction1()']")
    btncopy.dblclick()
    fd2 = page.locator("#field2")
    expect(fd2).to_have_value("Hello World!")

    page.wait_for_timeout(2000)
    page.close()

def test_mouse_draganddrop(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source = page.locator("#draggable")
    target = page.locator("#droppable")
    source.drag_to(target)

    page.wait_for_timeout(2000)
    page.close()


