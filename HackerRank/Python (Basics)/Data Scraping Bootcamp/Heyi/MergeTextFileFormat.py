import os
import pandas as pd

'''




directory = 'D:\\Visual Studio Codes\\'
output_file = 'heyi_articles_and_youtube_interview.txt'

with open(output_file, 'w', encoding='utf-8', newline='\n') as outfile:
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8', newline='\n') as infile:
                outfile.write(infile.read())
                outfile.write('\n')


print("Successfully Merged into one single text file format!")




'''





text_file = 'D:\\Visual Studio Codes\\heyi_articles_and_youtube_interview.txt'

df = pd.read_csv(text_file, header=None, sep='\t', encoding='utf-8') 

df.columns = ['Content', 'Topic']
print(df)

filtered_df = df[~df['Content'].isin(['Content']) & ~df['Topic'].isin(['Topic'])]

filtered_df.to_csv('heyi_articles_and_interviews.txt', index=False, sep='\t')
print("Successfully Merged and Cleaned!")
