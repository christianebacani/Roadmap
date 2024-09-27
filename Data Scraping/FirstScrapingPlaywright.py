from keybert import KeyBERT
import pandas as pd
import playwright
from playwright.async_api import async_playwright
import re 
import nest_asyncio
import asyncio

nest_asyncio.apply()

async def get_text_content():
    url = 'https://lelouch.dev/blog/you-are-probably-not-dumb/?ref=dailydev'

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)

        context = await browser.new_context(
            user_agent='Your Custom User Agent Here'
        )

        page = await context.new_page()
        await page.goto(url, wait_until='domcontentloaded')

        await page.wait_for_selector('body')

        text_content = await page.inner_text('body')

        await browser.close()

        with open('motivational_learnings.csv', 'w', encoding='utf-8', newline='\n') as csv:
            csv.write(text_content)

asyncio.run(get_text_content())

csv_filepath = 'D:\\Visual Studio Codes\\motivational_learnings.csv'

with open(csv_filepath, 'r', encoding='utf-8', newline='\n') as csv_file:
    data = csv_file.read()

splitted_text = data.split('\n')

combined_sentences = [' '.join(splitted_text[word:word+2]) for word in range(0, len(splitted_text), 2)]

df = pd.DataFrame(combined_sentences, columns=['Content'])
print(df)

df = df[df['Content'].str.strip() != '']

df = df.iloc[11:27]


def cleaned_content(text):
    text = re.sub(r'[.,!?]*$', '', text)
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = text.strip()

    return text

df['Content'] = df['Content'].apply(cleaned_content)

print(df)

model = KeyBERT('distilbert-base-nli-mean-tokens')

def generate_keywords(text):

    keywords = [keyword for keyword, score in model.extract_keywords(text)]

    capitalize_keywords = [word.title() for word in keywords]

    return ', '.join(capitalize_keywords)

df['Keyword'] = df['Content'].apply(generate_keywords)

print(df)

df.to_csv('motivational_learnings.csv', index=False)
print("Successfuly Converted into CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\motivational_learnings.csv'

textfile = csv_filepath.replace('.csv', '.txt')

with open(textfile, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"Content\t'Keyword'\n")
    for i, row in df.iterrows():
        content = row.get('Content', 'No Content')
        keyword = row.get('Keyword', 'No Keyword')
        text.write(f"{content}\t'{keyword}'\n")

print("Successfully Scraped!")

# TODO : Provide Inline Documentations
