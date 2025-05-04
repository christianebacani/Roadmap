'''
    Data Validation Module
'''
import pandas as pd

def validate_active_business_locs_in_san_francisco_datasets(transformed_dataframe: pd.Dataframe) -> None:
    '''
        Validate function to validate
        active_business_locs_in_san_francisco
        datasets
    '''
    columns = list(transformed_dataframe.keys())
    columns_with_integer_values = [
        'location_id', 
        'business_account_number', 
        'business_location_zip_code'
    ]
    columns_with_string_values = [
        'ownership_name', 
        'doing_business_as_name', 
        'business_location_street_address',
        'business_location_city',
        'business_location_state',
        'mailing_address'
    ]
    