import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

link = 'https://www.entrepreneur.com/en-ae/entrepreneurs/breaking-the-mould-he-yi-co-founder-and-chief-marketing/435688'

response = requests.get(link)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.get_text(separator='\n', strip=True)
    print(text)

    
else:
    print("You`re not allowed to scrape here!")

split_text = text.split('\n')
print(split_text)

# Function to extract text inside the quotes

def extract_quotes(text_data):
    quotes = []

    for line in text_data:
        # Find quotes
        found_quotes = re.findall(r'"(.*?)"', line)

        # Insert the data that has a quotes inside an empty list
        if found_quotes:
            quotes.extend(found_quotes)
    return quotes # Return the list of data that contains quotes

extracted_quotes = extract_quotes(split_text)

df = pd.DataFrame(extracted_quotes, columns=['Quotes'])
print(df)

df.to_csv('heyi_quotes.csv', index=False)
print("Successfuly Extracted the Quotes inside the content!")

# Cleaned the text

csv_filepath = 'D:\\Visual Studio Codes\\heyi_quotes.csv'

df = pd.read_csv(csv_filepath)

df.dropna(how='all', inplace=True)
print(df)

def clean_text(text):
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

df['Quotes'] = df['Quotes'].apply(clean_text)
print(df)

index_exclude = {2, 3, 4, 5, 6, 20, 21, 23, 24}
mask = ~df.index.isin(index_exclude)

heyi_quotes = df[mask]

df = heyi_quotes

keywords = ['interview', 'breakfast', 'lunch',
            'startups', 'tokens', 'CZ', 'binance.com',
            'China', 'BNB coin', 'business', 'Binance',
            'drama', 'global challenge', 'mum', 'successful',
            'country', 'reading', 'internet',
            'learning', 'family', 'teacher', 'women',
            'inspirational', 'life', 'jobs',
            'challenge', 'television host', 'crypto startup',
            'to do', 'world', 'impact',
            'Binance', 'female', 'soft skills']

def extract_keywords(text):
    text = text.lower()

    founded_keywords = [word for word in keywords if word.lower() in text]
    return ', '.join(founded_keywords) if founded_keywords else 'Heyi Quotes / Binance'
    
df['Keywords'] = df['Quotes'].apply(extract_keywords)

print(df)


df.to_csv('heyi_quotes.csv', index=False)
print("Successfuly Created a Keywords")

filepath = 'D:\\Visual Studio Codes\\heyi_quotes.csv'

df = pd.read_csv(filepath)

text_filepath = filepath.replace('.csv', '.txt')

with open(text_filepath, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"Quotes\tKeywords\n")

    for i, row in df.iterrows():
        quotes = row.get('Quotes', 'No Quotes')
        keywords = row.get('Keywords', 'No Keywords')

        text.write(f"{quotes}:\t{keywords}\n")

print("Successfuly Scraped!")
