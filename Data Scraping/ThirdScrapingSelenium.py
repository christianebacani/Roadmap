# Import Libraries
from keybert import KeyBERT
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import pandas as pd
import re 

# Data Extraction Phase

# Functions for Customize Web Driver
def web_driver():
    options =  webdriver.EdgeOptions()
    
    options.add_argument('--verbose') # No Logs
    options.add_argument('--no-sandbox') # No Testing Env
    options.add_argument('--disable-gpu') # Disable GPU 
    options.add_argument('--window-settings=1920, 1200') # Window Setting
    options.add_argument('--disable-dev-shm-usage') # Disable memory constrainst

    # Define the path for the Web Driver
    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')

    # Return the value of Customized Web Driver
    driver = webdriver.Edge(service=service, options=options)
    
    return driver

driver = web_driver()
# URL
driver.get('https://newsletter.techworld-with-milan.com/p/how-to-become-an-expert-in-anything?utm_source=leadershipintech&utm_medium=referral&utm_campaign=how-to-become-an-expert-in-anything')

# Wait for the document to be fully loaded
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# Find the presence of the div element to be scraped
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="available-content"]'))
)


container = driver.find_elements(By.XPATH, '//div[@class="available-content"]')

data = []

# Scrape the data from the specified div element
for element in container:
    try:
        data.append(element.text) # Parse as a text for compatibility
    
    except Exception as e:
        print(f"Error Code : {e}")

driver.close()

# Data Structuring

# Combined the Data
sentences = '\n\n'.join(data)

# Separate into multiple rows
rows = sentences.split('\n')

# Define the DataFrame based on the rows
df = pd.DataFrame(rows, columns=['Content'])

# Remove empty rows
df = df[df['Content'].str.strip() != '']
print(df)

# Save as CSV File
df.to_csv('expert_anything_article.csv', index=False)
print("Converted into CSV Fie Format!")

# Data Cleaning Phase

# CSV File
csv_file = 'expert_anything_article.csv'

df = pd.read_csv(csv_file)

print(df)

# Include necessary rows
df = df.iloc[:76]
print(df)

# Remove unnecessary rows
index_exluded = [27, 28, 29, 32, 33, 34, 35, 36, 37]
mask = ~df.index.isin(index_exluded)

df = df[mask].reset_index(drop=True)

# Function to cleant the data
def cleaned_content(text):
    text = re.sub(r'[👉➡️📌✅✨🚀]+', '', text)
    text = re.sub(r'[,.!?]+$', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = text.strip()

    return text

df['Content'] = df['Content'].apply(cleaned_content)

print(df)

# Data Enrichment Phase

# Model for Generating Keywords
model = KeyBERT('distilbert-base-nli-mean-tokens')

# Function to Generate Keywords
def generate_keywords(text):
    keywords = [keyword for keyword, score in model.extract_keywords(text)]

    keywords_capitalize = [word.title() for word in keywords] # Capitalize every keywords

    return ', '.join(keywords_capitalize)

df['Keyword'] = df['Content'].apply(generate_keywords)

# Save the Enriched Data in the existing CSV
df.to_csv('expert_anything_article.csv', index=False)
print("Successfully Enriching the Data!")

# Data Integration Phase

# CSV File
csv_file = 'expert_anything_article.csv'

# Replace into Text File
text_file = csv_file.replace('.csv', '.txt')

# Rewrite the Text File based on the CSV File
with open(text_file, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"Content\t\t'Keyword'\n")

    for i, row in df.iterrows():
        content = row.get('Content', 'No Content')
        keyword = row.get('Keyword', 'No Keyword')

        text.write(f"{content}\t\t'{keyword}'\n")
print("Successfully Integrated into our Local Working Directory!")

# Automaticall Integrated into the Working Directory
