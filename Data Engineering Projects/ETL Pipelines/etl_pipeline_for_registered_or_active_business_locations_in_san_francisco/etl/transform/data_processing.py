'''
    Data Processing Module
'''
import os
import pandas as pd
from glob import glob
from transform.transform import transform_active_business_locs_in_san_francisco_datasets
from transform.transform import transform_registered_business_locs_in_san_francisco_datasets

def processing_staged_datasets(staged_datasets_dir_path: str) -> None:
    '''
        Process function to process
        staged datasets from staged datasets
        directory path
    '''
    processed_datasets_dir_path = 'data/processed'
    target_subdir_path = f'{processed_datasets_dir_path}/{staged_datasets_dir_path.replace('data/stage/', '')}'

    if not os.path.exists(target_subdir_path):
        os.makedirs(target_subdir_path)

    # We can return it already if the datasets are already processed for transformation to prevent unnecessary processing of hundred thousands of rows which results of slower runtime
    if len(glob(f'{target_subdir_path}/*.csv')) == len(glob(f'{staged_datasets_dir_path}/*.csv')):
        return

    base_filename = staged_datasets_dir_path.replace('data/stage/', '')
    total_datasets = len(glob(f'{staged_datasets_dir_path}/*.csv'))

    # Glob function does not work when processing data in order that's why I use the datasets number from their filename to process datasets in order
    for dataset_num in range(1, total_datasets + 1):
        filepath = f'{staged_datasets_dir_path}/{base_filename}({dataset_num}).csv'
        staged_dataframe = pd.read_csv(filepath, encoding='ISO-8859-1')

        if base_filename == 'active_business_locs_in_san_francisco':
            transformed_dataframe = transform_active_business_locs_in_san_francisco_datasets(staged_dataframe)
            target_filepath = f'{target_subdir_path}/{base_filename}({dataset_num}).csv'
            transformed_dataframe.to_csv(target_filepath, index=False)
            
            print(f'Successfully transformed {base_filename}({dataset_num}) dataset from stage datasets directory path')

        else:
            transformed_dataframe = transform_registered_business_locs_in_san_francisco_datasets(staged_dataframe)
            