import pandas as pd
import re
import os 

# Transform Phase

# Transform Data (Pre-Cleaning)
def transform_data():
    source_filepath = 'D:\\Visual Studio Codes\\Data Engineering Projects in Python\\ETL Pipeline\\Source Data Files\\data_architecture_article.csv' 
    with open(source_filepath, 'r', encoding='utf-8', newline='\n') as f:
        data = f.read() # Read CSV and Parse as a string\

    f.close() # Close the file

    rows = data.split('\n')

    df = pd.DataFrame(rows, columns=['Content'])
    print("Extracted Dataframe:")
    print(df)

    # Remove empty rows
    df = df[df['Content'].str.strip() != '']
    # Exclude unncessary rows
    df = df.iloc[14:298].reset_index(drop=True)


    # Clean Data using Regex
    def clean_content(text):
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\t+', ' ', text)
        text = re.sub(r'[\"\"\“\”\’]+' , '', text)
        text = re.sub(r'—', ':', text)
        text = re.sub(r'[,.!?]*$', '', text)
        text = text.strip()

        return text

    df['Content'] = df['Content'].apply(clean_content)
    os.remove(source_filepath) # Remove unused csv file inside the source data filepath
    return df

