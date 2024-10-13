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
    options.add_argument('--windows-size=1920,1200')
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')

    driver = webdriver.Edge(service=service, options=options)
    return driver

driver = web_driver()
driver.get('https://coingape.com/breaking-reports-on-binance-exchange-under-attack/')

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="col-lg-12 col-content"]'))
)

containers = driver.find_elements(By.XPATH, '//div[@class="col-lg-12 col-content"]')

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

df.to_csv('heyi_binance_exchange.csv', index=False)
print("Successfully Converted into CSV File Format!")
driver.quit()

csv_filepath = 'D:\\Visual Studio Codes\\heyi_binance_exchange.csv'

df = pd.read_csv(csv_filepath)

index_include = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]
df = df.iloc[index_include].reset_index(drop=True)

print(df)

def cleaned_content(text):
    text = re.sub('\s+', ' ', text)
    text = re.sub('\t+', ' ', text)
    text = re.sub('\n+', ' ', text)
    text = text.strip()

    return text

df['Content'] = df['Content'].apply(cleaned_content)
print(df)


keywords_dict = {
    "Exchange Attack Details": ["hack", "DDoS", "breach", "disruption", "lag", "interruption", "server-down"],
    "Official Binance Response": ["alert", "tweet", "confirmation", "probe", "reassure", "statement", "notify"],
    "Phishing Concerns Raised": ["phishing", "scam", "mailer", "survey", "questionnaire", "suspect", "hoax"],
    "User Experience Impact": ["lag", "issue", "disruption", "concern", "delay", "report", "funds", "inconvenience"],
    "CEO Public Statement": ["tweet", "update", "SAFU", "response", "announcement", "confirmation", "comment"],
    "Competitor Activity Suspicion": ["attack", "rivalry", "competition", "target", "opposition", "sabotage", "conflict"],
    "Security Measures": ["mitigation", "action", "safeguard", "countermeasure", "protection", "defense", "precaution"],
    "Customer Trust Assurance": ["trust", "confidence", "security", "safety", "reliability", "reassurance", "stability"],
    "Technical Investigation": ["probe", "analysis", "inspection", "diagnosis", "debug", "evaluation", "examination"],
    "Server Performance Issue": ["latency", "downtime", "slowdown", "disruption", "outage", "delay", "failure"],
    "Customer Communication": ["notification", "email", "mailer", "update", "survey", "message", "response"],
    "System Health Status": ["fine", "stable", "secured", "normal", "protected", "functional", "operational"],
    "Exchange Reputation Management": ["credibility", "reputation", "trust", "loyalty", "publicity", "goodwill", "integrity"],
    "Market Reaction": ["shock", "concern", "volatility", "uncertainty", "response", "impact", "fluctuation"],
    "Contract Page Glitch": ["lag", "issue", "error", "glitch", "failure", "delay", "slowdown"]
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

df.to_csv('heyi_binance_exchange.txt', index=False, sep='\t')
print("Successfully Scraped!")



    



