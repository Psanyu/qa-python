import pytest
from playwright.sync_api import Page,expect

def test_N5(page:Page):
    page.goto("http://localhost:4000")
    myurl=page.url

#How to use page.on with dialogue box event with lambda and altered inner text in dialog box
    frames= page.frames
    print("No. of frames on Page:",len(frames))

    page.wait_for_timeout(5000)


    page.close()

