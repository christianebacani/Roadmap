'''
    Transforming summary statistics staged datasets
'''
from glob import glob
import os
import pandas as pd
from transform.rename_columns import rename_dataset_columns
from transform.clean_datasets import clean_staged_datasets

def transform(staged_datasets_subdir: str, staged_datasets_subdir_name: str) -> None:
    '''
        Transformation function to transform summary statistics staged datasets
    '''
    processed_dir = 'ETL Pipeline for Philippine PSA Summary Statistics/data/processed'
    transformed_datasets = {}

    # Glob function to iterate over the sequence of sub-directory path and reading the datasets using pandas
    for dataset in glob(f'{staged_datasets_subdir}/*.csv'):
        dataset_lst = str(dataset).split(f'\\{staged_datasets_subdir_name}\\')
        base_filename = dataset_lst[1].replace('.csv', '')
        staged_dataframe = pd.read_csv(dataset)

        # We can combined the 2 functions for cleaning and renaming datasets into one line for better readability
        staged_dataframe = clean_staged_datasets(rename_dataset_columns(staged_dataframe))
        
        # Mapped again to the dictionary to provide the filename also as a key
        filename = f'{base_filename}.csv'
        transformed_datasets[filename] = staged_dataframe

    # Using os routine again to check if the target directory path are already exists
    target_processed_subdir = f'{processed_dir}/{staged_datasets_subdir_name}'
    
    if not os.path.exists(target_processed_subdir):
        os.makedirs(target_processed_subdir)

    # For loop to get the filename key and store the dataframe to the filename key with target directory path
    for filename, dataframe in transformed_datasets.items():
        filepath = f'{target_processed_subdir}/{filename}'
        dataframe.to_csv(filepath, index=False)
        
        staged_datasets_subdir_name = staged_datasets_subdir_name.replace('_', ' ')
        print(f'Successfully processed {filename.replace('.csv', '')} from {staged_datasets_subdir_name} datasets')
