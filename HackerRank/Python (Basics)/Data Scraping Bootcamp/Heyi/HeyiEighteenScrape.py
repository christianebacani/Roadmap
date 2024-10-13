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
    options.add_argument('--window-size=1290,1200')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--blink-settings=imagesEnabled=false')

    services = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')

    driver = webdriver.Edge(service=services, options=options)

    return driver

driver = web_driver()
driver.get('https://coingape.com/binance-co-founder-announces-5-million-reward-for-reporting-insider-trading/')

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="postF"]'))
)

containers = driver.find_elements(By.XPATH, '//div[@class="postF"]')

all_data = []

for element in containers:
    try:
        all_data.append(element.text)
    except Exception as e:
        print(f"Error : {e}")



strings = '\n\n'.join(all_data)
sentences = strings.split('\n')

df = pd.DataFrame(sentences, columns=['Content'])

df = df[df['Content'].str.strip() != '']

df.to_csv('heyi_binance_trading_reward_announcement.csv', index=False)

driver.quit()


csv_filepath = 'D:\\Visual Studio Codes\\heyi_binance_trading_reward_announcement.csv'

df = pd.read_csv(csv_filepath)

df = df.iloc[1:17].reset_index(drop=True)
print(df)


def cleaned_content(text):
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\n+', ' ', text)

    text = text.strip()

    text = re.sub(r'\.\+', '. ', text)
    text = re.sub(r'\!\+', '! ', text)
    text = re.sub(r'\?\+', '? ', text)
    return text

df['Content'] = df['Content'].apply(cleaned_content)


keywords_dict = {
    "Ronin Token Crash": ["Ronin drop", "Binance listing", "20% loss", "info leak", "speculation rise"],
    "Project Cancel Warning": ["Yi He", "leak threat", "cancel risk", "internal alert", "tight measures"],
    "Insider Reward Program": ["$5M reward", "insider tip", "reporting bonus", "integrity focus", "verified info"],
    "Internal Firewall Boost": ["management boost", "firewall isolation", "listing group", "leak warning", "termination risk"],
    "External Partner Rules": ["partner check", "token model", "listing hold", "leak penalty", "process review"],
    "Technical Watchdog": ["trade monitor", "technical scan", "secure system", "user safety", "issue detect"],
    "Community Support": ["community backing", "transparency focus", "security promise", "ongoing efforts", "integrity push"],
    "Corruption Report Rewards": ["whistleblower bonus", "confidential report", "vulnerability tip", "corruption check", "safety first"],
    "Blacklist Corrupt Projects": ["blacklist rule", "employee ban", "fund ban", "corruption-free", "strict control"],
    "Background Checks Partnerships": ["funds review", "partner check", "background checks", "partnership trust", "offer scrutiny"]
}


def generate_keywords(text):
    keywords = []

    for topics, sub_categories in keywords_dict.items():
        if any(word.lower() in text.lower() for word in sub_categories):
            keywords.append(topics)
    
    return ', '.join(keywords)

df['Topic'] = df['Content'].apply(generate_keywords)

df['Topic'] = df['Topic'].replace('', 'He Yi')

print(df)

df.to_csv('heyi_binance_trading_reward_announcement.txt', index=False, sep='\t')
print("Successfully Scraped!")






