'''
    Data Type Casting Module
'''
import pandas as pd
from datetime import datetime

def cast_datatype(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Type Casting Function
    '''
    # Initializing a dictionary for storing data after type casting process
    columns = list(dataframe.keys())
    data = {}

    for column in columns:
        data[column] = []

    # Type casting
    for _, row in dataframe.iterrows():
        for column in columns:
            value = row.get(column)

            if value is None:
                data[column].append(value)
                continue

            try:
                datetime_value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                data[column].append(datetime_value)
                continue

            except:
                pass

            if str(value).isdigit():
                value = int(value)
                data[column].append(value)
                continue

            try:
                value = float(value)

            except:
                value = str(value)
            
            data[column].append(value)
    
    return pd.DataFrame(data)