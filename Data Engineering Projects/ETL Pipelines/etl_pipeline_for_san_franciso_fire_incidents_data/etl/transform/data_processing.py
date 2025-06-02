'''
    Data Processing Module
'''
import os
from glob import glob
import pandas as pd

def processing_extracted_data(subdirectory_path: str) -> None:
    '''
        Data Processing Function
    '''
    # Initializing target directory path
    target_directory_path = 'data/processed'
    target_subdirectory_path = f'{target_directory_path}/san_francisco_fire_incidents_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)

    if len(glob(f'{target_subdirectory_path}/*.csv')) > 0:
        return
    
    dataset_name = 'san_francisco_fire_incidents_data'
    total_datasets = len(glob(f'{subdirectory_path}/*.csv'))

    for dataset_number in range(1, total_datasets + 1):
        filepath = f'{subdirectory_path}/{dataset_name}({dataset_number}).csv'
        