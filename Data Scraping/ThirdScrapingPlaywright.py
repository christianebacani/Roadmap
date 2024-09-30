# Import Libraries/Modules
from keybert import KeyBERT
import pandas as pd
import playwright
from playwright.async_api import async_playwright
import re 
import nest_asyncio
import asyncio

# Apply nest_asyncio function for the script
nest_asyncio.apply()

# Function to get text content from the website
async def get_text_content():
    # URL
    url = 'https://muratbuffalo.blogspot.com/2024/07/advice-to-young.html?ref=dailydev'

    # Inner async function to scrape data using chromium web driver
    async with async_playwright() as pw:
        # Parameters of Web Browser
        browser = await pw.chromium.launch(headless=True)

        # User agent
        context = await browser.new_context(
            user_agent='Your Custom User Agent Here'
        )

        # New page
        page = await context.new_page()
        # Go to url
        await page.goto(url, wait_until='domcontentloaded')
        # Wait for the body div element to be loaded
        await page.wait_for_selector('body')
        
        # Get the inner text
        text_content = await page.inner_text('body')

        # Close the web driver
        await browser.close()
        
        # Write the csv file content using the text data from the website
        with open('advice_to_young.csv', 'w', encoding='utf-8', newline='\n') as text:
            text.write(text_content)

# Execute the function
asyncio.run(get_text_content()) 

# Open the file and read the whole content
with open('D:\\Visual Studio Codes\\advice_to_young.csv', 'r', newline='\n', encoding='utf-8') as text:
    data = text.read()

# Split the single coherent string into multiple rows
splitted_data = data.split('\n')

# Combine two sentences per rows
sentences = [' '.join(splitted_data[word:word+2]) for word in range(0, len(splitted_data), 2)]

# Create dataframe based on the rows
df = pd.DataFrame(sentences, columns=['Content'])

# Remove empty rows
df = df[df['Content'].str.strip() != '']
print(df)

# Save into CSV to analyze manually the data for possible cleaning methods
df.to_csv('advice_to_young.csv', index=False)

# Read the CSV
df = pd.read_csv('advice_to_young.csv')

# Remove unnecessary rows
df = df.iloc[4:32].reset_index(drop=True)
print(df)

# Function to clean the data using Regex
def cleaned_content(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'[,.!?]*$', '', text)
    text = text.strip()

    return text

df['Content'] = df['Content'].apply(cleaned_content)
print(df)

# KeyBERT Model for Generating Keywords
model = KeyBERT('distilbert-base-nli-mean-tokens')

# Function to Generate Keyword/s using KeyBERT Model
def generate_keywords(text):
    # Loop through each line to generate keywords
    keywords = [keyword for keyword, score in model.extract_keywords(text)]

    # Loop through each keyword to capitalize it from the list and store it inside another list
    keywords_capitalize = [word.title() for word in keywords]

    # Return as a single string
    return ', '.join(keywords_capitalize)

df['Keyword'] = df['Content'].apply(generate_keywords)
print(df)

# Save the Enriched Data into CSV 
df.to_csv('advice_to_young.csv', index=False)

# Replace File Format!
textfile = 'advice_to_youngs.csv'.replace('.csv', '.txt')

# Modify the text file with the content from the CSV File
with open(textfile, 'w', encoding='utf-8', newline='\n') as text:
    for i, row in df.iterrows():
        content = row.get('Content', 'No Content')
        keyword = row.get('Keyword', 'No Keyword')

        text.write(f"{content}\tKeywords: '{keyword}'\n")
        
print("Successfully Scraped!")

