import requests
import pandas as pd
from bs4 import BeautifulSoup

link = 'https://crypto.news/exclusive-interview-with-he-yi-co-founder-and-cmo-of-binance/'

response = requests.get(link) 

if response.status_code == 200:
    html_content = response.text 
    soup = BeautifulSoup(html_content, 'html.parser') 
    print("\nYou're allowed to scrape!") 
else:
    print("\nYou're not allowed to scrape!") 

# HTML Content
print(soup.prettify()) 
# Title of HTML Content
print(soup.title.string) 

text_data = soup.get_text(separator='\n', strip=True)

sentences = text_data.split('\n')
print(sentences) 

data = ['. '.join(sentences[i:i+5]) for i in range(0, len(sentences), 5)]
print(data)

df = pd.DataFrame(data, columns=['Content'])
print(df)

keywords = [
    "Interview", "He Yi", "Binance", "Co-Founder", "CMO", "Binance Open Platform", 
    "Decentralized", "Infrastructure", "Binance Chain", "Binance DEX", 
    "Crypto Exchange", "Decentralization", "Freedom of Money", "Broker Program", 
    "Binance Cloud", "API", "Liquidity", "Market Depth", "Trading Services", 
    "Digital Asset Exchanges", "P2P Trading", "Token Launch", "Global Adoption", 
    "Steemit", "Hard Fork", "Customer Deposits", "Regular Upgrades", "Binance P2P"
]

def extract_keywords(text):
    text = text.lower()
    found_keywords = [keyword for keyword in keywords if keyword.lower() in text]
    return ', '.join(found_keywords).capitalize() if found_keywords else 'Crypto, Binance, HeYi Interview'

df['Topic'] = df['Content'].apply(extract_keywords)

print(df)

df.to_csv('heyi_interview.csv', index=False)
print(df)

filepath = 'D:\\Visual Studio Codes\\heyi_interview.csv'
df = pd.read_csv(filepath)
print(df)

df.dropna(how='all', inplace=True) 

print("Columns:")
print(df.columns)

file = filepath.replace('.csv', '.txt')


with open(file, 'w', encoding='utf-8') as txt:
    txt.write(f"Content\t\t\t\tTopic\n")

    for i, row in df.iterrows():
        content = row.get('Content', 'NULL')
        topic = row.get('Topic', 'NULL')

        txt.write(f"{content.strip()}\t\t{topic.strip()}\n")

print("\nSuccessfully Scraped the Data from the Website!")
