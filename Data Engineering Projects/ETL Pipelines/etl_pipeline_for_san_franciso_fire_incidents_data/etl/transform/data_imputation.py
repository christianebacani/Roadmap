'''
    Data Imputation Module
'''
import pandas as pd
from datetime import datetime

def impute_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Imputation Function
    '''
    # Initializing a dictionary to store imputed values per column for data imputation process
    columns = list(dataframe.keys())
    column_and_imputed_value = {}

    for column in columns:
        column_and_imputed_value[column] = None

    # Checking every data type to implement the imputations according to the datatype (Integer = median, Datetime and string = mode)
    for column in columns:
        values = []

        for value in dataframe[column]:
            if str(value).lower() != 'nan':
                values.append(value)
        
        if values == []:
            continue
        
        