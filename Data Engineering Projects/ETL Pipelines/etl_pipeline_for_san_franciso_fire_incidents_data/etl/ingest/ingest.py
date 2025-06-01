'''
    Data Ingestion Module
'''
import os

def ingest_raw_data(api_endpoint: str, total_rows: int) -> None:
    '''
        Data Ingestion Function
    '''
    target_directory_path = 'data/raw'
    target_subdirectory_path = f'{target_directory_path}/san_francisco_fire_incidents_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)
    
    # TODO: Implement more functionalities here...