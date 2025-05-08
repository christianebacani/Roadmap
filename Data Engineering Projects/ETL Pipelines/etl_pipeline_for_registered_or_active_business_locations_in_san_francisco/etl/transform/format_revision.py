'''
    Format Revision Module
'''
import pandas as pd

def revise_format_of_active_business_locs_in_sf_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Revise format function to revise
        the format of the values of the data from
        active_business_locs_in_san_francisco dataset
    '''
    columns = list(staged_dataframe.keys())

    # Initializing a dictionary to map the values from the dataframe for faster processing
    data = {}

    for i in range(len(columns)):
        data[columns[i]] = []
    
    for _, row in staged_dataframe.iterrows():
        data['location_id'].append(str(row.get('location_id')))
        data['business_account_number'].append(int(row.get('business_account_number')))
        data['ownership_name'].append(str(row.get('ownership_name')))
        data['doing_business_as_name'].append(str(row.get('doing_business_as_name')))
        data['business_loc_street_address'].append(str(row.get('business_loc_street_address')))