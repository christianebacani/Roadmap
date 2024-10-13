import re 
import pandas as pd
from bs4 import BeautifulSoup
import requests

link = 'https://wublock.substack.com/p/summary-of-binance-co-founder-heyis'

r = requests.get(link)

if r.status_code == 200:
    html_content =  r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup)

else:
    print("You`re not allowed to scrape!")

print(soup.prettify())

print(soup.title.string)

text = soup.get_text(separator='\n', strip=True)
print(text)

split_text = text.split('\n')
print(split_text)

combined_text = [' '.join(split_text[i:i+2]) for i in range(0, len(split_text), 2)]
print(combined_text)

df = pd.DataFrame(combined_text, columns=['Content'])
print(df)


df.to_csv('heyi_summary.csv', index=False)
print("Converted to CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\Practice Code Folders\\CSV File Data\\heyi_summary.csv'

df = pd.read_csv(csv_filepath)
print(df)

summary = df.iloc[15:46]
print(summary)

df = pd.DataFrame(summary, columns=['Content'])
print(df)

def cleaned_text(text):
    text = re.sub(r'["\'`]', '', text)              # Remove quotes (fixed pattern)
    text = re.sub(r'[""""\'`]', '', text)           # Remove quotes
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)             # Replace multiple question marks with one
    text = re.sub(r'-{2,}', '-', text)              # Replace multiple hyphens with a single hyphen
    text = re.sub(r'\(.*?\)', '', text)             # Remove text inside parentheses
    text = re.sub(r'[^\x00-\x7F]+', '', text)       # Remove non-ASCII characters
    text = re.sub(r'\n+', ' ', text)                # Replace newlines with space
    text = re.sub(r'\t+', ' ', text)                # Replace tabs with space
    text = re.sub(r'^[^\w]+|[^\w]+$', '', text)     # Remove punctuation from start and end
    text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text) # Keep only allowed characters
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Content'] = df['Content'].apply(cleaned_text)
print(df)


keywords = [
    "absolute security", "vigilant", "exchanges", "asset security management", "hardware wallets", 
    "e-commerce wallets", "Binance", "security", "investment", "risk control standards", 
    "dual risk control", "wash trading", "price fluctuations", "big data", "manual confirmation", 
    "plugins", "account sharing", "user behavior logs", "suspicious links", "phishing apps", 
    "rumors", "trust", "industry", "high FDV", "low-circulation projects", "token distribution", 
    "blockchain industry", "niche", "mainstream markets", "VR", "3D printing", "Tesla", 
    "decentralized", "efficient", "financial system", "trading", "asset management", "inflation prevention", 
    "business models", "mass adoption", "gaming", "social networking", "anti-VC wave", "memecoins", 
    "quality assets", "VCs", "high valuations", "airdrops", "user demand", "market makers", 
    "sustainable growth", "project parties", "investors", "research", "voting", "foot", 
    "excellent projects", "blockchain assets", "entrepreneurs", "airdrops", "trading platforms", 
    "self-improvement", "fitness", "health", "self-awareness", "Mindset", "psychology", 
    "success", "rebuilding", "growth", "strong organization", "Duan Yongping", "Subor", 
    "BBK", "vivo", "OPPO", "NetEase", "Pinduoduo", "high-potential talents", "corporate culture", 
    "Binance", "Launchpool", "MegaDrop", "Launchpad", "regulatory issues", "airdrop", "real users", 
    "Web3 wallet", "KYC", "bot studios", "user feedback", "short-term increases", "prices drop", 
    "low circulation", "deflationary models", "quality projects", "long-term development", 
    "potential for success", "real users", "benefits", "project selection", "market feedback", 
    "delisting standards", "zombie coins", "liquidity", "negative news", "high-risk tokens", 
    "bull market", "on-chain incidents", "hacker events", "accurate decisions", "shell projects", 
    "market value", "Coinbase", "BNB", "token", "burn mechanisms", "BNB Chain", "L2", "L1 ecosystems", 
    "TON", "Web3 users", "blockchain technology", "entrepreneurs", "BNBChain", "short-term price fluctuations", 
    "long-term efforts", "team goals", "collective efforts", "AI", "labor relations", "distribution of benefits", 
    "productivity transformation", "trading platforms", "multilingual environments", "translation costs", 
    "productivity improvement", "design", "marketing", "OpenAI", "chatbots", "plans", "videos", 
    "computing power", "NVIDIA", "chips", "technological advancements", "energy", "data", "wars", 
    "political struggles", "AI development", "privacy", "Greenfield product", "sector selection", 
    "leadership team", "organizational issues", "management", "HR", "emails", "life tidbits", 
    "exercise", "family time"
]

def search_keywords(text):
    text = text.lower()
    founded_keywords = [word for word in keywords if word.lower() in text]
    return ', '.join(founded_keywords) if founded_keywords else 'Summary of Binance Co-Founde Heyi'

df['Topic'] = df['Content'].apply(search_keywords)

print(df)

df.to_csv('heyi_summary_keywords.csv', index=False)
print("Converted and Added a Keywords in CSV File!")

filepath = 'D:\\Visual Studio Codes\\heyi_summary_keywords.csv'

df = pd.read_csv(filepath)
print(df)

df.dropna(how='all', inplace=True)

text_filepath = filepath.replace('.csv', '.txt')

with open(text_filepath, 'w', encoding='utf-8', newline='\n') as txt:
    txt.write(f"Content\tTopic\n")

    for i,row in df.iterrows():
        contents = row.get('Content', 'No Content')
        topics = row.get('Topic', 'No Topic')

        txt.write(f"{contents}.\t\t{topics}\n")

print("Converted to Text File Format!")
