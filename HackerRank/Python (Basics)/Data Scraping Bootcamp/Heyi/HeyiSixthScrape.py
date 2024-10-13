import re
import pandas as pd
from bs4 import BeautifulSoup
import requests

link = 'https://www.investing.com/news/cryptocurrency-news/interview-with-he-yi-cofounder-and-the-cmo-of-binance-2459637'

response = requests.get(link)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.get_text(separator='\n', strip=True)
    print("You can scraped here!")

    
else:
    print("You`re not allowed to scrape here!")


split_text = text.split('\n')
print(split_text)

combined_sentences = ['\n'.join(split_text[i:i+3]) for i in range(0, len(split_text), 3)]
print(combined_sentences)

df = pd.DataFrame(combined_sentences, columns=['Content'])
print(df)

df.to_csv('heyi_data.csv', index=False)
print("Converted to CSV File Format!")

filepath = 'D:\\Visual Studio Codes\\heyi_data.csv'

df = pd.read_csv(filepath)
print(df)

def cleaned_content(text):
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)             # Replace multiple question marks with one
    text = re.sub(r'-{2,}', '-', text)              # Replace multiple hyphens with a single hyphen
    text = re.sub(r'\t+', ' ', text)                # Replace tabs with space
    text = re.sub(r'[^\x00-\x7F]+', '', text)       # Remove non-ASCII characters
    text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text) # Keep only allowed characters
    text = text.strip()                             # Trim leading and trailing spaces
    return text 

df['Content'] = df['Content'].apply(cleaned_content)
print(df)

df.to_csv('heyi_data.csv', index=False)
print("Successfuly Cleaned the Data!")

cleaned_csv_filepath = 'D:\\Visual Studio Codes\\heyi_data.csv'
df = pd.read_csv(cleaned_csv_filepath)
print(df)

included_rows = df.index.isin(range(119, 135))
df = df[included_rows]
print(df)

keywords = ['Binance', 'Cryptocurrency', 'CZ', 
            'OKCoin', 'CMO', 'feedback', 'users',
            'tweets', 'Clubhouse sessions', 'Online Conferences', 
            'Crypto', 'Considerations', 'Meercat', 'BSC', 'Blockchain',
            'Assets', 'BNB', 'Society', 'Problems', 'Copyright Issues', 'Trading Volume',
            'Yixia Technology', 'Blockchain', 'Government Information', 'NFT', 'Digital Artwork',
            'Industry', 'Mainstream', 'Portfolio', 'MS', 'CoinMarketCap', 'Growth', 'ETH',
            'Global Exchanges', 'Future Plans', 'Decentralized', 'Centralized', 'Governments',
            'Countries', 'Smart Chain', 'Expansions', 'Competitor', 'Process', 'Freedom', 'Biggest Break', 
            'Self Breakthroughs', 'Education', 'Women', 'Gender Equality', 'Binance Charity Foundation'
]
default_keywords = ['Heyi Cryptocurrency News']

def generate_keywords(text):
    text = text.lower()
    founded_keywords = [word.capitalize() for word in keywords if word.lower() in text]
    return founded_keywords if founded_keywords else default_keywords

df['Keyword'] = df['Content'].apply(generate_keywords)

print(df)

df.to_csv('heyi_data.csv', index=False)
print("Successfully Added Keywords Column!")

final_filepath = 'D:\\Visual Studio Codes\\heyi_data.csv'

df = pd.read_csv(final_filepath)
print(df)

df.dropna(how='all', inplace=True)
print(df)

text_filepath = final_filepath.replace('.csv', '.txt')

with open(text_filepath, 'w', newline='\n', encoding='utf-8') as txt:
    txt.write(f"Index\tContent   Keyword\n")

    for i, row in df.iterrows():
        contents = row.get('Content', 'No Content')
        keywords = row.get('Keyword', 'No Keyword')

        txt.write(f"{i + 1}\t{contents}:   {keywords}\n")

print("Successfuly Converted to Text File Format!")


