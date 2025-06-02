'''
    Data Extraction/Staging Module
'''
import os
from glob import glob
import pandas as pd

def extract_ingested_data(subdirectory_path: str) -> None:
    '''
        Data Extraction/Staging Function
    '''
    # Initializing target directory path
    target_directory_path = 'data/stage'
    target_subdirectory_path = f'{target_directory_path}/san_francisco_fire_incidents_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)
    
    # We can check the data if it's already ingested, return None if yes
    if len(glob(f'{target_subdirectory_path}/*.csv')) > 0:
        return
    
    dataset_name = 'san_francisco_fire_incidents_data'
    total_datasets = len(glob(f'{subdirectory_path}/*.csv'))

    # Extract/Ingest data to be ready for transformation phase using pandas library
    for dataset_number in range(1, total_datasets + 1):
        filepath = f'{subdirectory_path}/{dataset_name}({dataset_number}).csv'
        ingested_dataframe = pd.read_csv(filepath, encoding='cp1252')
        
        target_filepath = f'{target_subdirectory_path}/{dataset_name}({dataset_number}).csv'
        ingested_dataframe.to_csv(target_filepath, index=False)
        print(f'Successfully extracted/staged {dataset_name}({dataset_number}) dataset')