# Import Libraries
from keybert import KeyBERT
import pandas as pd
import playwright
from playwright.async_api import async_playwright
import re 
import nest_asyncio
import asyncio

# Making sure nest_asyncio is applicable for our function
nest_asyncio.apply()

# Asynchronous function for Scraping the Website
async def get_text_content():
    url = 'https://lelouch.dev/blog/you-are-probably-not-dumb/?ref=dailydev'

    # Function to scrape the data inside the website using playwright
    async with async_playwright() as pw:
        # Browser
        browser = await pw.chromium.launch(headless=True)

        # Custom Agent
        context = await browser.new_context(
            user_agent='Your Custom User Agent Here'
        )

        # Create a new page based from the browser
        page = await context.new_page()
        await page.goto(url, wait_until='domcontentloaded') # Specify the URL and wait until the content is loaded

        # Wait for the body element inside the Website
        await page.wait_for_selector('body')

        # Get the text from the body content
        text_content = await page.inner_text('body')
        
        # Close the browser
        await browser.close()

        # Save into CSV File
        with open('motivational_learnings.csv', 'w', encoding='utf-8', newline='\n') as csv:
            csv.write(text_content)

# Call the function
asyncio.run(get_text_content())

# CSV Filepath
csv_filepath = 'D:\\Visual Studio Codes\\motivational_learnings.csv'

# Read the CSV Filepath
with open(csv_filepath, 'r', encoding='utf-8', newline='\n') as csv_file:
    data = csv_file.read()

# Split into multiple rows
splitted_text = data.split('\n')

# Parse into a list using loop
combined_sentences = [' '.join(splitted_text[word:word+2]) for word in range(0, len(splitted_text), 2)]

# Define into a Dataframe
df = pd.DataFrame(combined_sentences, columns=['Content'])
print(df)

# Remove null rows
df = df[df['Content'].str.strip() != '']

# Include only necessary rows
df = df.iloc[11:27]

# Clean the rows
def cleaned_content(text):
    text = re.sub(r'[.,!?]*$', '', text)
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = text.strip()

    return text
# Call the function
df['Content'] = df['Content'].apply(cleaned_content)

print(df)

# Model for Generating Keywords using KeyBERT
model = KeyBERT('distilbert-base-nli-mean-tokens')

# Function to Generate Keywords
def generate_keywords(text):

    # Store the keywords/s inside the list
    keywords = [keyword for keyword, score in model.extract_keywords(text)]

    # Mapped the keyword/s into capitalize keyword/s and store in the list
    capitalize_keywords = [word.title() for word in keywords]
    
    # Return the keyword/s
    return ', '.join(capitalize_keywords)

# Call the function
df['Keyword'] = df['Content'].apply(generate_keywords)

print(df)

# Save into CSV File
df.to_csv('motivational_learnings.csv', index=False)
print("Successfuly Converted into CSV File Format!")

# CSV Filepath
csv_filepath = 'D:\\Visual Studio Codes\\motivational_learnings.csv'

# Convert into Text File
textfile = csv_filepath.replace('.csv', '.txt')

# Save the Converted Text file into another file
with open(textfile, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"Content\t'Keyword'\n")
    for i, row in df.iterrows():
        content = row.get('Content', 'No Content')
        keyword = row.get('Keyword', 'No Keyword')
        text.write(f"{content}\t'{keyword}'\n")

print("Successfully Scraped!")
