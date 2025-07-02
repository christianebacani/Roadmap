'''
    Type Casting Module
'''
import pandas as pd
from datetime import datetime

def cast_data_type(dataframe: pd.DataFrame, column_and_data_type: dict[str, str], dataset_name: str) -> pd.DataFrame:
    '''
        Cast data type function
    '''
    # Get the columns
    columns = list(dataframe.keys())
    data = {}
    
    for column in columns:
        data[column] = []
    
    # Perform type casting operation
    for _, row in dataframe.iterrows():
        for column in columns:
            value = row.get(column)

            if str(value).lower() == 'nan':
                data[column].append(value)
                continue
            
            if column_and_data_type[column] == 'integer':
                value = int(value)
            
            elif column_and_data_type[column] == 'float':
                value = float(value)
            
            elif column_and_data_type[column] == 'string':
                value = str(value)

            elif column == 'incident_date':
                value = datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.%f').date()
            
            else:
                value = datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.%f')
            
            data[column].append(value)
    
    type_casted_dataframe = pd.DataFrame(data)
    print(f'Successfully perform type casting operation to {dataset_name} partitioned dataset')

    return type_casted_dataframe