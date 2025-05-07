'''
    Extract Module
'''
import os
import pandas as pd
from glob import glob

def extract_ingested_data(raw_datasets_dir_path: str) -> None:
    '''
        Extract function to extract and stage
        the datasets to stage datasets directory path
        for transformation processes
    '''
    stage_datasets_dir_path = 'data/stage'
    target_sub_dir_path = f'{stage_datasets_dir_path}/{raw_datasets_dir_path.replace('data/raw/', '')}'

    if not os.path.exists(target_sub_dir_path):
        os.makedirs(target_sub_dir_path)
    
    # We can return it already if the datasets are already extracted to prevent unnecessary processing of hundred thousands of rows which results of slower runtime
    if len(glob(f'{target_sub_dir_path}/*.csv')) == len(glob(f'{raw_datasets_dir_path}/*.csv')):
        return

    base_filename = raw_datasets_dir_path.replace('data/raw/', '')
    total_datasets = len(glob(f'{raw_datasets_dir_path}/*.csv'))
    
    # Glob function does not work when processing data in order that's why I use the datasets number from their filename to process datasets in order
    for dataset_num in range(1, total_datasets + 1):
        filepath = f'{raw_datasets_dir_path}/{base_filename}({dataset_num}).csv'
        ingested_dataframe = pd.read_csv(filepath, encoding='ISO-8859-1')

        target_filepath = f'{target_sub_dir_path}/{base_filename}({dataset_num}).csv'
        ingested_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully extracted and staged the {base_filename}({dataset_num}) from raw datasets directory path')