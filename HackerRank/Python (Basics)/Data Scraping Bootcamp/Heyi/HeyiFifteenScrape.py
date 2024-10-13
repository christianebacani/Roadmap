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
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--blink-settings=imagesEnabled=false')

    services = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')
    driver = webdriver.Edge(service=services, options=options)
    return driver

driver = web_driver()
driver.get('https://blockchain.news/news/he-yi-discusses-binances-regulatory-strategy-amid-actions-against-binance-and-zhao-changpen')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="post"]'))
)

containers = driver.find_elements(By.XPATH, '//div[@class="post"]')
all_data = []

for container in containers:
    try:
        all_data.append(container.text)
    except Exception as e:
        print(f"Error : {e}")

strings = '\n\n'.join(all_data)
sentences = strings.split('\n')
df = pd.DataFrame(sentences, columns=['Content'])

# Drop empty strings and duplicates
df = df[df['Content'].str.strip() != '']
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df.to_csv('heyi_binance_regulatory_strategy.csv', index=False)
driver.quit()
print("Successfully Extracted the Data from the Website!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_binance_regulatory_strategy.csv'

df = pd.read_csv(csv_filepath)


df = df.iloc[:12].reset_index(drop=True)


keywords_dict =  {
    "Compliance Power Moves": [
        "KYC (Know Your Customer)",
        "EDD (Enhanced Due Diligence)",
        "WCK (Washing Control KYC)",
        "POA (Proof of Address)",
        "Binance's Global Compliance Strategy",
        "U.S. Department of Justice Inquiry",
        "SEC Charges",
        "Stringent Compliance Measures",
        "Regulatory Scrutiny"
    ],
    "Market Shake-Ups": [
        "Binance's Exit from the Russian Market",
        "CommEX Acquisition",
        "Strategic Market Exit",
        "Operational Transition",
        "Global Market Impact",
        "Russian Market Dynamics"
    ],
    "Legal Drama Unfolded": [
        "U.S. Sanctions on Russia",
        "DOJ and SEC Investigations",
        "Russian Access Violation",
        "Ongoing SEC Charges",
        "Historical DOJ-IRS Probe",
        "Legal Battles",
        "Regulatory Challenges"
    ],
    "Strategic Survival Tactics": [
        "He Yi's Public Letter",
        "Internal Efficiency Enhancements",
        "Logical Decision-Making",
        "Future Compliance Plans",
        "Response to Regulatory Pressures",
        "Strategic Adjustments",
        "Leadership Communication"
    ],
    "Global Compliance Trends": [
        "International Regulatory Compliance",
        "Global Sanctions Impact",
        "Compliance Best Practices",
        "Regulatory Strategy Shifts",
        "Market Adaptations",
        "Cross-Border Compliance Challenges"
    ]
}


def generate_keywords(text):
    keywords = []

    for key, values in keywords_dict.items():
        if any(word.lower() in text.lower() for word in values):
            keywords.append(key)
    return ', '.join(keywords)

df['Topic'] = df['Content'].apply(generate_keywords)
df['Topic'] = df['Topic'].replace('', 'He Yi`s Strategic Compliance Masterplan')

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

df.to_csv('heyi_binance_regulatory_strategy.txt', index=False, sep='\t')
print("Successfully Scraped!")






