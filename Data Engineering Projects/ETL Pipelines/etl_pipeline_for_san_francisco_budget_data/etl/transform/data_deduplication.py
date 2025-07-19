'''
    Data Deduplication Module
'''
import pandas as pd

def deduplicate_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Deduplication Function
    '''
    # Perform data deduplication
    dataframe.drop_duplicates(inplace=True)
    print(f'Successfully perform data deduplication')

    return dataframe