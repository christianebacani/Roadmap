'''
    Format Revision Module
'''
import pandas as pd
from glob import glob

def revise_dataset_format() -> None:
    '''
        Format Revision Function
    '''
    # Perform format revision
    total_number_of_datasets = len(glob(f'data/staged/san_francisco_budget_data/*.csv'))
    
    for dataset_number in range(1, total_number_of_datasets + 1):
        filepath = f'data/staged/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'
        partitioned_dataframe = pd.read_csv(filepath)