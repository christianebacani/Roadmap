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
    
    # We can check the data if it's already extracted and integrated/staged, return None if yes
    if len(glob(f'{target_subdirectory_path}/*.csv')) > 0:
        return

    integrated_dataframe = pd.read_csv(f'{subdirectory_path}/san_francisco_fire_incidents_data(1).csv')
    total_datasets = len(glob(f'{subdirectory_path}/*.csv'))

    # Extract ingested datasets and integrate/stage it before transformation phase using pandas library and concat method
    for dataset_number in range(2, total_datasets + 1):
        ingested_dataframe = pd.read_csv(f'{subdirectory_path}/san_francisco_fire_incidents_data({dataset_number}).csv', encoding='cp1252')
        integrated_dataframe = pd.concat([integrated_dataframe, ingested_dataframe], ignore_index=True)

        print(f'Successfully integrated san_francisco_fire_incidents_data({dataset_number})')
    
    target_filepath = f'{target_subdirectory_path}/san_francisco_fire_incidents_integrated_data.csv'
    integrated_dataframe.to_csv(target_filepath, index=False)