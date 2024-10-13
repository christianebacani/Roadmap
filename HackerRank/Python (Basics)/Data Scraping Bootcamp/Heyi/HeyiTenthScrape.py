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
    url = 'https://forkast.news/binance-regulation/'

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

        with open('heyi_forkfast_binance_regulations.txt', 'w', encoding='utf-8') as text:
            text.write(text_content)
            print("Successfully Converted to Text File Format!")

asyncio.run(get_text_content())

text_filepath = 'D:\\Visual Studio Codes\\heyi_forkfast_binance_regulations.txt'

with open(text_filepath, 'r', encoding='utf-8') as text:
    data = text.read()

sentences = data.split('\n')

combined_sentences = [' '.join(sentences[i:i+2]) for i in range(0, len(sentences), 2)]

df = pd.DataFrame(combined_sentences, columns=['Content'])
print(df)

def clean_content(text):
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'-{2,}', '-', text)              # Replace multiple hyphens with a single hyphen
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Content'] = df['Content'].apply(clean_content)
print(df)

df.to_csv('heyi_forkfast_binance_regulations.csv', index=False)
print("Successfully Converted to CSV File Format!")

df = pd.read_csv('D:\\Visual Studio Codes\\heyi_forkfast_binance_regulations.csv')
print(df)

df = df.iloc[10:67].reset_index(drop=True)
print(df)
print("\nRemoved Unnecessary Content!")

keywords_dict = {
    "Crypto Exchange Giants": [
        "Global operations",
        "Headquarters establishment",
        "Compliance and regulation",
        "Cryptocurrency exchange",
        "Trading volume",
        "Cryptocurrency market dominance",
        "Physical headquarters",
        "KYC regulations",
        "Money laundering prevention",
        "Terrorist financing prevention",
        "Global expansion",
        "Geographical units",
        "Company structure",
        "Corporate strategy",
        "Virtual asset services"
    ],
    "Regulatory Trends": [
        "Know-your-customer (KYC) practices",
        "Anti-money laundering (AML)",
        "Terrorist financing",
        "Global compliance efforts",
        "Regulatory oversight",
        "Regulation adaptation",
        "Identity verification",
        "Account status changes",
        "Regulatory challenges",
        "Cross-country capital transfers",
        "Compliance teams",
        "Regulatory scrutiny"
    ],
    "Crypto Ecosystem": [
        "Cryptocurrency exchange services",
        "Capital flight prevention",
        "Privacy concerns",
        "Market size and share",
        "Fiat integration",
        "Mainstream adoption",
        "Decentralized finance",
        "Digital tokens",
        "Market dynamics",
        "Virtual currencies",
        "Innovations in crypto"
    ],
    "Industry Movers": [
        "Yi He",
        "Changpeng Zhao",
        "Mark McGinness",
        "Kunchou Tsai",
        "Kevin Cheng",
        "Charlotte Wu",
        "Timmy Shen",
        "Ningwei Qin",
        "Tom Zuo"
    ],
    "Global Hotspots": [
        "China",
        "United Kingdom",
        "Japan",
        "United States",
        "Dubai",
        "Taiwan",
        "Cayman Islands",
        "Singapore"
    ],
    "Compliance Challenges": [
        "Regulatory hurdles",
        "Compliance issues",
        "Account restrictions",
        "Legal risks",
        "Hacking risks",
        "Operational challenges",
        "Capital transfer regulations",
        "Licensing and registration",
        "Regulatory scrutiny"
    ],
    "Strategic Moves": [
        "Global compliance strategy",
        "Headquarters establishment",
        "Hiring for compliance",
        "Scaling operations",
        "Regulatory partnerships",
        "Integration with traditional finance",
        "Onshore licensing",
        "Expanding compliance teams",
        "Strategic goals for compliance"
    ],
    "Regulatory Actions & Reactions": [
        "Regulation enforcement",
        "Government crackdowns",
        "Compliance orders",
        "Investigations",
        "Licensing issues",
        "Regulatory rebukes",
        "Fines and penalties"
    ],
    "Tech & Security Innovations": [
        "Identity verification technologies",
        "Two-factor authentication",
        "Virtual private networks (VPNs)",
        "Corporate structure",
        "Cybersecurity",
        "Hacking incidents",
        "Online wallet security",
        "Integration with payment services"
    ],
    "Legal & Risk Management": [
        "Legal risks of international operations",
        "Lawsuits and legal actions",
        "Regulatory frameworks",
        "Legal entity challenges",
        "International legal disputes",
        "Legal compliance in different jurisdictions"
    ],
    "Future Outlook": [
        "Industry growth",
        "Regulatory developments",
        "Market expansion",
        "User base growth",
        "Regulatory adaptations",
        "Future compliance strategies"
    ]
}




def get_keywords(text):
    keywords = []

    for categories, sub_categories in keywords_dict.items():
        if any(sub.lower() in text.lower() for sub in sub_categories):
            keywords.append(categories)
   
    return ', '.join(keywords)


df['Keyword'] = df['Content'].apply(get_keywords)

df['Keyword'] = df['Keyword'].replace('', 'He Yi')

print(df)

df.to_csv('heyi_forkfast_binance_regulations.csv', index=False)
print("\nSuccessfully Converted to CSV File with Content, and Keyword Column!")


text_file = 'D:\\Visual Studio Codes\\heyi_forkfast_binance_regulations.csv'.replace('.csv', '.txt')

with open(text_file, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"Row\tContent\tKeyword\n")

    for i,row in df.iterrows():
        contents = row.get('Content', 'No Content')
        keywords = row.get('Keyword', 'No Keyword')
        text.write(f"{i + 1}\t{contents}\t{keywords}\n")

print("\nSuccessfully Scraped!")
