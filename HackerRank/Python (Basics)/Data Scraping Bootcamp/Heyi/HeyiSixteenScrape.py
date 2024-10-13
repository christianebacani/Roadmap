from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import pandas as pd
import re


def web_driver():
    options = webdriver.EdgeOptions()

    options.add_argument('--verbose')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--dev-disable-shm-usage')
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--blink-settings=imageEnabled=false')

    services = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')
    driver = webdriver.Edge(service=services, options=options)

    return driver

driver = web_driver()
driver.get('https://blockchain.news/news/Binance-Cofounder-He-Yi-Clarifies-Token-Listing-Criteria-and-Addresses-Market-Volatility-Concerns-78c640fe-f0e8-4f3c-889c-61ae370faaf3')

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="post"]'))
)

containers = driver.find_elements(By.XPATH, '//div[@class="post"]')

all_data = []

for element in containers:
    try:
        all_data.append(element.text)
    except Exception as e:
        print(f"Error : {e}")

driver.quit()

strings = '\n\n'.join(all_data)

sentences = strings.split('\n')

df = pd.DataFrame(sentences, columns=['Content'])

df = df[df['Content'].str.strip() != '']
df.drop_duplicates(inplace=True)

df.to_csv('heyi_binance_token_listing.csv', index=False)
print("Successfully Converted to CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_binance_token_listing.csv'

df = pd.read_csv(csv_filepath)

def cleaned_content(text):
    # Replace multiple newlines with a single space
    text = re.sub(r'\n+', ' ', text)
    
    # Replace multiple tabs with a single space
    text = re.sub(r'\t+', ' ', text)
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading and trailing spaces
    text = text.strip()
    
    # Ensure proper punctuation spacing
    text = re.sub(r'\.\s+', '. ', text)  # Ensure a space follows periods
    text = re.sub(r'\!\s+', '! ', text)  # Ensure a space follows exclamation marks
    text = re.sub(r'\?\s+', '? ', text)  # Ensure a space follows question marks

    return text

df['Content'] = df['Content'].apply(cleaned_content)

keywords_dict = {
    "Token Hype": ["criteria", "user demands", "decision process", "collaborative", "project owners"],
    "Market Frenzy": ["performance", "price fluctuations", "monitoring", "oversight", "multi-party custody"],
    "IEO Buzz": ["market capitalizations", "bull market", "investor investments", "valuation", "capital pursuit"],
    "Transparent Economy": ["transparency", "pricing approach", "capitalization", "user pricing", "risk mitigation"],
    "Blockchain Revolution": ["innovation", "decentralization", "smart contracts", "peer-to-peer", "consensus mechanisms"],
    "NFT Boom": ["digital assets", "ownership", "creators", "collectibles", "tokenization"],
    "Crypto Compliance": ["compliance", "AML", "KYC", "legal framework", "international standards"],
    "DeFi Revolution": ["yield farming", "liquidity pools", "governance tokens", "decentralized exchanges", "staking"],
    "AI Takeover": ["automation", "machine learning", "predictive analytics", "neural networks", "natural language processing"],
    "Metaverse Experience": ["virtual reality", "augmented reality", "digital identity", "immersive experience", "virtual worlds"],
    "Eco Energy": ["sustainability", "renewable resources", "carbon footprint", "clean energy", "environmental impact"],
    "Social Media Buzz": ["influencers", "hashtags", "viral content", "engagement", "community building"],
    "E-commerce Surge": ["online shopping", "user experience", "digital payments", "logistics", "customer retention"],
    "Cyber Defense": ["data protection", "encryption", "threat detection", "firewalls", "vulnerability management"],
    "Remote Revolution": ["telecommuting", "flexible schedules", "virtual collaboration", "digital nomads", "work-life balance"]
}


def generate_keywords(text):
    keywords = []

    for key, values in keywords_dict.items():
        if any(word.lower() in text.lower() for word in values):
            keywords.append(key)

    return ', '.join(keywords)

df['Topic'] = df['Content'].apply(generate_keywords)

df['Topic'] = df['Topic'].replace('', 'He Yi’s Binance Listing Insights')
df = df.iloc[:8].reset_index(drop=True)

df.to_csv('heyi_binance_token_listing.txt', index=False, sep='\t')
print("Successfully Scraped!")





