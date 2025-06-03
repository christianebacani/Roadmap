'''
    Data Imputation Module
'''
import pandas as pd

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
        
        value_is_digit = True

        for value in values:
            if not str(value).isdigit():
                value_is_digit = False
                break
        
        if value_is_digit:
            column_and_imputed_value[column] = round(pd.Series(values).median(), 0)
        
        else:
            column_and_imputed_value[column] = pd.Series(values).mode()[0]
    
    # Initializing dictionary to store dataframe after imputation process
    data = {}

    for column in columns:
        data[column] = []
    
    # Data Imputation
    for _, row in dataframe.iterrows():
        for column in columns:
            value = row.get(column)

            if str(value).lower() == 'nan':
                value = column_and_imputed_value[column]

            data[column].append(value)
    
    return pd.DataFrame(data)