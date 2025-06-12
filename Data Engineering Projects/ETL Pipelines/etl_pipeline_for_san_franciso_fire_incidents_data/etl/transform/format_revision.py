'''
    Data Format Revision Module
'''
import pandas as pd

def revive_format(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Format Revision Function
    '''
    # Using .keys() method to get all the variable/field names
    columns = list(dataframe.keys())
    
    for index, row in dataframe.iterrows():
        for column in columns:
            value = row.get(column)

            if column in ['incident_date', 'data_as_of', 'data_loaded_at'] or 'dttm' in column:
                continue

            if isinstance(value, (int, float)):
                continue