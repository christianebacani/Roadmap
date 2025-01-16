import pandas as pd
import re

# Transform Job

def transform(df):
    df = df[df['Content'].str.strip() != ''] # Remove empty rows
    df = df.iloc[:2215].reset_index(drop=True) # Include necessary rows only
    df.drop([3, 4, 5, 6], axis=0, inplace=True) # Remove specific rows

    # Clean data using regex
    def clean_content(text):
        text = text.strip()
        text = re.sub(r'[\n\s\t]+', ' ', text)
        text = re.sub(r'(View Details)+$', '', text)
        text = re.sub(r'(Link to Description)+$', '', text)
        return text
    
    df['Content'] = df['Content'].apply(clean_content)
    print("\nTransformed Data:")
    return df 

