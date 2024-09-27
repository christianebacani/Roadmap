# Import Libraries
from keybert import KeyBERT
import pandas as pd
import playwright
from playwright.async_api import async_playwright
import re 
import nest_asyncio
import asyncio

# Apply nest_asyncio function
nest_asyncio.apply()

# Function to get the text data from the website
async def get_text_content():
    # URL to Scrape
    url = 'https://www.linuxjournal.com/content/25-years-later-interview-linus-torvalds'

    # Inner function to create a web driver that will scrape the data from a website
    async with async_playwright() as pw:
        # Browser
        browser = await pw.chromium.launch(headless=True)

        # Custom Agent
        context = await browser.new_context(
            user_agent='Your Custom User Agent Here'
        )

        # Page
        page = await context.new_page()
        await page.goto(url, wait_until='domcontentloaded') # Wait for the content to be fully loaded
        await page.wait_for_selector('body') # Wait for the body content to be loaded
        
        text_content = await page.inner_text('body') # Get the text from the body content

        await browser.close() # Close the web driver

        # Save into CSV File
        with open('linus_torvalds_interview.csv', 'w', encoding='utf-8', newline='\n') as csv:
            csv.write(text_content)

# Run the function
asyncio.run(get_text_content())

# Access the Filepath
csv_filepath = 'D:\\Visual Studio Codes\\linus_torvalds_interview.csv'

# Read the CSV
with open(csv_filepath, 'r', encoding='utf-8', newline='\n') as csv:
    data = csv.read()

# Split into multiple rows
splitted_data = data.split('\n')

# Combined the rows by 2 sentences per rows
combined_sentences = [' '.join(splitted_data[word:word+2]) for word in range(0, len(splitted_data), 2)]

# Define the DataFrame with the combined rows
df = pd.DataFrame(combined_sentences, columns=['Content'])

# Remove empty rows
df = df[df['Content'].str.strip() != '']

print(df)

# Save into CSV File
df.to_csv('linus_torvalds_interview.csv', index=False)
print("Converted into CSV File Format!")

# Access the CSV File Path
csv_filepath = 'D:\\Visual Studio Codes\\linus_torvalds_interview.csv'

# Read the CSV
df = pd.read_csv(csv_filepath)

# Remove unnecessary rows
df = df.iloc[8:83]
print(df)

# Functions to clean the rows of dataframe using Regex
def cleaned_content(text):
    text = re.sub(r'[,.!?]*$', '', text)
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()

    return text

# Run the function
df['Content'] = df['Content'].apply(cleaned_content)

print(df)

# Initialize KeyBERT Model for Generating Keywords
model = KeyBERT('distilbert-base-nli-mean-tokens')

# Function to Generate Keywords using KeyBERT
def generate_keywords(text):

    # Extract keywords per rows
    keywords = [keyword for keyword, score in model.extract_keywords(text)]

    # Capitalize every keywords
    keywords_capitalize = [word.title() for word in keywords]

    return ', '.join(keywords_capitalize)

# Run the function
df['Keyword'] = df['Content'].apply(generate_keywords)
print(df)

# Save into CSV File
df.to_csv('linus_torvalds_interview.csv', index=False)
print("Converted into CSV File Format with Keywords")

# Access the CSV Filepath
csv_filepath = 'D:\\Visual Studio Codes\\linus_torvalds_interview.csv'

# Convert into Text File
textfile = csv_filepath.replace('.csv', '.txt')

# Write the Text File with the content from the CSV File
with open(textfile, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"Content\t\t'Keyword'\n")

    for i, row in df.iterrows():
        content = row.get('Content', 'No Content')
        keyword = row.get('Keyword', 'No Keyword')

        text.write(f"{content}\t\t'{keyword}'\n")
print("Successfully Scraped from the Website : https://www.linuxjournal.com/content/25-years-later-interview-linus-torvalds")


