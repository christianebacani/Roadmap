'''
    Data Format Revision Module
'''
import pandas as pd
from datetime import datetime

def revise_data_format(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Format Revision Function
    '''
    # Initializing a dictionary for storing data after data format revisioning proces
    columns = list(dataframe.keys())
    data = {}

    for column in columns:
        data[column] = []
    
    for _, row in dataframe.iterrows():
        for column in columns:
            value = row.get(column)

            if value is None:
                data[column].append(value)
                continue

            # TODO: Implement a functionality to format values