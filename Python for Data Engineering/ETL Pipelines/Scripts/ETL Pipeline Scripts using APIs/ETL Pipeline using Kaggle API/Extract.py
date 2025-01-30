from zipfile import ZipFile
import pandas as pd

# Extract

def extract(zipfile):
    with ZipFile(zipfile, 'r') as z:
        z.extract('earthquake_data.csv')
    z.close() 

    df = pd.read_csv('earthquake_data.csv')
    return df 

