'''
    Transform Module
'''
import os
from glob import glob
import pandas as pd
from transform.data_imputation import impute_missing_values

def transform_extracted_datasets(subdirectory_path: str) -> None:
    '''
        Transform Function
    '''
    # Create the target subdirectory path if it's not existed before data ingestion phase
    target_subdirectory_path = f'data/processed/san_francisco_budget_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)

    # Perform data integration before data imputation phase
    total_number_of_datasets = len(glob(f'{subdirectory_path}/*.csv'))
    integrated_dataframe = pd.read_csv(f'data/staged/san_francisco_budget_data/san_francisco_budget_data(1).csv')

    for dataset_number in range(2, total_number_of_datasets + 1):
        filepath = f'data/staged/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'
        integrated_dataframe = pd.concat([integrated_dataframe, pd.read_csv(filepath)], ignore_index=True)
        
        print(f'Successfully integrate san_francisco_budget_data({dataset_number}).csv to the integrated dataset')
    
    target_filepath = f'{subdirectory_path}/san_francisco_integrated_budget_data.csv'
    integrated_dataframe.to_csv(target_filepath, index=False)
    print(f'Successfully perform data integration')

    # Remove staged datasets after data integration phase
    for dataset_number in range(1, total_number_of_datasets + 1):
        filepath = f'data/staged/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'

        if os.path.exists(filepath):
            os.remove(filepath)
            print(f'Successfully removed san_francisco_budget_data({dataset_number}).csv staged dataset')

    # Perform data imputation phase
    impute_missing_values(pd.read_csv(f'{subdirectory_path}/san_francisco_integrated_budget_data.csv'))    