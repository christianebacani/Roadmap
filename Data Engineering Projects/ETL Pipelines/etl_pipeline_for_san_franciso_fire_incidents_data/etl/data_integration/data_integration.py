'''
    Data Integration Module
'''
import pandas as pd
from glob import glob

def integrate_processed_datasets() -> None:
    '''
        Data Integration Function 
    '''
    # Initialize a directory path to store integrated dataset/s
    target_directory_path = 'data/integrated_datasets'

    if len(glob(f'{target_directory_path}/*.csv')) > 0:
        return
    
    # Data Integration Process using glob function
    subdirectory_path = f'data/processed/san_francisco_fire_incidents_data'
    integrated_dataframe = pd.read_csv(f'{subdirectory_path}/san_francisco_fire_incidents_data(1).csv')

    total_datasets = len(glob(f'{subdirectory_path}/*.csv'))

    for dataset_number in range(2, total_datasets + 1):
        base_filename = f'san_francisco_fire_incidents_data({dataset_number}).csv'
        target_filepath = f'{subdirectory_path}/{base_filename}'
        integrated_dataframe = pd.concat([integrated_dataframe, pd.read_csv(target_filepath)], ignore_index=True)

        print(f'Successfully integrate {base_filename}')
    
    integrated_dataframe.to_csv(f'{target_directory_path}/san_francisco_fire_incidents_integrated_data.csv', index=False)