'''
    Field Name Modification Module
'''
import pandas as pd

def modify_field_names_of_active_business_locs_in_sf_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Modify function to modify field/attribute names of
        active_business_locs_in_san_francisco dataset
    '''
    # Inplace modification is much more faster rather than creating new instances
    staged_dataframe.rename(columns={
        'ttxid': 'location_id',
        'certificate_number': 'business_account_number',
        'dba_name': 'doing_business_as_name',
        'full_business_address': 'business_loc_street_address',
        'city': 'business_loc_city',
        'state': 'business_loc_state',
        'business_zip': 'business_loc_zipcode',
        'dba_start_date': 'start_date_of_business',
        'dba_end_date': 'end_date_of_business',
        'location_start_date': 'start_date_at_the_loc',
        'location_end_date': 'end_date_at_the_loc',
        'mailing_address_1': 'mailing_address'
    }, inplace=True)

    return staged_dataframe