import requests
import pandas as pd
import time
import playwright
from playwright.async_api import async_playwright
import nest_asyncio
import asyncio
import re

nest_asyncio.apply()

async def get_text_content():
    url = 'https://coingape.com/did-binance-really-seize-crypto-from-palestinians/'

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)

        context = await browser.new_context(
            user_agent='Your Custom User Agent Here'
        )

        page = await context.new_page()
        await page.goto(url, wait_until='domcontentloaded')
        await page.wait_for_selector('body')
        text_content = await page.inner_text('body')

        await browser.close()

        with open('binance_seizure_claims.csv', 'w', encoding='utf-8', newline='\n') as text:
            text.write(text_content)

asyncio.run(get_text_content())

with open('binance_seizure_claims.csv', 'r', encoding='utf-8', newline='\n') as txt:
    data = txt.read()

sentences = data.split('\n')
combined_sentences = [' '.join(sentences[i:i+2]) for i in range(0, len(sentences), 2)]

df = pd.DataFrame(combined_sentences, columns=['Content'])
print(df)

df.to_csv('binance_seizure_claims.csv', index=False)
print("Successfully Converted to CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\binance_seizure_claims.csv'

df = pd.read_csv(csv_filepath)

df = df.iloc[10:30].reset_index(drop=True)

def cleaned_content(text):
    text = re.sub(r'/+', '', text)
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    text = text.strip()

    text = re.sub(r'\.\+', '. ', text)
    text = re.sub(r'\?\+', ' ', text)
    text = re.sub(r'\!\+', ' ', text)

    return text

df['Content'] = df['Content'].apply(cleaned_content)


keywords_dict = {
    "Hot Topic Buzz": ["Binance", "Seizure"],
    "Power Players": ["Yi He", "Poppe"],
    "Scandal Scoop": ["Assets", "Illicit Funds"],
    "Moment in Time": ["August", "2024"],
    "Law Watch": ["Anti-Money", "Laundering"],
    "Crowd Reaction": ["Backlash", "Denial"],
    "Crypto Surge": ["Market", "Recovery"],
    "Viral Quotes": ["Hundred Accounts", "Blockchain"],
    "Price Action": ["Bitcoin", "Ethereum"],
    "Where It’s Trending": ["Social Media", "X"],
    "Binance Narrative": ["Refuted", "Compliant"],
    "User Hotspot": ["Access", "Funds"],
    "Market Pulse": ["Price Surge", "Rally"],
    "Expert Take": ["False Claims", "Propaganda"],
    "Coin Focus": ["Bitcoin", "Ethereum"],
    "User Impact": ["Limited Access", "Illicit Use"],
    "Safety First": ["AML Laws", "Compliance"],
    "Breaking Rumors": ["Rumors", "Allegations"],
    "Investor Vibes": ["Uptrend", "Recovery"]
}


def generate_keywords(text):
    keywords = []

    for topics, sub_categories in keywords_dict.items():
        if any(word.lower() in text.lower() for word in sub_categories):
            keywords.append(topics)
    
    return ', '.join(keywords)

df['Topic'] = df['Content'].apply(generate_keywords)

df['Topic'] = df['Topic'].replace('', 'He Yi')
print(df)

not_included = [2, 8, 13, 14, 15, 16, 17]

mask = ~df.index.isin(not_included)
df = df[mask].reset_index(drop=True)

df.to_csv('heyi_binance_seizure_claims.txt', index=False, sep='\t')
print("Succesfully Scraped!")

