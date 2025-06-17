'''
    Data Imputation Module
'''
import pandas as pd
from scipy.stats import skew

def impute_values_from_the_integrated_datasetr(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Imputation Function
    '''
    # Using .keys() method to get all the variable/field names
    columns = list(dataframe.keys())
    
    # Initializing a dictionary to store the variable/field name as a key and imputed value as a value
    columns_and_imputed_value = {}

    # Initializing a dictionary to store the variable/field names as a key and skewness as a value
    columns_and_skewness = {}

    for column in columns:
        values = []

        for row_number in range(0, 705909, 1000):
            values.extend(list(dataframe[column][row_number : row_number + 1000]))
            print(f'Extracting the values of column: {column} from {row_number}-{row_number} rows for data imputation process')

        data = pd.Series(values)

        # Check if it's a numerical value using try and catch statement
        try:
            data.median()
            skewness = skew(data.dropna())
            columns_and_skewness[column] = skewness

        # Get the mode value if it's not a numerical value
        except TypeError:
            data = data.dropna()
            columns_and_imputed_value[column] = data.mode()[0]

    # Identifying the skewness of the numerical value to determine the imputed value
    for key, value in columns_and_skewness.items():
        if value == 0 or value < 0.5:
            imputed_value = int(pd.Series(dataframe[key].dropna()).mean())
        
        else:
            imputed_value = int(pd.Series(dataframe[key].dropna()).median())
        
        columns_and_imputed_value[key] = imputed_value
    
    for column in columns:
        dataframe[column] = dataframe[column].fillna(columns_and_imputed_value[column])
    
    return dataframe