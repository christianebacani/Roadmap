from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service  # This imports the Service class
import pandas as pd
import re

def web_driver():
    options = webdriver.EdgeOptions()

    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--blink-settings=imagesEnabled=false')

    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')
    driver = webdriver.Edge(service=service, options=options)
    return driver

driver = web_driver()
driver.get("https://medium.com/@btok_official/btok-binance-ama-he-yi-an-introduction-to-binance-futures-5d69a8e0a171")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="ab cb"]'))
)

containers = driver.find_elements(By.XPATH, './/div[@class="ab cb"]')

all_data = []

for container in containers:
    paragraphs = container.find_elements(By.XPATH, './/p')
    for paragraph in paragraphs:
        try:
            all_data.append(paragraph.text)
        except Exception as e:
            print(f"Error: {e}")




strings = '\n\n'.join(all_data)
sentences = strings.split('\n')

df = pd.DataFrame(sentences, columns=['Content'])

df = df[df['Content'].str.strip() != '']

df.drop_duplicates(inplace=True)


df.to_csv('heyi_intro_binance_futures.csv', index=False)

driver.quit()
print("Successfully Scraped the Data")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_intro_binance_futures.csv'

df = pd.read_csv(csv_filepath)

df = df.iloc[2:58].reset_index(drop=True)

keywords_dict = {
    "Host": [
        "Jenny Yang",
        "crypto visionary leader",
        "founder of Star Finance",
        "fintech and Web3 influencer",
        "blockchain strategist",
        "disruptive fintech voice"
    ],
    "Guest": [
        "YiYi",
        "Web3 marketing disruptor",
        "co-founder of Coin Security",
        "CMO and blockchain pioneer",
        "crypto brand strategist",
        "digital asset evangelist",
        "He Yi"
    ],
    "Crypto Security": [
        "market-leading exchange",
        "smart contract and derivatives leader",
        "Web3 liquidity engine",
        "digital asset protection innovator",
        "AI-powered trading",
        "next-gen crypto infrastructure",
        "risk mitigation solutions"
    ],
    "Smart Contracts": [
        "high-speed contract trading",
        "advanced derivatives marketplace",
        "DeFi-powered hedging",
        "AI-driven smart contracts",
        "options market disruptor",
        "decentralized trading tools",
        "blockchain-based automation"
    ],
    "Risk Management": [
        "AI-enhanced contract trading",
        "user asset protection systems",
        "automated margin strategies",
        "institutional-grade insurance funds",
        "crypto volatility stabilization",
        "blockchain risk intelligence",
        "fraud prevention technology"
    ],
    "Market Innovations": [
        "digital asset derivatives innovator",
        "contract and options market leader",
        "DeFi tokenized assets",
        "next-gen financial products",
        "global fintech competition",
        "AI-driven platform stability",
        "blockchain-based financial tools"
    ],
    "Global Trends": [
        "decentralized exchange disruption",
        "cutting-edge Web3 platforms",
        "cross-border crypto globalization",
        "blockchain innovation ecosystem",
        "next-gen token economies",
        "DeFi market transformation",
        "bull market growth potential"
    ],
    "Financial Products": [
        "multi-layered smart contracts",
        "advanced crypto options trading",
        "DeFi derivatives markets",
        "AI-driven risk mitigation",
        "tokenized financial instruments",
        "blockchain-powered tools",
        "decentralized insurance systems"
    ],
    "Digital Tech": [
        "live streaming evolution",
        "digital media breakthroughs",
        "integration strategies",
        "AI-powered user experience",
        "content creation disruption",
        "next-gen digital media",
        "platform scalability"
    ],
    "Market Makers": [
        "global crypto liquidity engines",
        "institutional API-driven trading",
        "specialized high-frequency trading",
        "decentralized liquidity protocols",
        "key account partnerships",
        "real-time institutional trading",
        "crypto liquidity disruptors"
    ],
    "Competitors Landscape": [
        "Bitmex trading dominance",
        "OKEX fintech innovations",
        "Huobi global expansion strategy",
        "Bibox AI trading technology",
        "Matcha platform disruptor",
        "B Network challenger model",
        "P Network competitive dynamics",
        "emerging blockchain challengers"
    ]
}



def generate_keywords(text):
    keywords = []

    for key, values in keywords_dict.items():
        if any(value for value in values if value.lower() in text.lower()):
                keywords.append(key)
    return ', '.join(keywords)

df['Topic'] = df['Content'].apply(generate_keywords)

df['Topic'] = df['Topic'].replace('', 'He Yi`s Crypto Revolution')

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

df.to_csv('heyi_intro_binance_futures_keywords.txt', index=False, sep='\t')
print("Successfully Scraped!")
