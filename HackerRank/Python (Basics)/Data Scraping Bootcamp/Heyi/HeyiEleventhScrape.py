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
    url = 'https://www.binance.com/en-IN/square/post/2023-10-30-1564286'

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

        with open('heyi_women_development.txt', 'w', encoding='utf-8', newline='\n') as text:
            text.write(text_content)

asyncio.run(get_text_content())

text_filepath = 'D:\\Visual Studio Codes\\heyi_women_development.txt'

with open(text_filepath, 'r', encoding='utf-8', newline='\n') as text:
    data = text.read()

sentences = data.split('\n')

combined_sentences = [' '.join(sentences[i:i+2]) for i in range(0, len(sentences), 2)]

df = pd.DataFrame(combined_sentences, columns=['Content'])
print(df)

df.to_csv('heyi_women_development.csv', index=False)
print("Converted to CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_women_development.csv'

df = pd.read_csv(csv_filepath)

df = df.iloc[10:71].reset_index(drop=True)
print(df)

def cleaned_content(text):
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)             # Replace multiple question marks with one
    text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text) # Remove special characters (keep basic punctuations)
    text = re.sub(r'-{2,}', '-', text)              # Replace multiple hyphens with a single hyphen
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Content'] = df['Content'].apply(cleaned_content)

print(df)

keywords_dict =  {
  "Career Start": [
    "Co-founded Binance in 2017",
    "Saw opportunity in cryptocurrency and blockchain",
    "Led business, investments, and marketing",
    "Pivoted from traditional finance to crypto innovations"
  ],
  "Current Role": [
    "Co-founder of Binance Labs",
    "Head of brand strategy",
    "Oversees incubator and venture arm",
    "Innovates in blockchain technology and investments"
  ],
  "Previous Roles": [
    "Vice President at Yixia Technology",
    "Co-founder of OKCoin",
    "TV Anchor",
    "Assistant Psychotherapist",
    "Experience in media and psychological counseling"
  ],
  "Early Life": [
    "Humble beginnings in small Chinese province",
    "Economic barriers and limited higher education",
    "Encountered Bitcoin in 2013",
    "Struggled with financial constraints during youth"
  ],
  "Philosophy": [
    "Belief in financial freedom",
    "Focus on user-centered model",
    "Passion for wealth distribution",
    "Commitment to decentralization and transparency"
  ],
  "Biggest Challenge": [
    "China’s 2017 cryptocurrency exchange ban",
    "Transitioned from Chinese market to global market",
    "Adapting to new cultures and languages",
    "Navigating regulatory challenges in multiple countries"
  ],
  "Learning Moments": [
    "Helping users recover lost cryptocurrencies",
    "Facing industry criticism for intervention",
    "Valuing user feedback and adaptation",
    "Improving product security and user trust"
  ],
  "Influential Figures": [
    "CZ, Binance CEO",
    "Received constructive feedback",
    "Grew through leadership guidance",
    "Inspired by industry pioneers and mentors"
  ],
  "Gender Diversity in Tech": [
    "Low female founder percentage",
    "Encouraging women to pursue leadership",
    "Supporting women in technology and innovation",
    "Advocating for gender equity in tech roles"
  ],
  "Supportive Measures": [
    "Encouraging gender diversity",
    "Creating inclusive educational environments",
    "Promoting female leadership at Binance",
    "Supporting women in tech initiatives and conferences"
  ],
  "Advice for Women Founders": [
    "Rise to challenges",
    "Embrace education and opportunities",
    "Challenge gender stereotypes",
    "Network and build supportive communities"
  ],
  "Entrepreneurship Traits": [
    "Lifelong learning",
    "Ambition and execution",
    "Perseverance through uncertainty",
    "Innovative thinking and adaptability"
  ],
  "Career Advice": [
    "Gain diverse experience",
    "Develop vision and execution",
    "Consider internal entrepreneurship at Binance",
    "Build resilience and adaptability in your career"
  ],
  "Lessons Learned": [
    "Accept outcomes gracefully",
    "Align with stakeholders",
    "Embrace failure as growth",
    "Learn from setbacks and iterate quickly"
  ],
  "Impactful Actions": [
    "Reshaping the crypto industry",
    "Reducing transaction fees",
    "Building customer service systems",
    "Expanding global access to digital assets"
  ],
  "Philanthropic Efforts": [
    "Created Binance Charity",
    "Donated over $30 million",
    "Initiatives like Lunch for Kids and Web3 Scholarships",
    "Supporting global disaster relief and educational programs"
  ],
  "Future Vision": [
    "Mainstream adoption of cryptocurrencies",
    "Improving financial inclusion",
    "Promoting global economic fairness",
    "Advancing blockchain technology for societal benefits"
  ],
  "Inspirational Figures": [
    "Elon Musk",
    "Jeff Bezos",
    "Sheryl Sandberg",
    "Lady Gaga",
    "Angelina Jolie",
    "Oprah Winfrey",
    "Malala Yousafzai"
  ]
}


print(df)

def get_keywords(text):
    keywords = []

    for topics, sub_topics in keywords_dict.items():
        if any(sub.lower() in text.lower() for sub in sub_topics):
            keywords.append(topics)
    return ', '.join(keywords)


df['Topic'] = df['Content'].apply(get_keywords)
df['Topic'] = df['Topic'].replace('', 'He Yi')

print(df)   

df.to_csv('heyi_women_development.txt', index=False, sep='\t')
print("Successfully Scraped the Data!")








