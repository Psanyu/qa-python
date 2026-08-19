from sys import path

from playwright.sync_api import Page, expect

def test_singlefileUpload(page: Page):
   page.goto("https://testautomationpractice.blogspot.com/")

   file = [r"C:\Users\pandi\PycharmProjects\PythonProject\Plyrite\Test1.txt"]

   page.locator("#singleFileInput").set_input_files(file)
   page.locator("button:has-text('Upload Single File')").click()

   expect(page.locator("#singleFileStatus")).to_contain_text("Test1.txt")

   page.wait_for_timeout(5000)
   page.close()


def test_multiplefileUpload(page: Page):
   # Don't wait for all resources, just the DOM
   page.goto("https://testautomationpractice.blogspot.com/",wait_until="domcontentloaded")

   file = [r"C:\Users\pandi\PycharmProjects\PythonProject\Plyrite\Test1.txt",r"C:\Users\pandi\PycharmProjects\PythonProject\Plyrite\Test2.txt"]

   page.locator("#multipleFilesInput").set_input_files(file)
   page.locator("button:has-text('Upload Multiple Files')").click()

   expect(page.locator("body")).to_contain_text("Test1.txt")
   expect(page.locator("body")).to_contain_text("Test2.txt")

   page.wait_for_timeout(6000)
   page.close()