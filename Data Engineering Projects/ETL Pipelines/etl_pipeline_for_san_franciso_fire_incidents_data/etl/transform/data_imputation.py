'''
    Data Imputation Module
'''
import pandas as pd

def impute_values_from_the_staged_dataset(staged_dataframe: pd.Dataframe) -> None:
    '''
        Data Imputation Function
    '''
    # Initializing a dictionary to store the imputed values per column name
    columns = list(staged_dataframe.keys())
    imputed_values = {}

    # Data imputation process by using dataframe and group of row-based extraction to optimize the data parsing
    for column in columns:
        data = {column: []}

        for row_number in range(0, 705908, 1000):
            data[column].extend(list(staged_dataframe[column][row_number : row_number + 1000]))
        
        # Checking if the values is a pure numerical value
        try:
            _ = pd.Series(data[column]).mean()

            
        # Getting the mode for the impute value because the value is not numeric
        except TypeError:
            impute_value = pd.Series(data[column].mode()[0])