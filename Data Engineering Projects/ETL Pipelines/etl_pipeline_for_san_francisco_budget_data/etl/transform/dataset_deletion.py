'''
    Dataset Deletion Module
'''
from glob import glob
import os

def remove_unnecessary_datasets(directory_path: str) -> None:
    '''
        Dataset Deletion Function
    '''
    # Get the total number of datasets from the staged directory path (excluding the integrated dataset)
    total_number_of_datasets = 0

    for csv_file in glob(f'{directory_path}/*.csv'):
        base_filename = str(csv_file).replace('data/staged/san_francisco_budget_data\\', '')
        base_filename = base_filename.replace('.csv', '')
        
        if base_filename != 'san_francisco_integrated_budget_data':
            total_number_of_datasets += 1

    # Perform dataset deletion
    for dataset_number in range(1, total_number_of_datasets + 1):
        filepath = f'{directory_path}/san_francisco_budget_data({dataset_number}).csv'

        if os.path.exists(filepath):
            os.remove(filepath)
            print(f'Successfully removed san_francisco_budget_data({dataset_number}).csv')

    print(f'Successfully deleted staged datasets after data integration')