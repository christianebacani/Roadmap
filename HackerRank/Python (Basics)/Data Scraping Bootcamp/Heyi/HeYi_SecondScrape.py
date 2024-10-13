import requests 
import pandas as pd
from bs4 import BeautifulSoup
import re


link = 'https://decrypt.co/31693/binance-is-still-accessible-from-china-says-report'

r = requests.get(link)

if r.status_code == 200:
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup)

else:
    print("You`re not allowed to scrape!")

print(soup.prettify())

print(soup.title.string)

text = soup.get_text(separator='\n', strip=True)
print(text)


text_split = text.split('\n')
print(text_split)


combined_sentences = ['. '.join(text_split[i:i+3]).strip() for i in range(0, len(text_split), 3)]
print(combined_sentences)

df = pd.DataFrame(combined_sentences, columns=['Content'])
print(df)

def clean_content(text):
    text = re.sub(r'[“”"\'`]', '', text)            # Remove quotes
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)             # Replace multiple question marks with one
    text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text) # Remove special characters (keep basic punctuations)
    text = re.sub(r'-{2,}', '-', text)              # Replace multiple hyphens with a single hyphen
    text = re.sub(r'\(.*?\)', '', text)             # Remove text inside parentheses
    text = re.sub(r'[^\x00-\x7F]+', '', text)       # Remove non-ASCII characters
    text = re.sub(r'\n+', ' ', text)                # Replace newlines with space
    text = re.sub(r'\t+', ' ', text)                # Replace tabs with space
    text = re.sub(r'^[^\w]+|[^\w]+$', '', text)     # Remove punctuation from start and end
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Content'] = df['Content'].apply(clean_content)

csv = df.to_csv('heyi_article.csv', index=False)
print(csv)

csv_filepath = 'D:\\Visual Studio Codes\\heyi_article.csv'

df = pd.read_csv(csv_filepath)
print(df)

df.dropna(how='all', inplace=True)

print(df)

extracted_rows = df.iloc[254:266]
print(extracted_rows)

df = pd.DataFrame(extracted_rows, columns=['Content'])
print(df)


cleaned_csv = df.to_csv('heyi_article_clean.csv', index=False)
print(cleaned_csv)

cleaned_csv_filepath = 'D:\\Visual Studio Codes\\heyi_article_clean.csv'

df = pd.read_csv(cleaned_csv_filepath)
print(df)

df.dropna(how='all', inplace=True)
print(df)

print("Columns:")
print(df.columns)

keywords = ['Binance', 'China', 'Crypto', 'cryptocurrency', 'Alexa', 'Bijie technology']

def extract_keywords(text):
    text = text.lower()
    founded_keywords = [keyword for keyword in keywords if keyword.lower() in text]
    return ', '.join(founded_keywords) if founded_keywords else 'Heyi Article'


df['Topic'] = df['Content'].apply(extract_keywords)

print(df)

print("Columns")
print(df.columns)

heyi_article = df.to_csv('heyi_article_keywords.csv', index=False)
print(heyi_article)

heyi_article_filepath = 'D:\\Visual Studio Codes\\heyi_article_keywords.csv'

df = pd.read_csv(heyi_article_filepath)
print(df)

df.dropna(how='all', inplace=True)
print(df)


heyi_txt = heyi_article_filepath.replace('.csv', '.txt')

with open(heyi_txt, 'w', encoding='utf=8', newline='\n') as txt:
    txt.write("Content  Topic\n")

    for i, row in df.iterrows():
        contents = row.get('Content', 'No Content')
        topics = row.get('Topic', 'No Topic')

        txt.write(f"{contents}. {topics}\n")

print(f"Successfully Converted to .txt file format! : {heyi_txt}")




