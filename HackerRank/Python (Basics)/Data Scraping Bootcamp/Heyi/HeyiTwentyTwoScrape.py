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
    url = 'https://en.bitcoinsistemi.com/binance-co-founder-yi-he-responded-to-wsj-claims/?utm_source=CryptoNews&utm_medium=app'

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)

        context = await browser.new_context(
            user_agent='Your Customer User Agent Here'
        )

        page = await context.new_page()
        await page.goto(url, wait_until='domcontentloaded')
        await page.wait_for_selector('body')
        text_content = await page.inner_text('body')

        await browser.close()

        with open('heyi_wsj_claims.csv', 'w', encoding='utf-8', newline='\n') as text:
            text.write(text_content)

asyncio.run(get_text_content())

with open('heyi_wsj_claims.csv', 'r', encoding='utf-8', newline='\n') as text:
    data = text.read()

sentences = data.split('\n')
combined_sentences = [' '.join(sentences[i:i+2]) for i in range(0, len(sentences), 2)]

df = pd.DataFrame(combined_sentences, columns=['Content'])

df = df[df['Content'].str.strip() != '']

df.to_csv('heyi_wsj_claims.csv', index=False)

csv_filepath = 'D:\\Visual Studio Codes\\heyi_wsj_claims.csv'

df = pd.read_csv(csv_filepath)


def cleaned_content(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = text.strip()

    return text

df['Content'] = df['Content'].apply(cleaned_content)

df = df.iloc[14:29].reset_index(drop=True)
print(df)


keywords_dict = {
    "Binance Whistleblower Drama": ["Binance", "WSJ", "DWF", "Labs", "manipulation", "altcoins", "token", "prices"],
    "Denial Blitz": ["denied", "spokesperson", "Cointelegraph", "claims", "framework", "abuse", "action"],
    "Maker vs Maker Showdown": ["makers", "competition", "behavior", "fairness", "fraudulent", "target"],
    "Yi He’s Mic Drop": ["Yi", "He", "sarcastic", "targeted", "investment", "privileged", "thanks"],
    "WSJ Bias Exposed": ["bias", "reporting", "Zkasino", "culprit", "enforcement", "budget", "arrest"],
    "Crypto Clapback": ["Twitter", "post", "statement", "exposure", "marketing", "grateful", "account"],
    "Hashtag Mania": ["Binance", "BNB", "Bitcoin", "BTC", "Crypto", "trending", "hashtags"],
    "Regulatory Face-Off": ["law", "regulations", "auditors", "compliance", "terms", "surveillance"],
    "Altcoin Price Shenanigans": ["YGG", "tokens", "altcoins", "market", "prices", "activity", "pumping"],
    "Fraud Alert Headlines": ["allegations", "fraud", "denied", "DWF", "WSJ", "claims", "accusations"],
    "PR Powerplay": ["Binance", "spokesperson", "claims", "denied", "official", "response", "media"],
    "Market Watchdog Mode": ["surveillance", "program", "framework", "detects", "abuse", "enforcement", "action"],
    "Regulators Closing In": ["regulatory", "auditors", "law", "actions", "compliance", "fairness", "governance"],
    "Crypto Price Wars": ["market", "prices", "competition", "tokens", "altcoins", "activity", "behavior"],
    "Yi He’s Twitter Roast": ["Yi", "He", "statement", "thanks", "long-term", "bias", "reporting"]
}


def generate_keywords(text):
    keywords = []
    text_lower = text.lower()

    for topics, sub_topics in keywords_dict.items():
        if any(word.lower() in text_lower for word in sub_topics):
            keywords.append(topics)
    return ', '.join(keywords)

df['Topic'] = df['Content'].apply(generate_keywords)

df['Topic'] = df['Topic'].replace('', 'He Yi')

df.to_csv('heyi_wsj_claims.txt', index=False, sep='\t')
print("Successfully Scraped!")





