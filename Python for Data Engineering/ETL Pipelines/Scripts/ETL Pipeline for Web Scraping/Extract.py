from playwright.async_api import async_playwright
import nest_asyncio
import asyncio

# Extract Phase

nest_asyncio.apply()

# Function to get text content
async def get_text_content():
    url = 'https://medium.com/towards-data-engineering/data-architecture-a-brief-overview-a93286f3e1f7'

    async with async_playwright() as pw :
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent='Your Custom User Agent Here'
        )
            
        page = await context.new_page()
        await page.goto(url, wait_until='domcontentloaded')
        await page.wait_for_selector('body')
        content = await page.inner_text('body')
        
        await browser.close()   

        # Store the text content inside the csv file
        with open('D:\\Visual Studio Codes\\Data Engineering Projects in Python\\ETL Pipeline\\Source Data Files\\data_architecture_article.csv', 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)


