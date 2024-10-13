# Import Libraries
from keybert import KeyBERT
import pandas as pd
from playwright.async_api import async_playwright
import re 
import nest_asyncio
import asyncio

# Apply nested async function
nest_asyncio.apply()

# Asynchronous function to get text content
async def get_text_content():
    url = 'https://dev.to/llxd/beginners-guide-to-freelancing-3m5i?ref=dailydev' # Specify the URL

    # Nested asynch function to create web driver to scrape data
    async with async_playwright() as pw:
        # Define the browser parameter
        browser = await pw.chromium.launch(headless=True)

        # User agent
        context = await browser.new_context(
            user_agent='Custom Agent'
        )

        # Create new page
        page = await context.new_page()
        # Specify the URL from the new page
        await page.goto(url, wait_until='domcontentloaded')

        # Wait for the body element from HTML Element to be loaded
        await page.wait_for_selector('body')

        # Fetch the text element inside the body element
        text_element = await page.inner_text('body')

        # Close the web driver browser
        await browser.close()

        # Create a CSV File from and load the content from the fetched data
        with open('freelancing_tips.csv', 'w', encoding='utf-8', newline='\n') as text:
            text.write(text_element)
    
        text.close()

# Execute the async function
asyncio.run(get_text_content())

# File function to open the Loaded CSV File and read the whole content
with open('freelancing_tips.csv', 'r', encoding='utf-8', newline='\n') as text:
    data = text.read()

# Parse the read content into a DataFrame
df = pd.DataFrame(data.split('\n'), columns=['Article'])
print(df)

# Remove empty rows
df = df[df['Article'].str.strip() != '']
print(df)

# Remove unncessary rows
df = df.iloc[26:75].reset_index(drop=True)

# Save into the existing CSV (Overwriting)
df.to_csv('freelancing_tips.csv', index=False)
print("Successfully Parsed and Pre-Cleaned the Data!")

# Read the CSV File
df = pd.read_csv('freelancing_tips.csv')

# Function to clean the content inside the CSV using Regex
def clean_content(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = text.strip()

    return text

# Execute the function
df['Article'] = df['Article'].apply(clean_content)
print(df)

# Load the KeyBERT Model for Generating Keywords
model = KeyBERT('distilbert-base-nli-mean-tokens')

# Function to Generate Keywords
def generate_keywords(data):
    # Generate keywords for every rows
    keywords = [keyword for keyword, score in model.extract_keywords(data)]

    # Capitalize every keywords
    formatted_keywords = [word.capitalize() for word in keywords]

    # Return into Comma Separated Format
    return ', '.join(formatted_keywords)

# Execute the function
df['Category'] = df['Article'].apply(generate_keywords)
print(df)

df.to_csv('freelancing_tips.csv', index=False)
print("Successfully Enriched the Data!")

csv_file = 'freelancing_tips.csv'

text_file = csv_file.replace('.csv', '.txt')

with open(text_file, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"Row\tArticle\t'Keywords'\n")

    for i, row in df.iterrows():
        article = row.get('Article', 'No Article')
        category = row.get('Category', 'No Category')

        text.write(f"{i + 1}\t{article}\t'{category}'\n")

# Close the File
text.close()
print("Successfully Scraped from a Website!")

