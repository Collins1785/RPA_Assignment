import asyncio
from playwright.async_api import async_playwright

async def run():
    url = "https://www.tnebnet.org/awp/login"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to TNEB portal
        await page.goto(url, wait_until="networkidle")

        # Extract only visible text from the page
        page_text = await page.inner_text("body")

        # Save to .txt file
        output_file = "tneb_output.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(page_text)

        print(f"Text content saved to {output_file}")

        await browser.close()

asyncio.run(run())