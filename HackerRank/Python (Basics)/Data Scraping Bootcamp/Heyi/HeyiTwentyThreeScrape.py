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
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--blink-settings=imageEnabled=false')

    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')

    driver = webdriver.Edge(service=service, options=options)

    return driver

driver = web_driver()
driver.get('https://u.today/binance-cofounder-issues-scam-warning-to-crypto-community?utm_source=CryptoNews&utm_medium=app')

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="article__content"]'))
)

containers = driver.find_elements(By.XPATH, '//div[@class="article__content"]')

all_data = []

for container in containers:
    try:
        all_data.append(container.text)
    except Exception as e:
        print(f"Error Code : {e}")

strings = '\n\n'.join(all_data)
sentences = strings.split('\n')

df = pd.DataFrame(sentences, columns=['Content'])

df = df[df['Content'].str.strip() != '']

df.to_csv('heyi_scam_warning.csv', index=False)
print("Successfully Converted to CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_scam_warning.csv'

df = pd.read_csv(csv_filepath)

index_excluded = [1, 8, 9, 10, 11]

mask = ~df.index.isin(index_excluded)

filtered_df = df[mask].reset_index(drop=True)

print(filtered_df)

def cleaned_content(text):
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = text.strip()

    return text

filtered_df['Content'] = filtered_df['Content'].apply(cleaned_content)

df = filtered_df
print(df)

keywords_dict = {
    "Telegram Scam Alerts": ["Telegram", "YiHe", "warning", "scam", "community", "username", "fake", "alert"],
    "Binance Power Moves": ["BinanceLabs", "investment", "incubator", "projects", "startups", "program", "mentor"],
    "Stay Vigilant! Security Tips": ["caution", "fraud", "awareness", "protect", "alert", "scam", "message", "users"],
    "Token Listing Secrets Unlocked": ["listings", "process", "details", "token", "projects", "quietly", "application", "criteria"],
    "Blockchain Revolution": ["BNBChain", "blockchain", "ventures", "sponsor", "crypto", "firms", "technology"],
    "Incubator Game-Changers": ["incubation", "founders", "network", "sessions", "mentoring", "chats", "apply", "startups"],
    "Venture Capital Titans": ["investor", "VC", "sponsor", "firms", "early-stage", "funding", "investment", "capital"],
    "Social Media Risks Exposed": ["Telegram", "identity", "scam", "name", "fake", "social", "fraud", "users"],
    "Leadership Disruptors": ["cofounder", "CEO", "YiHe", "RichardTeng", "leadership", "venture", "Binance", "CZ"],
    "Crypto Trends Redefined": ["crypto", "Binance", "BNB", "blockchain", "projects", "ventures", "exchange", "innovation"]
}

def generate_keywords(text):
    keywords = []
    text_lower = text.lower()

    for topics, sub_topics in keywords_dict.items():
        if any(word.lower() in text_lower for word in sub_topics):
            keywords.append(topics)

    return ', '.join(keywords)

df['Topic'] = df['Content'].apply(generate_keywords)

df["Topic"] = df['Topic'].replace('', 'He Yi')

print(df)

df.to_csv('heyi_scam_warning.txt', index=False, sep='\t')
print("Successfully Scraped!")
