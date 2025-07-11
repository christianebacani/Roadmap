'''
    Ingest Module
'''
import os
import requests

def ingest_raw_data(api_endpoint: str, total_rows: int) -> None:
    '''
        Ingest Function
    '''
    # Create the target subdirectory path if it's not existed before data ingestion phase
    target_subdirectory_path = 'data/raw/san_francisco_budget_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)
    
    # Perform data ingestion process
    for dataset_number, offset in enumerate(range(0, total_rows + 1, 1000)):
        dataset_number += 1
        target_filepath = f'{target_subdirectory_path}/san_francisco_budget_data({dataset_number}).csv'

        response = requests.get(url=f'{api_endpoint}?$limit=1000&$offset={offset}', timeout=250)

        with open(target_filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)
        f.close()

        print(f'Successfully ingested san_francisco_budget_data({dataset_number}).csv')