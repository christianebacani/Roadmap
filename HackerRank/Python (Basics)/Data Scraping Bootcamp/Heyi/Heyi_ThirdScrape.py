import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import csv

link = 'https://markets.businessinsider.com/news/currencies/binance-founder-yi-he-regulation-crypto-growth-headquarter-search-meme-2021-11'

r = requests.get(link)

if r.status_code == 200:
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup)

else:
    print("You`re not allowed to scrape here!")

print(soup.prettify())
print(soup.title.string)

text = soup.get_text(separator='\n', strip=True)
print(text)

sentences = text.split('\n')
print(sentences)

combined_sentences = ['. '.join(sentences[i:i+2]) for i in range(0, len(sentences), 2)]
print(combined_sentences)

df = pd.DataFrame(combined_sentences, columns=['Content'])
print(df)

def cleaned_content(text):
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

df['Content'] = df['Content'].apply(cleaned_content)
print(df)

csv = df.to_csv('heyi_interview_binance.csv', index=False)
print("Successfully Cleaned and Converted to CSV File!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_interview_binance.csv'
df = pd.read_csv(csv_filepath)
print(df)

df.dropna(how='all', inplace=True)

extracted_rows = df.iloc[65:89]
print(extracted_rows)

df = pd.DataFrame(extracted_rows, columns=['Content'])
print(df)

cleaned_csv = df.to_csv('heyi_interview_binance_regulations.csv', index=False)
print("Successfully Extracted the revelant data!")

cleaned_csv_filepath = 'D:\\Visual Studio Codes\\heyi_interview_binance_regulations.csv'

df = pd.read_csv(cleaned_csv_filepath)
print(df)

mask = ~df.index.isin(range(2, 10))
filtered_df = df[mask]

print(filtered_df)

filtered_df.to_csv('heyi_binance_regulations_article.csv', index=False)
print("Successfully Excluded a specific row!")


filtered_csv_filepath = 'D:\\Visual Studio Codes\\heyi_binance_regulations_article.csv'

df = pd.read_csv(filtered_csv_filepath)
print(df)

keywords = ['Binance', 'crypto', 'crypto regulation',
            'Insider', 'crypto growth', 'meme coins',
            'headquarters', 'global regulators', 'working from home',
            'digital asset space', 'insider training', 'crypto growth',
            'crypto demand', 'Internet', 'dogecoin', 'FOMO', 'bitcoin',
            'ether', 'Women', 'remote work', 'leadership']

def extract_keywords(text):
    text = text.lower()
    founded_keywords = [word for word in keywords if word.lower() in text]
    return ', '.join(founded_keywords) if founded_keywords else 'Heyi Interview about Binance'

df['Topic'] = df['Content'].apply(extract_keywords)
print(df)

df.to_csv('heyi_binance_regulations_keywords.csv', index=False)
print("Successfully added a keywords!")

filepath = 'D:\\Visual Studio Codes\\heyi_binance_regulations_keywords.csv'

df = pd.read_csv(filepath)
print(df)

df.dropna(how='all', inplace=True)
print(df)

print("Columns:")
print(df.columns)

text_filepath = filepath.replace('.csv', '.txt')

with open(text_filepath, 'w', encoding='utf-8', newline='\n') as txt:
    txt.write(f"Content\tTopic\n")

    for i, row in df.iterrows():
        contents = row.get('Content', 'No Content')
        topics = row.get('Topic', 'No Topic')

        txt.write(f"{contents}.\t{topics.capitalize()}\n")

print("Successfully Extracted, Transformed/Cleaned, Loaded into a Text File Format!")

