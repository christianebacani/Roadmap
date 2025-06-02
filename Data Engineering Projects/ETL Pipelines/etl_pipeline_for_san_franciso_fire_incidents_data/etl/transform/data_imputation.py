'''
    Data Imputation Module
'''
import pandas as pd
from datetime import datetime

def impute_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Imputation Function
    '''
    # Initializing dictionary to map dataframe after data imputation rather than in-place modification
    columns = list(dataframe.keys())
    data = {}

    for i in range(len(columns)):
        data[columns[i]] = []
    
    # Initializing a list to store columns names with same data type for imputation purposes
    columns_with_integer_value, columns_with_datetime_value, columns_with_string_value = [], [], []

    for i in range(len(columns)):
        # Checking their data type
        if isinstance(dataframe[columns[i]][0], int):
            columns_with_integer_value.append(columns[i])
            continue

        try:
            datetime.strptime(dataframe[columns[i]][0], '%Y-%m-%dT%H:%M:%S.%f')
            columns_with_datetime_value.append(columns[i])

        except ValueError:
            columns_with_string_value.append(columns[i])

    # Using set to remove duplicate column names
    columns_with_integer_value, columns_with_datetime_value, columns_with_string_value = list(set(columns_with_integer_value)), list(set(columns_with_datetime_value)), list(set(columns_with_string_value))

    # Debugging purposes
    print('Columns with integer value:')
    print(columns_with_integer_value)
    print()

    print('Columns with datetime value:')
    print(columns_with_datetime_value)
    print()

    print('Columns with string value:')
    print(columns_with_string_value)