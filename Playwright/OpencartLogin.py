import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_lgin():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://localhost/opencart/index.php?route=account/login&language=en-gb")
        await expect(page).to_have_url("http://localhost/opencart/index.php?route=account/login&language=en-gb")
        await browser.close()


