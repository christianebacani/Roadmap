'''
    Data Integration Module
'''
from glob import glob
import pandas as pd

def integrate_datasets(directory_path: str) -> None:
    '''
        Data Integration Function
    '''
    total_number_of_datasets = len(glob(f'{directory_path}/*.csv'))

    # Perform data integration
    integrated_dataframe = pd.read_csv(f'{directory_path}/san_francisco_budget_data(1).csv')

    for dataset_number in range(2, total_number_of_datasets + 1):
        filepath = f'{directory_path}/san_francisco_budget_data({dataset_number}).csv'
        integrated_dataframe = pd.concat([integrated_dataframe, pd.read_csv(filepath)], ignore_index=False)
        
        print(f'Successfully perform data integration to san_francisco_budget_data({dataset_number}).csv')
    
    target_filepath = f'{directory_path}/san_francisco_integrated_budget_data.csv'
    integrated_dataframe.to_csv(target_filepath, index=False)
    print(f'Successfully perform data integration')