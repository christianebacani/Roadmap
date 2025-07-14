'''
    Format Revision Module
'''
import pandas as pd
from glob import glob

def revise_the_value_format_of_department_column(value: str) -> str:
    '''
        Format revision function for department column of
        san francisco budget datasets
    '''
    # Initialize a dictionary that stores the old value of department column as a key and the new standardized format value as a pair of the key
    new_values = {
        # C
        'CCD SF Communtiy College Dist': 'CCD SF Community College District',
        'CFC Children & Families Commsn': 'CFC Children & Families Commission',
        'CHF Children;Youth & Families': 'CHF Children/Youth & Families',
        'CII Commty Invest & Infrstrctr': 'CII Commity Invest & Infrastructure',
        'CTA SF County Transprtn Auth': 'CTA SF County Transportation Authority',
        
        # D
        'DEC Dept of Early Childhood': 'DEC Department of Early Childhood',\
        'DT  GSA - Technology': 'DT GSA - Technology',
        
        # E
        'ECN Economic & Wrkfrce Dvlpmnt': 'ECN Economic & Workforce Development',

        # G
        'General Services Agency - City Admin': 'General Services Agency - City Admininistration',

        # M
        'MTA Municipal Transprtn Agncy': 'MTA Municipal Transportation Agency',

        # P
        'PUC Public Utilities Commsn': 'PUC Public Utilities Commission',

        # R
        'REC Recreation & Park Commsn': 'REC Recreation & Park Commission',

        # S
        'SAS Dept of Sanitation & Sts': 'SAS Department of Sanitation & Streets',
        'SDA Shrf Dept Ofc Inspctr Genl': 'San Francisco Sheriff\'s Department Office of the Inspector General.',
        
        # T
        'TJP Transbay Joint Power Auth': 'TJP Transbay Joint Power Authority'
    }

    if value in new_values:
        value = new_values[value]
    
    return value

def revise_the_value_format_of_object_column(value: str) -> str:
    '''
        Format revision function for object column of
        san francisco budget datasets
    '''
    # TODO: Add more key and value pair from the dictionary to revise the value format of the object column
    new_values = {
        # E
        'ELIMUC TRANSFER ADJ-USES CITY': 'Elimination/Transfer Adjustment – Uses – City',

        # G
        'GF-Adm Grants For The Arts': 'General Fund – Administration: Grants for the Arts',
        'GF-HR-Workers\' Comp Claims': 'General Fund – Human Resources – Workers\' Compensation Claims',

        # H
        'HlthSvcFnd-HMO/Dental/Disab': 'Health Service Fund - HMO / Dental / Disability',
        
        # I
        'ITI Fr 2S/LIB-Public LibraryFd': 'Interfund Transfer from 2S Fund / Library – Public Library Fund',
        'ITI Fr 5P-Port of SanFrancisco': 'Interfund Transfer In from Fund 5P – Port of San Francisco',
        
        # R
        'Rec & Park Service Charges': 'Recreation and Parks Service Charges',
        
        # S
        'Services of Other Depts (AAO Funds)': 'Services of Other Departmentts (AAO Funds)',
        'SFO - Advertising: Tele & Othe': 'San Francisco Office - Advertising: Television & Other'
    }

def revise_dataset_format() -> None:
    '''
        Format Revision Function
    '''
    # Perform format revision
    total_number_of_datasets = len(glob(f'data/staged/san_francisco_budget_data/*.csv'))
    
    for dataset_number in range(1, total_number_of_datasets + 1):
        filepath = f'data/staged/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'
        partitioned_dataframe = pd.read_csv(filepath)

        # Initialize the dictionary that stores formatted values of every column
        columns = list(partitioned_dataframe.keys())
        data = {}

        for column in columns:
            data[column] = []
        
        for _, row in partitioned_dataframe.iterrows():
            for column in columns:
                value = row.get(column)

                if str(value).lower() == 'nan':
                    data[column].append(value)
                    continue

                if column == 'department':
                    data[column].append(revise_the_value_format_of_department_column(value))
                
                else:
                    data[column].append(value)

        target_filepath = filepath
        format_revised_dataframe = pd.DataFrame(data)
        format_revised_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully perform format revisioning to san_francisco_budget_data({dataset_number}).csv dataset')
    
    print('Successfully perform format revisioning')