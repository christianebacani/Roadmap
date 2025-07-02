'''
    Data Deduplication Module
'''
import pandas as pd

def deduplicate_integrated_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Deduplication Function
    '''
    # Perform data deduplication process
    dataframe.drop_duplicates(subset=['incident_number', 'id'], inplace=True)

    return dataframe