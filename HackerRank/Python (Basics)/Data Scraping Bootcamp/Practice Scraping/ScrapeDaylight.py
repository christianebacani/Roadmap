import pandas as pd


csv_filepath = 'D:\\Visual Studio Codes\\daylight_lyrics.csv'

df = pd.read_csv(csv_filepath)

with_column = pd.DataFrame(df, columns=['Daylight Lyrics'])

txt_file = csv_filepath.replace('.csv', '.txt')

with open(txt_file, 'w', encoding='utf-8', newline='\n') as txt:
    txt.write(f"Daylight Lyrics\n")

    for i, row in df.iterrows():
        daylight_lyrics = row.get('Daylight Lyrics', 'N/A')

        txt.write(f"{daylight_lyrics}\n")
        print("Successfully Saved into a .txt file format!")
