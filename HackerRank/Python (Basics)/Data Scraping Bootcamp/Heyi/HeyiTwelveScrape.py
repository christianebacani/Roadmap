from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service  # This imports the Service class
import pandas as pd
import re



def web_driver():
    options = webdriver.EdgeOptions()

    options.add_argument('--verbose')
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')
    driver = webdriver.Edge(service=service, options=options)

    return driver

driver = web_driver()
driver.get('https://cointelegraph.com/news/binance-co-founder-yi-he-says-forget-gender-and-focus-on-mindset-to-make-in-web3')

WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="post-content relative"]'))
)

containers = driver.find_elements(By.XPATH, '//div[@class="post-content relative"]')

all_paragraphs = []

for container in containers:
    elements = container.find_elements(By.XPATH, './/p | .//blockquote')

    for element in elements:
        all_paragraphs.append(element.text)

content = '\n\n'.join(all_paragraphs)
sentences = content.split('\n')
df = pd.DataFrame(sentences, columns=['Content'])

df = df[df['Content'].str.strip() != '']

df = df.drop_duplicates()

df.to_csv('heyi_cointelegraph.csv', index=False)

driver.quit()

print("Successfully Saved into a CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_cointelegraph.csv'

df = pd.read_csv(csv_filepath)

def cleaned_content(text):
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)             # Replace multiple question marks with one
    text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text) # Remove special characters (keep basic punctuations)
    text = re.sub(r'-{2,}', '-', text)              # Replace multiple hyphens with a single hyphens
    text = re.sub(r'[^\x00-\x7F]+', '', text)       # Remove non-ASCII characters
    text = re.sub(r'\n+', ' ', text)                # Replace newlines with space
    text = re.sub(r'\t+', ' ', text)                # Replace tabs with space
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Content'] = df['Content'].apply(cleaned_content)
print(df)

keywords_dict  = {
    "Crypto Revolution": [
        "crypto", "decentralized technologies", "fintech", "digital interactions",
        "blockchain", "BTC", "Bitcoin", "decentralized finance", "Binance", "Web3"
    ],
    "Women Empowerment in Tech": [
        "women", "financial freedom", "gender bias", "women in crypto",
        "women founders", "female", "international women's day", "female leaders"
    ],
    "Tech Leadership Strategies": [
        "mindset", "growth management", "decision-making", "assertive",
        "ownership", "problem solver", "business leader", "CEO", "education", "community building"
    ],
    "Binance Innovations": [
        "Binance", "Yi He", "Changpeng Zhao", "CZ", "Binance Charity", "Web3 scholarships"
    ],
    "Decentralized Finance (DeFi)": [
        "decentralized finance", "DeFi", "smart contracts", "blockchain technology", "crypto assets"
    ],
    "Blockchain Trailblazers": [
        "blockchain", "distributed ledger", "smart contracts", "cryptographic security", "blockchain innovation"
    ],
    "Fintech Disruption": [
        "fintech", "financial technology", "digital payments", "blockchain finance", "fintech startups"
    ],
    "Diversity in Tech": [
        "diversity", "inclusion", "tech diversity", "gender equality", "underrepresented groups"
    ],
    "Crypto Industry Trends": [
        "cryptocurrency trends", "market analysis", "investment in crypto", "blockchain trends", "crypto regulations"
    ],
    "Web3 Development": [
        "Web3", "decentralized applications (dApps)", "blockchain interoperability", "smart contracts", "Web3 protocols"
    ],
    "Blockchain for Social Impact": [
        "social impact", "blockchain for good", "impact investing", "philanthropy", "blockchain initiatives"
    ],
    "Next-Gen Finance": [
        "next-gen finance", "future of finance", "fintech evolution", "digital assets", "innovative financial models"
    ],
    "Crypto Security & Compliance": [
        "crypto security", "compliance", "regulatory framework", "cryptographic protocols", "data protection"
    ],
    "Women Leading Crypto Startups": [
        "women leaders", "crypto startups", "female entrepreneurs", "startup culture", "tech startups"
    ],
    "Global Crypto Adoption": [
        "global adoption", "crypto acceptance", "international markets", "crypto regulations", "cross-border transactions"
    ],
    "Fintech Innovations & Trends": [
        "fintech innovations", "trending fintech", "financial technology trends", "payment systems", "fintech solutions"
    ],
    "Tech Industry Disruptors": [
        "tech disruptors", "innovation leaders", "industry disruptors", "tech revolution", "emerging technologies"
    ]
}

def generate_keywords(text):
    tags = []

    for categories, sub_categories in keywords_dict.items():
        if any(sub.lower() in text.lower() for sub in sub_categories):
            tags.append(categories)
    return ', '.join(tags)

df['Topic'] = df['Content'].apply(generate_keywords)

df['Topic'] = df['Topic'].replace('', 'He Yi/Yi He')

df.to_csv('heyi_cointelegraph.txt', index=False, sep='\t')
print("Successfully Scraped!")
