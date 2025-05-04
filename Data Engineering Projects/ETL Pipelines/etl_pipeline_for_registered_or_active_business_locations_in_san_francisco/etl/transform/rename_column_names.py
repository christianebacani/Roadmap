'''
    Rename Column Names Module
'''
import pandas as pd

def rename_active_business_locs_in_san_francisco_dataset_columns(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        active_business_locs_in_san_francisco
        dataset columns
    '''
    staged_dataframe.rename(columns={
        'ttxid': 'location_id',
        'certificate_number': 'business_account_number',
        'dba_name': 'doing_business_as_name',
        'full_business_address': 'business_location_street_address',
        'city': 'business_location_city',
        'state': 'business_location_state',
        'business_zip': 'business_location_zip_code',
        'dba_start_date': 'business_start_date',
        'dba_end_date': 'business_end_date',
        'mailing_address_1': 'mailing_address'
    }, inplace=True)
    
    return staged_dataframe