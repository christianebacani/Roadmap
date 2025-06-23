'''
    Type Casting Module
'''
import pandas as pd
from datetime import datetime

def get_the_data_type_of_every_column(dataframe: pd.DataFrame) -> dict[str, str]:
    '''
        Get function to get the data type of every column
        for type casting process
    '''
    # Get the column
    columns = list(dataframe.keys())

    column_and_distinct_values = {}

    # Extract the values per column in every 
    for column in columns:
        values = list(dataframe[column])
        values = list(set(values))

        column_and_distinct_values[column] = values
        print(f'Successfully extracted the values of column: {column} from integrated staged dataset for getting the data type of every column')

    column_and_data_type = {}

    for column, distinct_value in column_and_distinct_values.items():
        data_type_and_frequencies = {
            'nan': 0,
            'datetime': 0,
            'integer': 0,
            'float': 0,
            'string': 0
        }

        for value in distinct_value:
            if str(value).lower() == 'nan':
                data_type_and_frequencies['nan'] = data_type_and_frequencies['nan'] + 1
                continue

            try:
                datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.%f')
                data_type_and_frequencies['datetime'] = data_type_and_frequencies['datetime'] + 1
                continue

            except ValueError:
                pass

            if str(value).isdigit():
                data_type_and_frequencies['integer'] = data_type_and_frequencies['integer'] + 1
                continue

            try:
                float(value)
                data_type_and_frequencies['float'] = data_type_and_frequencies['float'] + 1
            
            except ValueError:
                data_type_and_frequencies['string'] = data_type_and_frequencies['string'] + 1
    
        if data_type_and_frequencies['string'] > 0:
            column_and_data_type[column] = 'string'
            continue

        maximum_frequency = max(list(data_type_and_frequencies.values()))

        for data_type, frequency in data_type_and_frequencies.items():
            if maximum_frequency != frequency:
                continue

            column_and_data_type[column] = data_type
            break
    
    return column_and_data_type

def cast_data_type(dataframe: pd.DataFrame, column_and_data_type: dict[str, str], dataset_name: str) -> pd.DataFrame:
    '''
        Cast data type function
    '''
    # Get the columns
    columns = list(dataframe.keys())
    data = {}
    
    for column in columns:
        data[column] = []
    
    for index, row in dataframe.iterrows():
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