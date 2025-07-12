'''
    Transform Module
'''
import os
import pandas as pd
from glob import glob
from transform.data_integration import integrate_datasets
from transform.dataset_deletion import remove_unnecessary_datasets
from transform.data_imputation import impute_missing_values
from transform.data_partition import partition

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
    
    # Data integration phase
    integrate_datasets(total_number_of_datasets)
    
    # Dataset deletion phase
    remove_unnecessary_datasets(total_number_of_datasets)

    # Data imputation phase
    target_filepath = f'data/staged/san_francisco_budget_data/san_francisco_integrated_budget_data.csv'
    integrated_dataframe = impute_missing_values(pd.read_csv(f'{subdirectory_path}/san_francisco_integrated_budget_data.csv', low_memory=False))
    integrated_dataframe.to_csv(target_filepath, index=False)
    print(f'Successfully perform data imputation')

    # Data partition phase
    partition(pd.read_csv(f'{subdirectory_path}/san_francisco_integrated_budget_data.csv', low_memory=False))
    print(f'Successfully perform data partitioning')