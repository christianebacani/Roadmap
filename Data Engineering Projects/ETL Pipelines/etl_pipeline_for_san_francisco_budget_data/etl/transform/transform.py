'''
    Transform Module
'''
import os
from glob import glob

def transform_extracted_datasets(subdirectory_path: str) -> None:
    '''
        Transform Function
    '''
    # Create the target subdirectory path if it's not existed before data ingestion phase
    target_subdirectory_path = f'data/processed/san_francisco_budget_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)

    total_number_of_datasets = len(glob(f'{subdirectory_path}/*.csv'))

    # TODO: Implement more functionalities here...