import requests
import pandas as pd
from bs4 import BeautifulSoup
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
        url = f"https://www.goodreads.com/quotes/search?page={page}&q=Kobe+Bryant"
        page_data = get_data_from_website(url)

        if not page_data:
            break
        all_data.extend(page_data)
        page += 1
        time.sleep(1)

    return all_data

base_url = 'https://www.goodreads.com/quotes/search?page=1&q=Kobe+Bryant'
data = scrape_all_pages(base_url)

df = pd.DataFrame(data)
print(df)

def cleaned_content(text):
    text = re.sub(r'[“”"\'`]', '', text)            # Remove quotes
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)             # Replace multiple question marks with one
    text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text) # Remove special characters (keep basic punctuations)
    text = re.sub(r'-{2,}', '-', text)              # Replace multiple hyphens with a single hyphen
    text = re.sub(r'[^\x00-\x7F]+', '', text)       # Remove non-ASCII characters
    text = re.sub(r'\n+', ' ', text)                # Replace newlines with space
    text = re.sub(r'\t+', ' ', text)                # Replace tabs with space
    text = re.sub(r'^[^\w]+|[^\w]+$', '', text)     # Remove punctuation from start and end
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Quote'] = df['Quote'].apply(cleaned_content)

print(df)

keyword_dict = {
    "Pro Hoops": ["NBA", "basketball", "scoring", "MVP", "championship", "game", "team", "shooting", "offense", "defense"],
    "Mamba Mentality": ["Black Mamba", "Kobe", "Bryant", "Lakers", "24", "8", "legend", "GOAT", "Kobe System", "retirement"],
    "Iconic Achievements": ["championships", "MVP awards", "Olympic gold", "scoring titles", "All-Star", "Hall of Fame", "records"],
    "Grit & Grind": ["hard work", "dedication", "mentality", "perseverance", "focus", "leadership", "drive", "competitive"],
    "Motivational Vibes": ["motivation", "inspiration", "dreams", "success", "never give up", "work ethic", "resilience", "legacy"],
    "Family Life": ["father", "family", "daughter", "Gianna", "Vanessa", "Mamba Mentality", "business", "philanthropy", "books"],
    "Heartbreaking Loss": ["helicopter crash", "death", "loss", "tribute", "legacy", "mourning", "impact", "sadness"],
    "Mamba Skillset": ["footwork", "fadeaway", "post moves", "jump shot", "dribbling", "passing", "basketball IQ", "clutch"],
    "Sports Legacy": ["basketball legend", "career highlights", "icon", "impact on the game", "global influence", "inspiration"],
    "Life Lessons": ["self-discipline", "growth mindset", "overcoming obstacles", "passion", "dedication", "focus on greatness"],
    "Cultural Impact": ["Nike shoes", "Kobe Bryant Academy", "basketball camps", "Mamba Academy", "brand ambassador", "influencer"],
    "Post-Career Ventures": ["film production", "Granity Studios", "Dear Basketball", "Oscar win", "investments", "businessman"],
    "Tributes & Honors": ["Kobe Bryant Day", "statues", "memorials", "court renaming", "jersey retirement", "global tributes"],
    "Global Hero": ["international icon", "Olympics", "fans worldwide", "ambassador of the game", "global superstar", "role model"],
    "Winning Culture": ["winning mentality", "champion mindset", "game-winning shots", "playoff performance", "ultimate competitor"]
}


def generate_keywords(text):
    tags = []

    for category, sub_category in keyword_dict.items():
        if any(sub.lower() in text.lower() for sub in sub_category):
            tags.append(category)
    return ', '.join(tags)

df['Topic'] = df['Quote'].apply(generate_keywords)

df['Topic'] = df['Topic'].replace('', 'Kobe Bryant')

df.to_csv('kobe_quotes.csv', index=False)
print("Saved into CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\kobe_quotes.csv'

text_filepath = csv_filepath.replace('.csv', '.txt')

with open(text_filepath, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"Row\tQuote\tTopic\tURL\n")

    for i,row in df.iterrows():
        quotes = row.get('Quote', 'No Quote')
        topics = row.get('Topic', 'No Topic')
        urls = row.get('URL', 'No URL')

        text.write(f"{i + 1}\t{quotes}\t{topics}\t{urls}\n")

print("Successfully Scraped!")
