'''
    Data Imputation Module
'''
import pandas as pd
from datetime import datetime

def impute_missing_values(integrated_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Imputation Function
    '''
    # Initialized the columns of the integrated dataset
    columns = list(integrated_dataframe.keys())
    
    # Get the distinct values of every column
    column_and_distinct_values = {}
    
    for column in columns:
        distinct_values = list(set(integrated_dataframe[column]))
        column_and_distinct_values[column] = distinct_values

    # Get the data type of every column
    column_and_data_type = {}

    for column, distinct_values in column_and_distinct_values.items():
        data_type_and_frequencies = {
            'nan': 0,
            'datetime': 0,
            'string': 0,
            'integer': 0,
            'float': 0
        }
        
        for value in distinct_values:
            if str(value).lower() == 'nan':
                data_type_and_frequencies['nan'] = data_type_and_frequencies['nan'] + 1
                continue
            
            try:
                datetime.strptime(str(value), '%Y-%m-%d %H:%M:%S.%f')
                data_type_and_frequencies['datetime'] = data_type_and_frequencies['datetime'] + 1
                continue

            except:
                pass
            
            if str(value).isdigit():
                data_type_and_frequencies['integer'] = data_type_and_frequencies['integer'] + 1
                continue

            try:
                float(value)
                data_type_and_frequencies['float'] = data_type_and_frequencies['float'] + 1
            
            except:
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
            
    # Get the imputed value of every column
    column_and_imputed_value = {}

    for column in columns:
        if column_and_data_type[column] == 'nan':
            imputed_value = pd.NA
        
        elif column_and_data_type[column] in ['datetime', 'string']:
            imputed_value = integrated_dataframe[column].mode()[0]

        elif integrated_dataframe[column].skew() >= -0.5 and integrated_dataframe[column].skew() <= 0.5:
            imputed_value = integrated_dataframe[column].mean()

        else:
            imputed_value = integrated_dataframe[column].median()
        
        if column in ['fiscal_year', 'organization_group_code', 'budget']:
            imputed_value = int(imputed_value)

        column_and_imputed_value[column] = imputed_value

    for column in columns:
        imputed_value = column_and_imputed_value[column]
        integrated_dataframe[column] = integrated_dataframe[column].fillna(imputed_value)

    return integrated_dataframe