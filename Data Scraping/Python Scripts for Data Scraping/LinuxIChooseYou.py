# Import Libraries
from keybert import KeyBERT
import pandas as pd
import playwright
from playwright.async_api import async_playwright
import re 
import nest_asyncio
import asyncio

# Applying nest asycn function
nest_asyncio.apply()

# Define a async function to scrape data from a website
async def get_text_content():
    # URL of the Website
    url = 'https://dev.to/jimmymcbride/linux-i-choose-you-5ebe?ref=dailydev'

    # Nested asycn function for defining the parameters of the web driver
    async with async_playwright() as pw:
        # Define the browser for isolated Web Scraping
        browser = await pw.chromium.launch(headless=False)

        # Defining the user agent
        context = await browser.new_context(
            user_agent='Your Custom User Agent Here'
        )

        # Create new page based on the browser
        page = await context.new_page()

        # Define a new page and go to the defined URL with help of user custom agent
        await page.goto(url, wait_until='domcontentloaded')

        # Function to wait until the HTML content are fully loaded
        await page.wait_for_selector('body')

        # Fetch the inner text element
        content = await page.inner_text('body')

        # Close the browser
        browser.close()

        # Function to write a content inside the file using the fetched data
        with open('Linux, I Choose You!.csv', 'w', encoding='utf-8', newline='\n') as text:
            text.write(content)
        
        text.close() # Close the file

# Execute the async main function
asyncio.run(get_text_content())


# Function to read the content of the existing file
with open('Linux, I Choose You!.csv', 'r', encoding='utf-8', newline='\n') as text:
    data = text.read() # Read function

text.close() # Close the file

# Display the content of the whole file
print(data)

# Join multiple data into single string
rows = data.split('\n')

# Parsed into DF
df = pd.DataFrame(rows, columns=['Dev Blog'])
print(df)

# Remove empty rows
df = df[df['Dev Blog'].str.strip() != '']
print(df)

# Remove unnessary rows
df = df.iloc[24:41].reset_index(drop=True)

# Save into CSV
df.to_csv('Linux, I Choose You!.csv', index=False)
print("Successfully Convert it into CSV File!")


# Read the CSV
df = pd.read_csv('Linux, I Choose You!.csv')


# Clean Content Function
def clean_content(text):
    # Function to clean text using Regex
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', ' ', text)

    text = text.strip() # Remove whitespaces

    return text

# Execute the function
df['Dev Blog'] = df['Dev Blog'].apply(clean_content)
print(df)

# Save the CSV File
df.to_csv('Linux, I Choose You!.csv', index=False)

# CSV File
csvfile = 'Linux, I Choose You!.csv'

# Convert File Format
textfile = csvfile.replace('.csv', '.txt')


# Function to modify the content of the file
with open(textfile, 'w', encoding='utf-8', newline='\n') as text:
    # For loop the write the content of the file
    for i, row in df.iterrows():
        # Fetch the row inside the column
        data = row.get('Dev Blog', 'No Dev Blog')

        # Reformat the structure to text file 
        if data in ['Ownership', 'Freedom', 'Open Source', 'Morals', 'Conclusion']:
            text.write(f"\n'{data.upper()}'\n")
        
        else:
            text.write(f"{data}\n")
        
# Close the file
text.close()

# Display a message
print("Successfully Extracted the Data!")



