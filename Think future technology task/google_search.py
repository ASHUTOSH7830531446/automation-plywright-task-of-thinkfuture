import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # Set headless=True for running in background
        page = await browser.new_page()
        print("Navigating to Google...")
        await page.goto("https://www.google.com")
        print("Google page loaded.")

        search_query = "what is the future of sdet role in it"
        print(f"Searching for: '{search_query}'")

        # Locate the search input field and fill it
        # Google's search input often has the name 'q' or an aria-label like 'Search'
        # We can also use a more generic selector if 'name="q"' doesn't work, e.g., 'input[aria-label="Search"]'
        await page.fill('textarea[name="q"]', search_query)

        # Press Enter to submit the search
        await page.press('textarea[name="q"]', 'Enter')

        print("Search submitted. Waiting for results...")
        # Optional: Wait for navigation or a specific element to appear
        await page.wait_for_selector('#search') # Wait for the search results container

        print("Search results page loaded. Keeping browser open for 5 seconds for visual inspection.")
        await asyncio.sleep(5) # Keep the browser open for a few seconds to see the results

        await browser.close()
        print("Browser closed.")

if __name__ == "__main__":
    asyncio.run(main())
