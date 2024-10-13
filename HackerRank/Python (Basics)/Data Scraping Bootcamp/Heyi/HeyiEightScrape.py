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
    url = 'https://www.cityam.com/binances-yi-he-my-talent-has-always-been-trying-to-challenge-myself/'

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context(user_agent='Your Custom User Agent Here')

        page = await context.new_page()
        await page.goto(url, wait_until='domcontentloaded')
        await page.wait_for_selector('body')

        text_content = await page.inner_text('body')

        await browser.close()

        with open('heyi_challenge_mindset.txt', 'w', encoding='utf-8') as text:
            text.write(text_content)
            print("Successfully Created the Text File Format!")

asyncio.run(get_text_content())

text_filepath = 'D:\\Visual Studio Codes\\heyi_challenge_mindset.txt'

with open(text_filepath, 'r', encoding='utf-8') as text:
    data = text.read()

sentences = data.split('\n')

strings = [' '.join(sentences[i:i+3]) for i in range(0, len(sentences), 3)]

df = pd.DataFrame(strings, columns=['Content'])

def clean_content(text):
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)             # Replace multiple question marks with one
    text = re.sub(r'-{2,}', '-', text)              # Replace multiple hyphens with a single hyphen
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Content'] = df['Content'].apply(clean_content)

df.to_csv('heyi_challenge_mindset.csv', index=False)
print("Converted to CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_challenge_mindset.csv'

df = pd.read_csv(csv_filepath)
print(df)

df = df.iloc[4:38].reset_index(drop=True)
print(df)

keywords_dict = {
    "Crypto Industry": [
        "Binance", "OkCoin", "cryptocurrency", "Bitcoin", "blockchain", "digital assets", 
        "crypto space", "crypto exchange", "BNB Chain", "DappBay"
    ],
    "Leadership": [
        "Yi He", "CZ", "Changpeng Zhao", "founder", "co-founder", 
        "chief marketing officer", "CEO", "leadership", "captain"
    ],
    "Financial Regulation": [
        "FCA", "financial conduct authority", "regulatory", "permissions", 
        "compliance", "Digivault", "Equonex", "UK", "Paris", "Dubai", 
        "financial regulators", "approval", "warning", "risk"
    ],
    "Business Operations": [
        "transactions", "employees", "users", "business activities", "global company", 
        "regional headquarters", "growth", "market expansion", "operations", 
        "public listing", "shareholders", "investors", "staff", "success"
    ],
    "Marketing": [
        "branding", "customer service", "PR", "public relations", "media", 
        "social media", "Twitter", "branding division", "promotion", "public figurehead"
    ],
    "Tech & Innovation": [
        "blockchain technology", "crypto exchange", "new technology", 
        "skills", "innovation", "technology whizz", "simplifying technology", 
        "transformation", "digital financial system"
    ],
    "Hiring & Talent": [
        "staff", "hiring", "talent pool", "employees", "best people", 
        "recruitment", "job market", "talent", "workforce", "job search"
    ],
    "Gender & Diversity": [
        "women", "gender", "education", "tech sector", "male dominated", 
        "cultural problem", "societal expectations", "diversity", 
        "gender equality", "gender roles"
    ],
    "Investment & Growth": [
        "public listing", "shareholders", "investors", "growth", "expansion", 
        "investment", "future", "opportunities", "financial success"
    ],
    "Challenges": [
        "challenge", "regulatory attention", "hiring challenges", "changes", 
        "competition", "limitations", "risks", "job turnover", "uncertainty"
    ]
}

def generate_keywords(text):
    tags = []

    for categories, sub_categories in keywords_dict.items():
        if any(sub.lower() in text.lower() for sub in sub_categories):
            tags.append(categories)
    return ', '.join(tags)

df['Keyword'] = df['Content'].apply(generate_keywords)

df['Keyword'] = df['Keyword'].replace('', 'He Yi')

print(df)

df.to_csv('heyi_submission_3_content.txt', index=False, sep='\t')
print("Successfully Scraped!")
