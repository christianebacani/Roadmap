'''
    Type Casting Module
'''
import pandas as pd
from datetime import datetime

def cast_data_type(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Type Casting Function
    '''
    # Using .keys() method to get all the variable/field names
    columns = list(dataframe.keys())
    data = {}

    for column in columns:
        data[column] = []
        
    # Type casting process by using the name of the column or using try and catch statement
    for _, row in dataframe.iterrows():
        for column in columns:
            value = row.get(column)

            if column == 'incident_date':
                value = datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.%f').date()
                data[column].append(value)
                continue

            elif column in ['data_as_of', 'data_loaded_at'] or 'dttm' in column:
                value = datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.%f')
                data[column].append(value)
                continue

            else:
                pass
            
            if str(value).isdigit():
                value = int(value)
                data[column].append(value)
                continue

            try:
                value = float(value)
            
            except ValueError:
                value = str(value)
            
            data[column].append(value)

    type_casted_dataframe = pd.DataFrame(data)

    return type_casted_dataframe