'''
    Ingest Module
'''
import requests
import os
from glob import glob

def ingest_data_using_rest_api(dataset_name: str, api_endpoint: str, total_rows: int) -> None:
    '''
        Ingest function to ingest
        data using REST API
    '''
    raw_datasets_dir_path = 'data/raw'
    target_subdir_path = f'{raw_datasets_dir_path}/{dataset_name}'

    if not os.path.exists(target_subdir_path):
        os.makedirs(target_subdir_path)
    
    if len(glob(f'{target_subdir_path}/*.csv')) > 0:
        return

    index = 0

    for offset in range(0, total_rows + 1, 1000):
        index += 1
        response = requests.get(f'{api_endpoint}?$limit=1000&$offset={offset}', timeout=250)
        
        target_filepath = f'{target_subdir_path}/{dataset_name}({index}).csv'

        with open(target_filepath, 'w') as f:
            f.write(response.text)
        
        f.close()
        print(f'Successfully ingested {dataset_name}({index}) dataset from API Endpoint')