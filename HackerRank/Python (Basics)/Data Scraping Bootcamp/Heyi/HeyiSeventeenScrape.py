# Import necessary libraries
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
    url = 'https://coingape.com/binance-co-founder-optimistic-amidst-czs-legal-situation/'

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)

        context = await browser.new_context(
            user_agent='Your Customer User Agent Here'
        )

        page = await context.new_page()
        await page.goto(url, wait_until='domcontentloaded')
        await page.wait_for_selector('body')
        text_content = await page.inner_text('body')

        browser.close()

        with open('heyi_binance_legal_peaceful.csv', 'w', encoding='utf-8', newline='\n') as text:
            text.write(text_content)

asyncio.run(get_text_content())
print("Succesfully Converted to CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_binance_legal_peaceful.csv'

with open('heyi_binance_legal_peaceful.csv', 'r', encoding='utf-8', newline='\n') as text:
    data = text.read()

sentences = data.split('\n')
combined_sentences = [' '.join(sentences[i:i+2]) for i in range(0, len(sentences), 2)]

df = pd.DataFrame(combined_sentences, columns=['Content'])
print(df)

csv = df.to_csv('heyi_binance_legal_peaceful.csv', index=False)
print(f"Converted to {csv}")

filepath = 'D:\\Visual Studio Codes\\heyi_binance_legal_peaceful.csv'

df = pd.read_csv(filepath)

df = df.iloc[13:24]
print(df)

def cleaned_content(text):
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    text = re.sub(r'\.\s+', '. ', text)
    text = re.sub(r'\!\s+', '! ', text)
    text = re.sub(r'\?\s+', ' ', text)

    text = text.strip()

    return text


df['Content'] = df['Content'].apply(cleaned_content)
print(df)

keywords_dict = {
    "Legal Battles": ["settlement", "forfeiture", "sentencing", "plea", "scrutiny"],
    "Corporate Shakeup": ["Binance", "Richard Teng", "resignation", "board overhaul", "leadership change"],
    "Key Figures": ["He Yi", "CZ", "shareholder", "influence", "personal connection"],
    "High-Stakes Events": ["conference", "Token2049", "Dubai summit", "global meetup", "VASP license"],
    "Regulatory Moves": ["compliance", "regulatory framework", "confidence boost", "proactive strategy", "guidelines"],
    "Leadership Transition": ["CEO exit", "power shift", "new direction", "organizational restructure", "Teng's vision"],
    "Financial Impact": ["$4.3 billion", "company forfeiture", "asset loss", "corporate fines", "financial settlement"],
    "Media Buzz": ["press coverage", "public perception", "industry reaction", "headlines", "media attention"],
    "Strategic Vision": ["long-term planning", "business roadmap", "future outlook", "stability goals", "expansion plans"],
    "Crisis Management": ["damage control", "legal defense", "public reassurance", "internal stability", "challenges ahead"]
}


def generate_keywords(text):
    keywords = []

    for topics, categories in keywords_dict.items():
        if any(word.lower() in text.lower() for word in categories):
            keywords.append(topics)
    
    return ', '.join(keywords)


df['Topic'] = df['Content'].apply(generate_keywords)

df['Topic'] = df['Topic'].replace('', 'He Yi')
print(df)

text_filepath = df.to_csv('heyi_binance_legal_peaceful.txt', index=False, sep='\t')
print(f"Successfully Scraped!")


