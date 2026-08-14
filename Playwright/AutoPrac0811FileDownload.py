from playwright.sync_api import Page
from pathlib import Path
import os

def test_FileDownload(page: Page):
   page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html", wait_until="domcontentloaded")

   #fills text in textarea to be generated
   page.locator("textarea#inputText").fill("Download Tests")

   page.locator("button#generateTxt").click()

   page.wait_for_load_state("domcontentloaded")

   with page.expect_download() as download_info:
      page.locator("a#txtDownloadLink").click()

   download = download_info.value
   save_path = Path(r"C:\Users\pandi\Downloads") / "info.txt"
   download.save_as(save_path)

   # Verify download
   assert save_path.exists(), "File was not downloaded"
   assert download.suggested_filename == "info.txt"


def test_FileDownload2(page: Page):
   page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html", wait_until="domcontentloaded")

   #fills text in textarea to be generated
   page.locator("textarea#inputText").fill("Download Tests")

   page.locator("button#generateTxt").click()

   page.on("download", lambda download: download.save_as("downloads/testfile.txt"))

   page.locator("a#txtDownloadLink").click()

   if os.path.exists("downloads/testfile.txt"):
      print("transfered file exists")
   else:
      print("transfered file does not exist")

   page.wait_for_timeout(5000)
   page.close()




