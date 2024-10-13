import requests
import pandas as pd
import time
import playwright
from playwright.async_api import async_playwright
import nest_asyncio
import asyncio
import re 

# Defines asynchronous nesting
nest_asyncio.apply()

# Defines Asynchronous Functions
async def get_text_content():
    url = 'https://www.binance.com/en/square/post/8354085953778'

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)

        context = await browser.new_context(
            user_agent = 'Your Custom User Agent Here'
        )

        page = await context.new_page()
        await page.goto(url, wait_until='domcontentloaded')
        await page.wait_for_selector('body')

        text_data = await page.inner_text('body')

        await browser.close()

        with open('heyi_biography.txt', 'w', encoding='utf-8') as file:
            file.write(text_data)
            print("Successfully Extracted a Data From the Website!") 

asyncio.run(get_text_content())

text_filepath = 'D:\\Visual Studio Codes\\heyi_biography.txt'

with open(text_filepath, 'r', encoding='utf-8') as read_file:
    data = read_file.read()

print(data)

sentences = data.split('. ')
print(sentences)

combined_sentences = ['. '.join(sentences[i:i+2]) for i in range(0, len(sentences), 2)]
print(combined_sentences)

df = pd.DataFrame(combined_sentences, columns=['Content'])
print(df)

df.to_csv('heyi_biography.csv', index=False)
print("Successfully Created a CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_biography.csv'

df = pd.read_csv(csv_filepath)

df = df[df['Content'].str.strip() != '']

def cleaned_content(text):
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Content'] = df['Content'].apply(cleaned_content)

print(df)

df = df.iloc[1:38].reset_index(drop=True)
print(df)

df.to_csv('heyi_biography_cleaned.csv', index=False)
print("Successfully Cleaned the Data!")

df = pd.read_csv('heyi_biography_cleaned.csv')

keywords_dict = {
    "Crypto": [
        "cryptocurrency",
        "blockchain",
        "digital assets",
        "mining",
        "smart contracts",
        "decentralized finance (DeFi)",
        "NFTs (Non-Fungible Tokens)"
    ],
    "Binance": [
        "cryptocurrency exchange",
        "trading platform",
        "Binance Coin (BNB)",
        "spot trading",
        "futures trading",
        "staking",
        "Binance Smart Chain"
    ],
    "China": [
        "economic growth",
        "regulations on crypto",
        "blockchain innovation",
        "tech industry",
        "digital yuan",
        "Great Firewall",
        "China's approach to cryptocurrency"
    ],
    "He Yi/Yi He": [
        "entrepreneur",
        "tech innovation",
        "business ventures",
        "leadership",
        "investments in blockchain",
        "founder",
        "strategic partnerships"
    ],
    "Leadership": [
        "visionary leader",
        "business strategy",
        "crisis management",
        "public speaking",
        "mentorship",
        "decision-making",
        "team management"
    ],
    "Women in Tech": [
        "female entrepreneur",
        "gender diversity in tech",
        "inspiring women leaders",
        "women empowerment",
        "breaking glass ceiling",
        "women in blockchain",
        "role model"
    ],
    "Business Development": [
        "market expansion",
        "user acquisition",
        "business growth",
        "partnerships",
        "investor relations",
        "marketing strategy",
        "brand development"
    ],
    "Technology": [
        "AI",
        "cloud computing",
        "software development",
        "blockchain technology",
        "machine learning",
        "fintech",
        "innovation in tech"
    ],
    "Financial Market": [
        "cryptocurrency market",
        "trading volumes",
        "market analysis",
        "financial regulations",
        "investment strategies",
        "digital assets trading",
        "market trends"
    ],
    "Legal and Regulations": [
        "compliance",
        "crypto regulations",
        "SEC lawsuit",
        "government policies",
        "financial crime",
        "asset freeze",
        "regulatory framework"
    ],
    "Media and Public Relations": [
        "public relations",
        "media appearances",
        "brand image",
        "social media presence",
        "press releases",
        "interviews",
        "marketing campaigns"
    ]
}

default_keyword = ['Journey of He Yi']

def generate_keywords(text):
    tags = []

    for category, sub_category in keywords_dict.items():
        if any(sub.lower() in text.lower() for sub in sub_category):
            tags.append(category)
    return ', '.join(tags)

df['Keyword'] = df['Content'].apply(generate_keywords)

print(df)

df['Keyword'] = df['Keyword'].replace('', 'Journey of He Yi')
print(df)

df.to_csv('heyi_journey.csv', index=False)
print("Converted to CSV File Format with Keywords and Cleaned!")


filepath = 'D:\\Visual Studio Codes\\heyi_journey.csv'

df = pd.read_csv(filepath)

df.dropna(how='all', inplace=True)

print(df)

text_file = filepath.replace('.csv', '.txt')

with open(text_file, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"Content    Keyword\n")

    for i,row in df.iterrows():
        contents = row.get('Content', 'No Content')
        keywords = row.get('Keyword', 'No Keyword')

        text.write(f"{contents}:    {keywords}\n")
print("Successfully Scraped!")













