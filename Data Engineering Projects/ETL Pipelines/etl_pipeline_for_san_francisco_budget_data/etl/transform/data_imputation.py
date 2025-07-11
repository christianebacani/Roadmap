'''
    Data Imputation Module
'''
import pandas as pd

def impute_missing_values(integrated_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Imputation Function
    '''
    # Initialized the columns of the integrated dataset
    columns = list(integrated_dataframe.keys())
    
    # Get the distinct values of every column
    column_and_distinct_values = {}

    for column in columns:
        column_and_distinct_values[column] = []
    
    for column in columns:
        distinct_values = list(set(integrated_dataframe[column]))
        column_and_distinct_values[column] = distinct_values
    
    # Display the column and distinct values for debugging purposes only
    for column, distinct_values in column_and_distinct_values.items():
        print(column)
        print(f'{distinct_values}')
        print()
    
    data_type_and_frequencies = {
        'nan': 0,
        'datetime': 0,
        'string': 0,
        'integer': 0,
        'float': 0
    }