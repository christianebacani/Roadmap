import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def get_data_from_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')

    quotes = soup.find_all('div', class_='quoteText')

    raw_data = []

    for quote in quotes:
        text = quote.get_text(strip=True, separator=' ')
        raw_data.append({'Quote' : text, 'URL' : url})
    return raw_data

def scrape_all_pages(base_url):
    all_data = []
    page = 1

    while True:
        url = f"{base_url}?page={page}"

        page_data = get_data_from_website(url)

        if not page_data:
            break

        all_data.extend(page_data)
        page += 1
        time.sleep(2)

    return all_data

base_url = 'https://www.goodreads.com/author/quotes/92867.Linus_Torvalds'
data = scrape_all_pages(base_url)

df_extracted = pd.DataFrame(data)
print(df_extracted)

df_extracted.to_csv('linus_torvalds_quotes.csv', index=False)
print("Converted to CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\linus_torvalds_quotes.csv'

df = pd.read_csv(csv_filepath)

def cleaned_content(text):
    text = re.sub(r'[“”"\'`]', '', text)            # Remove quotes
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)             # Replace multiple question marks with one
    text = re.sub(r' - Linus Torvalds.*$', '', text) # Remove unnecessary author names and trailing text
    text = re.sub(r'\s*- [^\s]+.*$', '', text)       # General pattern for author names and trailing text
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Quote'] = df['Quote'].apply(cleaned_content)
print(df)

keywords_dict = {
    "Programming": ["Code", "Software", "Data Structures", "Programming", "System Design", "Bugs"],
    "Leadership": ["Visionary", "Leadership", "Motivation", "Decision Making", "Collaboration"],
    "Work Philosophy": ["Productivity", "Laziness", "Effort", "Sleep", "Getting Things Done"],
    "Technology and Society": ["Open Source", "Technology", "Social Conscience", "Civilization"],
    "Personal Traits": ["Offensive Humor", "Bluntness", "Bastard", "Honesty", "Rebellious"],
    "Operating Systems": ["Linux", "Unix", "Minix", "System Design"],
    "Ethics and Beliefs": ["Do No Harm", "Rules", "Freedom", "Privacy"]
}

def get_keywords(text):
    tags = []

    for categories, sub_categories in keywords_dict.items():
        if any(sub.lower() in text.lower() for sub in sub_categories):
            tags.append(categories)
    return ', '.join(tags)

df['Topic'] = df['Quote'].apply(get_keywords)

df['Topic'] = df['Topic'].replace('', 'Programming/Tech Motivations')
print(df)

filepath = 'D:\\Visual Studio Codes\\linus_torvalds_quotes.csv'

text = filepath.replace('.csv', '.txt')

with open(text, 'w', encoding='utf-8', newline='\n') as txt:
    txt.write(f"Row\tQuote\tTopic\tURL\n")

    for i,row in df.iterrows():
        quotes = row.get('Quote', 'No Quote')
        topics = row.get('Topic', 'No Topic')
        urls = row.get('URL', 'No URL')

        txt.write(f"{i + 1}\t{quotes}\t\t'{topics}'\t\t{urls}\n")

print("Sucessfully Scraped a Website!")


















