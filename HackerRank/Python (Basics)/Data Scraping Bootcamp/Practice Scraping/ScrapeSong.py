import pandas as pd
import requests
from bs4 import BeautifulSoup

# Hello Bebi, You can read out the comment above the code para maintindihan yung process

# Get the link
link = 'https://www.azlyrics.com/lyrics/taylorswift/daylight.html'
response = requests.get(link)

# Request
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    print("\nYou`re allowed to scrape here!")
else:
    print("\nYou`re not allowed to scrape here!")

# Find the html div tag to scrape the content
lyrics_div = soup.find('div', class_=None, id=None)
if lyrics_div:
    lyrics = lyrics_div.get_text(separator='\n', strip=True)

else:
    lyrics = None
    print("Couldn't find the lyrics div!")
    
# Split the content into newlines
if lyrics:
    lyrics_lines = lyrics.split('\n')

    # Create a DataFrame
    df = pd.DataFrame(lyrics_lines, columns=['Daylight Lyrics'])

    csv_path = 'daylight_lyrics.csv'
    df.to_csv(csv_path, index=False)
    print(f"Lyrics saved to {csv_path}") # Save into a CSV File


    # Read the CSV Filepath
    csv_filepath = 'D:\\Visual Studio Codes\\daylight_lyrics.csv'

    # Modify it into .txt file format
    text_file = csv_filepath.replace('.csv', '.txt')

    # Modify
    with open(text_file, 'w', encoding='utf-8', newline='\n') as txt:
        txt.write(f"Daylight Lyrics\n")

        for i,row in df.iterrows():
            lyrics = row.get('Daylight Lyrics', 'N/A')

            txt.write(f"{lyrics}\n")
        print("Successfully Converted to .txt file format!")

