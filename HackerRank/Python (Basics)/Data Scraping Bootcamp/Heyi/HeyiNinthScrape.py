import requests
import pandas as pd
import time
import playwright
from playwright.async_api import async_playwright
import re 
import nest_asyncio
import asyncio

nest_asyncio.apply()

async def get_text_content():
    url = 'https://forkast.news/plainspoken-binance-cofounder-good-stead/'

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent='Your Custom User Agent Here'
        )

        page = await context.new_page()
        await page.goto(url, wait_until='domcontentloaded')
        await page.wait_for_selector('body')

        text_content = await page.inner_text('body')

        await browser.close()

        with open('heyi_forkfast_interview.txt', 'w', encoding='utf-8') as text:
            text.write(text_content)
            print("Successfully Converted to Text File Format!")

asyncio.run(get_text_content())

text_filepath = 'D:\\Visual Studio Codes\\heyi_forkfast_interview.txt'

with open(text_filepath, 'r', encoding='utf-8') as text:
    data = text.read()

sentences = data.split('\n')
print(sentences)

strings = ['\n'.join(sentences[i:i+2]) for i in range(0, len(sentences), 2)]
print(strings)

df = pd.DataFrame(strings, columns=['Content'])
print(df)

df.to_csv('heyi_forkfast_interview.csv', index=False)
print("Converted to CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_forkfast_interview.csv'

df = pd.read_csv(csv_filepath)

def clean_content(text):
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)             # Replace multiple question marks with one
    text = re.sub(r'-{2,}', '-', text)              # Replace multiple hyphens with a single hyphen
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Content'] = df['Content'].apply(clean_content)
print(df)

df.to_csv('heyi_forkfast_interview.csv', index=False)
print("Successfully Cleaned the CSV File Format!")

filepath = 'D:\\Visual Studio Codes\\heyi_forkfast_interview.csv'
df = pd.read_csv(filepath)


df = df.iloc[8:53].reset_index(drop=True)
print(df)

keywords_dict =  {
    "Cryptocurrency": [
        "Binance", "BNB Token", "Regulation", "Security Breach", "Customer Service",
        "Crypto Exchange", "Blockchain", "DeFi", "Tokenomics"
    ],
    "He Yi": [
        "Cofounder", "Chief Marketing Officer", "Work-from-home", "Leadership Style",
        "Career Journey", "Public Profile", "Influence"
    ],
    "OKCoin": [
        "Market Share", "User Operations", "Marketing", "Crypto Exchange", "Chinese Market",
        "Partnerships"
    ],
    "Regulatory Challenges": [
        "China Ban", "Initial Coin Offerings", "Global Regulation", "Compliance", "Legal Issues"
    ],
    "Television": [
        "Travel Shows", "Hosting", "Chinese Television", "TV Industry", "Media Influence",
        "Show Formats"
    ],
    "Public Communications": [
        "Expanding Operations", "Regulatory Environment", "Public Relations", "Media Coverage",
        "Corporate Communication"
    ],
    "Motherhood": [
        "Work-Life Balance", "Mobile State", "Family Support", "Parenting Challenges", "Remote Work",
        "Childcare"
    ],
    "Education": [
        "Psychological Counseling", "English Class", "Educational Background", "Academic Challenges",
        "Continuous Learning"
    ]
}

def get_keywords(text):
    tags = []

    for categories, sub_categories in keywords_dict.items():
        if any(sub.lower() in text.lower() for sub in sub_categories):
            tags.append(categories)
    
    return ', '.join(tags)

df['Keyword'] = df['Content'].apply(get_keywords)

df['Keyword'] = df['Keyword'].replace('', 'He Yi')
print(df) 

df.to_csv('heyi_forkfast_interview.txt', index=False, sep='\t')
print("\nSuccessfully Scraped from the website : 'https://forkast.news/plainspoken-binance-cofounder-good-stead/'")



