'''
    Data Ingestion Module
'''
import os
from glob import glob
import requests

def ingest_raw_data(api_endpoint: str, total_rows: int) -> None:
    '''
        Data Ingestion Function
    '''
    # Initializing target directory path
    target_directory_path = 'data/raw'
    target_subdirectory_path = f'{target_directory_path}/san_francisco_fire_incidents_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)
    
    # We can check the data if it's already ingested, return None if yes
    if len(glob(f'{target_subdirectory_path}/*.csv')) > 0:
        return
    
    dataset_name = 'san_francisco_fire_incidents_data'
    dataset_number = 0
    
    # Ingest data using API Endpoint with pagination using request library
    for offset in range(0, total_rows + 1, 1000):
        dataset_number += 1
        response = requests.get(f'{api_endpoint}?$limit=1000&$offset={offset}', timeout=300)
        target_filepath = f'{target_subdirectory_path}/{dataset_name}({dataset_number}).csv'

        with open(target_filepath, 'w') as f:
            f.write(response.text)
        
        f.close()
        print(f'Successfully ingested {dataset_name}({dataset_number}) dataset')