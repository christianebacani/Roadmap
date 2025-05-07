'''
    Transform Module
'''
import pandas as pd
from datetime import datetime
from transform.rename_column_names import rename_active_business_locs_in_san_francisco_dataset_columns
from transform.rename_column_names import rename_registered_business_locs_in_san_francisco_dataset_columns

def transform_active_business_locs_in_san_francisco_datasets(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        active_business_locs_in_san_francisco
        datasets
    '''
    # Renaming dataset columns using a function from different modules for modularity purposes
    renamed_dataframe = rename_active_business_locs_in_san_francisco_dataset_columns(staged_dataframe)

    # Initializing dictionary to store transformed data from dataframe because pd.concat() is much more slower
    columns = list(renamed_dataframe.keys())
    transformed_data = {}

    for i in range(len(columns)):
        transformed_data[columns[i]] = []
    
    # Transforming data per column and storing in a key of the initialized dictionary
    for _, row in renamed_dataframe.iterrows():
        transformed_data['location_id'].append(str(row.get('location_id')))
        transformed_data['business_account_number'].append(int(row.get('business_account_number')))
        
        ownership_name = str(row.get('ownership_name'))
        ownership_name_char_delimiters = ['/', '&']

        for i in range(len(ownership_name_char_delimiters)):
            ownership_name = ownership_name.replace(ownership_name_char_delimiters[i], ' ')
        
        transformed_data['ownership_name'].append(ownership_name)

        transformed_data['doing_business_as_name'].append(str(row.get('doing_business_as_name')))
        transformed_data['business_location_street_address'].append(str(row.get('business_location_street_address')))
        transformed_data['business_location_city'].append(str(row.get('business_location_city')))
        transformed_data['business_location_state'].append(str(row.get('business_location_state')))
        
        business_location_zip_code = str(row.get('business_location_zip_code'))
        
        if business_location_zip_code.lower() == 'nan':
            transformed_data['business_location_zip_code'].append(int(float(renamed_dataframe['business_location_zip_code'].median())))

        else:
            transformed_data['business_location_zip_code'].append(int(float(business_location_zip_code)))

        transformed_data['business_start_date'].append(datetime.strptime(str(row.get('business_start_date')).split('T')[0], '%Y-%m-%d').date())

        business_end_date = str(row.get('business_end_date'))

        if business_end_date.lower() == 'nan':
            transformed_data['business_end_date'].append(None)
        
        else:
            transformed_data['business_end_date'].append(datetime.strptime(business_end_date.split('T')[0], '%Y-%m-%d').date())
        
        transformed_data['location_start_date'].append(datetime.strptime(str(row.get('location_start_date')).split('T')[0], '%Y-%m-%d').date())

        location_end_date = str(row.get('location_end_date'))

        if location_end_date.lower() == 'nan':
            transformed_data['location_end_date'].append(None)
        
        else:
            transformed_data['location_end_date'].append(datetime.strptime(location_end_date.split('T')[0], '%Y-%m-%d').date())
        
        transformed_data['mailing_address'].append(str(row.get('mailing_address')))
    
    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop_duplicates(subset=['location_id', 'business_account_number'], inplace=True)

    return transformed_dataframe

def transform_registered_business_locs_in_san_francisco_datasets(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        registered_business_locs_in_san_francisco
        datasets
    '''
    # Renaming dataset columns using a function from different modules for modularity purposes
    renamed_dataframe = rename_registered_business_locs_in_san_francisco_dataset_columns(staged_dataframe)

    # Initializing dictionary to store transformed data from dataframe because pd.concat() is much more slower
    columns = list(renamed_dataframe.keys())
    transformed_data = {}

    for i in range(len(columns)):
        transformed_data[columns[i]] = []

    for _, row in renamed_dataframe.iterrows():
        transformed_data['unique_id'].append(str(row.get('unique_id')))
        transformed_data['location_id'].append(str(row.get('location_id')))
        transformed_data['business_account_number'].append(int(row.get('business_account_number')))
        transformed_data['ownership_name'].append(str(row.get('ownership_name')))
        transformed_data['doing_business_as_name'].append(str(row.get('doing_business_as_name')))
        transformed_data['business_location_street_address'].append(str(row.get('business_location_street_addres')))
        transformed_data['business_location_city'].append(str(row.get('business_location_city')))
        transformed_data['business_location_state'].append(str(row.get('business_location_state')))
        transformed_data['business_location_zip_code'].append(int(row.get('business_location_zip_code')))
        transformed_data['business_start_date'].append(datetime.strptime(str(row.get('business_start_date')).split('T')[0], '%Y-%m-%d'))
        
        business_end_date = str(row.get('business_end_date'))

        if business_end_date.lower() == 'nan':
            transformed_data['business_end_date'].append(None)
        
        else:
            transformed_data['business_end_date'].append(datetime.strptime(business_end_date.split('T')[0], '%Y-%m-%d'))
        
        transformed_data['location_start_date'].append(datetime.strptime(str(row.get('location_start_date')).split('T')[0], '%Y-%m-%d'))
        
        location_end_date = str(row.get('location_end_date'))

        if location_end_date.lower() == 'nan':
            transformed_data['location_end_date'].append(None)
        
        else:
            transformed_data['location_end_date'].append(datetime.strptime(location_end_date.split('T')[0], '%Y-%m-%d'))
        
        is_administratively_closed = str(row.get('is_administratively_closed'))

        if is_administratively_closed.lower() == 'nan':
            transformed_data['is_administratively_closed'].append(False)
        
        else:
            transformed_data['is_administratively_closed'].append(True)
        
        transformed_data['mailing_address'].append(str(row.get('mailing_address', str(renamed_dataframe['mailing_address'].mode()[0]))))
        transformed_data['mailing_address_city'].append(str(row.get('mailing_address_city'), str(renamed_dataframe['mailing_address_city'].mode()[0])))
        transformed_data['mailing_address_zipcode'].append(int(row.get('mailing_address_zipcode', int(renamed_dataframe['mailing_address_zipcode'].median()))))
        transformed_data['mailing_address_state'].append(str(row.get('mailing_address_state'), str(renamed_dataframe['mailing_address_state'].mode()[0])))
        transformed_data['north_american_industry_classification_code'].append(str(row.get('north_american_industry_classification_code'), str(renamed_dataframe['north_american_industry_classification_code'].mode()[0])))
        transformed_data['naic_code_description'].append(str(row.get('naic_code_description'), str(renamed_dataframe['naic_code_description'].mode()[0])))
        transformed_data['naic_code_descriptions_list'].append(str(row.get('naic_code_descriptions_list'), str(renamed_dataframe['naic_code_descriptions_list'].mode()[0])))
        transformed_data['is_business_paying_parking_tax'].append(bool(row.get('is_business_paying_parking_tax')))
        transformed_data['is_business_paying_transient_occupancy_tax'].append(bool(row.get('is_business_paying_transient_occupancy_tax')))
        transformed_data['life_insurance_corporation_code'].append(str(row.get('life_insurance_corporation_code'), str(renamed_dataframe['life_insurance_corporation_code'].mode()[0])))
        transformed_data['lic_code_description'].append(str(row.get('lic_code_description'), str(renamed_dataframe['lic_code_description'].mode()[0])))
        
