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
    # Inplace modification is much more optimized for bigger datasets
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

def rename_registered_business_locs_in_san_francisco_dataset_columns(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        registered_business_locs_in_san_francisco
        dataset columns
    '''
    # Inplace modification is much more optimized for bigger datasets
    staged_dataframe.rename(columns={
        'uniqueid': 'unique_id',
        'ttxid': 'location_id',
        'certificate_number': 'business_account_number',
        'dba_name': 'doing_business_as_name',
        'full_business_address': 'business_location_street_address',
        'city': 'business_location_city',
        'state': 'business_location_state',
        'business_zip': 'business_location_zip_code',
        'dba_start_date': 'business_start_date',
        'dba_end_date': 'business_end_date',
        'administratively_closed': 'is_administratively_closed',
        'mailing_address_1': 'mailing_address',
        'mail_city': 'mailing_address_city',
        'mail_zipcode': 'mailing_address_zipcode',
        'mail_state': 'mailing_address_state',
        'naic_code': 'north_american_industry_classification_code',
        'naics_code_descriptions_list': 'naic_code_descriptions_list',
        'parking_tax': 'is_business_paying_parking_tax',
        'transient_occupancy_tax': 'is_business_paying_transient_occupancy_tax',
        'lic': 'life_insurance_corporation_code',
        'location': 'business_location'
    }, inplace=True)

    staged_dataframe.drop(columns=[
        'data_as_of',
        'data_loaded_at',
        ':@computed_region_6qbp_sg9q',
        ':@computed_region_qgnn_b9vv',
        ':@computed_region_26cr_cadq',
        ':@computed_region_ajp5_b2md',
        ':@computed_region_jwn9_ihcz'
    ], inplace=True)
    
    return staged_dataframe