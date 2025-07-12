'''
    Transform Module
'''
import os
from glob import glob
import pandas as pd
from transform.data_imputation import impute_missing_values

def transform_extracted_datasets(subdirectory_path: str) -> None:
    '''
        Transform Function
    '''
    # Get the total number of staged datasets
    total_number_of_datasets = 0

    for csv_file in glob(f'{subdirectory_path}/*.csv'):
        base_filename = str(csv_file).replace('data/staged/san_francisco_budget_data\\', '')
        base_filename = base_filename.replace('.csv', '')

        if base_filename != 'san_francisco_integrated_budget_data':
            total_number_of_datasets += 1
    
    # TODO: Implement a function here from other module for performing data integration phase

    # Remove staged datasets after data integration phase
    for dataset_number in range(1, total_number_of_datasets + 1):
        filepath = f'data/staged/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'

        if os.path.exists(filepath):
            os.remove(filepath)
            print(f'Successfully removed san_francisco_budget_data({dataset_number}).csv staged dataset')

    # Perform data imputation phase
    target_filepath = f'data/staged/san_francisco_budget_data/san_francisco_integrated_budget_data.csv'
    integrated_dataframe = impute_missing_values(pd.read_csv(f'{subdirectory_path}/san_francisco_integrated_budget_data.csv', low_memory=False))
    integrated_dataframe.to_csv(target_filepath, index=False)
    print(f'Successfully perform data imputation')

