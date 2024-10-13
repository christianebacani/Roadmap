import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Hello Bebi, You can read out the comment above the code para maintindihan yung pro

# Get the link
link = 'https://bookroo.com/quotes/a-gentle-reminder'

# Request to scrape
r = requests.get(link)

if r.status_code == 200:
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup)

else:
    print("You`re not allowed to scrape!")

# Get the HTML Content
print(soup.prettify())
# Get the title of the website
print(soup.title.string)

# Get the text
text = soup.get_text(separator='\n', strip=True)
print(text)

# Split it into multiple sentences
split_text = text.split('\n')
print(split_text)

# Combined multiple n sentences per string
combined_sentences = ['. '.join(split_text[i:i+1]) for i in range(0, len(split_text), 1)]
print(combined_sentences)

# Create a DataFrame
df = pd.DataFrame(combined_sentences, columns=['Gentle Reminders Quote for you bebi, I scraped it and tailor it specifically for you'])
print(df)

# Function to clean the rows
# PS : Yung specific na function na ito nagpatulong ako kay ChatGPT kaya may mga professional comments since di pa ako ganon karunong sa regex, pero I know the process and yung iba nababasa ko yung code
def cleaned_text(text):
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

# Call the function
df['Gentle Reminders Quote for you bebi, I scraped it and tailor it specifically for you'] = df['Gentle Reminders Quote for you bebi, I scraped it and tailor it specifically for you'].apply(cleaned_text)
print(df)

# Keywords
specific_quotes = ["The right person will choose you just as deeply as you choose them",
                    "The right person will know how to hold your love",
                    "The strongest human beings, the ones who laugh the loudest and hope the hardest, the ones who are always there for others- those souls often need people there for them. So, please- check on your kind friends",
                    "So keep going- because the world needs your uniqueness",
                    "If it is for you, trust that it will find you",
                    'No one will ever fully be able to understand the internal battles you had to endure just to heal, just to grow, just to make it here today. Be proud of the way you fought to save yourself. Be proud of the way you survived',
                    'If something ignites you, chase it',
                    'I hope you have the courage to go deeper. To never exist on the surface of your life, even if it’s easier or more convenient',
                    'You never know what is waiting for you on the other side of your hope',
                    'You have to let go. You have to let go because when you hold on, when you keep something alive inside of you, you are allowing for your past to take up the space in your heart and in your mind that is meant for your future',
                    'Do not seek familiarity, do not keep searching for your past in your future. Trust what comes',
                    'I hope you have the courage to go deeper. To never exist on the surface of your life, even if it’s easier or more convenient']

# Create a DataFrame that contains relevant quotes
quote_df = df[df['Gentle Reminders Quote for you bebi, I scraped it and tailor it specifically for you'].isin(specific_quotes)]
print(quote_df)

# Improvise by adding specific data in a new row
quote_df.loc[len(quote_df)] = ['I hope you have the courage to go deeper. To never exist on the surface of your life, even if it’s easier or more convenient']

quote_df.to_csv('gentle_reminder.csv', index=False)
print("Successfully Extracted the necessary quotes only!")

# Read the csv filepath
csv_filepath = 'D:\\Visual Studio Codes\\gentle_reminder.csv'

df = pd.read_csv(csv_filepath)
print(df)


print(df.columns)

# Modify into a .txt file format
text_file = csv_filepath.replace('.csv', '.txt')

with open(text_file, 'w', encoding='utf-8', newline='\n') as txt:
    txt.write(f"Gentle Reminders Quote for you bebi, I scraped it and tailor it specifically for you\n")

    for i, row in df.iterrows():
        quotes = row.get('Gentle Reminders Quote for you bebi, I scraped it and tailor it specifically for you', 'N/A')

        txt.write(f"{quotes}\n")

print("Converted to Text File Format!")

