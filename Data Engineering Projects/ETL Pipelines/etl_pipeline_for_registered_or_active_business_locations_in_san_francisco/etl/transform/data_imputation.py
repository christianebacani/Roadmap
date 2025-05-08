'''
    Data Imputation Module
'''
import pandas as pd
from datetime import datetime

def impute_data_of_active_business_locs_in_sf_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Impute Data function to impute data
        if the value consist of null/none/nan value
        from active_business_locs_in_san_francisco
        dataset
    '''
    columns = list(staged_dataframe.keys())
    
    columns_with_string_value = [
        'location_id',
        'ownership_name',
        'doing_business_as_name',
        'business_loc_street_address',
        'business_loc_city',
        'business_loc_state',
        'mailing_address'
    ]
    columns_with_date_value = [
        'start_date_of_business',
        'end_date_of_business',
        'start_date_at_the_loc',
        'end_date_at_the_loc'
    ]

    # Initializing dictionary that maps to a imputed value because it is much faster to call a key with a correspoding imputed value
    column_and_imputed_value = {}
    
    for i in range(len(columns)):
        column_and_imputed_value[columns[i]] = None
    
    for column in columns:
        values = []

        for value in staged_dataframe[column]:
            if str(value).lower() == 'nan':
                continue

            if (column in columns_with_string_value) or (column in columns_with_date_value):
                values.append(str(value))
            
            else:
                values.append(int(value))
        
        if len(values) == 0:
            continue

        if (column in columns_with_string_value) or (column in columns_with_date_value):
            column_and_imputed_value[column] = str(pd.Series(values).mode()[0])

        else:
            column_and_imputed_value[column] = int(pd.Series(values).median())
    
    # Initializing a dictionary to store data that is imputed for faster processing of large data
    data = {}

    for i in range(len(columns)):
        data[columns[i]] = []
    
    for _, row in staged_dataframe.iterrows():
        for column in columns:
            value = row.get(column, column_and_imputed_value[column])
            data[column].append(value)

    df = pd.DataFrame(data)
    
    return df