'''
    Extract Module
'''
import os
import pandas as pd
from glob import glob

def extract_raw_datasets(raw_subdir_path: str) -> None:
    '''
        Extract function to extract and staged
        all the raw datasets from all sub-directory 
        path of raw datasets directory
    '''
    stage_datasets_dir_path = 'data/stage'
    target_subdir_path = f'{stage_datasets_dir_path}/{raw_subdir_path.replace('data/raw/', '')}'

    if not os.path.exists(target_subdir_path):
        os.makedirs(target_subdir_path)
    
    if len(glob(f'{target_subdir_path}/*.csv')) > 0:
        return

    for csv_file in glob(f'{raw_subdir_path}/*.csv'):
        filename = str(csv_file).replace(f'{raw_subdir_path}\\', '')
        target_filepath = f'{target_subdir_path}/{filename}'

        raw_dataset = pd.read_csv(csv_file, encoding='cp1252')
        raw_dataset.to_csv(target_filepath, index=False)
        
        print(f'Successfully staged {filename} dataset from raw dataset directory path')