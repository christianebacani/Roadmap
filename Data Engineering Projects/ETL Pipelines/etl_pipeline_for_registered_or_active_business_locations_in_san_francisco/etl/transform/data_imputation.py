'''
    Data Imputation
'''
import pandas as pd

def impute_data_from_active_business_locs_in_sf_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
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
        'busines_loc_street_address',
        'business_loc_city',
        'business_loc_state',
        'mailing_address'
    ]
    columns_with_integer_value = [
        'business_account_number',
        'business_loc_zipcode'
    ]

    column_and_imputed_value = {}
    
    for i in range(len(columns)):
        column_and_imputed_value[columns[i]] = None

    for column in columns:
        values = []

        for value in staged_dataframe[column]:
            if str(value).lower() != 'nan':
                values.append(value)
        
        if column in columns_with_string_value:
            column_and_imputed_value[column] = str(pd.Series(values).mode()[0])
        
        elif column in columns_with_integer_value:
            column_and_imputed_value[column] = int(pd.Series(values).median())

        else:
            pass

    data = {}

    for i in range(len(columns)):
        data[columns[i]] = []

    for _, row in staged_dataframe.iterrows():
        location_id = str(row.get('location_id')).lower()
        location_id = location_id.replace('nan', column_and_imputed_value['location_id'])
        data['location_id'].append(location_id)
        
        business_account_number = str(row.get('business_account_number')).lower()
        business_account_number = int(business_account_number.replace('nan', str(column_and_imputed_value['business_account_number'])))
        data['business_account_number'].append(business_account_number)

        ownership_name = str(row.get('ownership_name')).lower()
        ownership_name = ownership_name.replace('nan', column_and_imputed_value['ownership_name'])
        data['ownership_name'].append(ownership_name)

        doing_business_as_name = str(row.get('doing_business_as_name')).lower()
        doing_business_as_name = doing_business_as_name.replace('nan', column_and_imputed_value['doing_business_as_name'])
        data['doing_business_as_name'].append(doing_business_as_name)

        business_loc_street_address = str(row.get('business_loc_street_address')).lower()
        business_loc_street_address = business_loc_street_address.replace('nan', column_and_imputed_value['business_loc_street_address'])
        data['business_loc_street_address'].append(business_loc_street_address)