'''
    Ingest Module
'''
import os
import requests
from glob import glob

def ingest_data_using_api(dataset_name: str, api_endpoint: str, total_rows: int) -> None:
    '''
        Ingest function to ingest data
        from API Endpoint and store the
        response data to the raw datasets
        directory path
    '''
    raw_datasets_dir_path = 'data/raw'
    target_subdir_path = f'{raw_datasets_dir_path}/{dataset_name}'
    
    if not os.path.exists(target_subdir_path):
        os.makedirs(target_subdir_path)

    # Check the total datasets per page (1000 rows per page of response data from API Request)
    total_datasets_per_page = total_rows // 1000
    
    if total_rows % 1000 != 0:
        total_datasets_per_page += 1
    
    # We can return it already if the datasets are already ingested to prevent unnecessary processing of hundred thousands of rows which results of slower runtime
    if len(glob(f'{target_subdir_path}/*.csv')) == total_datasets_per_page:
        return

    dataset_number = 0

    # Ingest data using API Endpoint and implementing pagination to store data into smaller components of datasets
    for offset in range(0, total_rows + 1, 1000):
        response = requests.get(url=f'{api_endpoint}?$limit=1000&$offset={offset}', timeout=250)
        dataset_number += 1

        target_filepath = f'{target_subdir_path}/{dataset_name}({dataset_number}).csv'

        with open(target_filepath, 'w') as f:
            f.write(response.text)
        
        f.close()

        print(f'Successfully ingested {dataset_name}({dataset_number}) dataset from API Endpoint')