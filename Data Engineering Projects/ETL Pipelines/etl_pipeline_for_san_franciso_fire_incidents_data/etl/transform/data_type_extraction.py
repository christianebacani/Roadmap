'''
    Data Type Extraction Module
'''
import pandas as pd

from datetime import datetime

def get_the_data_type_of_every_column(dataframe: pd.DataFrame) -> dict[str, str]:
    '''
        Get function to get the data type of every column
        before data partition process
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

    # Get the data type of each column based on the frequencies of the data type of distinct values per column
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