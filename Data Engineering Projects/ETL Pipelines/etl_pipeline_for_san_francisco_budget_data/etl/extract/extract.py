'''
    Extract Module
'''
import os
from glob import glob
import pandas as pd

def extract_ingested_datasets(subdirectory_path: str) -> None:
    '''
        Extract Function
    '''
    # Create the target subdirectory path if it's not existed before data ingestion phase
    target_subdirectory_path = 'data/stage/san_francisco_budget_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)
    
    total_number_of_datasets = len(glob(f'{subdirectory_path}/*.csv'))

    # Perform extraction process for ingested datasets
    for dataset_number in range(1, total_number_of_datasets + 1):
        filepath = f'{subdirectory_path}/san_francisco_budget_data({dataset_number}).csv'
        ingested_dataframe = pd.read_csv(filepath)

        target_filepath = f'{target_subdirectory_path}/san_francisco_budget_data({dataset_number}).csv'
        ingested_dataframe.to_csv(target_filepath, index=False)
        
        print(f'Successfully extracted san_francisco_fire_incidents_data({dataset_number}).csv ingested dataset')