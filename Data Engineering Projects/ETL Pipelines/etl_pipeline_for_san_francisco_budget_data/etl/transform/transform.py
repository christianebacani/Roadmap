'''
    Transform Module
'''
import pandas as pd
import os
from transform.data_integration import integrate_datasets
from transform.dataset_deletion import remove_unnecessary_datasets
from transform.data_imputation import impute_missing_values
from transform.data_partition import partition
from transform.datatype_cast import cast_datatype
from transform.format_revision import revise_dataset_format
from transform.data_deduplication import deduplicate_dataset

def transform_extracted_datasets(subdirectory_path: str) -> None:
    '''
        Transform Function
    '''
    # Data integration phase
    integrate_datasets(subdirectory_path)

    # Dataset deletion phase
    remove_unnecessary_datasets(subdirectory_path)

    # Data imputation phase
    dataframe = pd.read_csv(f'{subdirectory_path}/san_francisco_integrated_budget_data.csv', low_memory=False)
    impute_missing_values(dataframe)

    # Data partition phase
    partition(dataframe)

    # Remove integrated dataset from the directory
    if os.path.exists('data/staged/san_francisco_budget_data/san_francisco_integrated_budget_data.csv'):
        os.remove('data/staged/san_francisco_budget_data/san_francisco_integrated_budget_data.csv')
    
    # Dataype casting phase
    cast_datatype()

    # Format revisioning phase
    revise_dataset_format()

    # Data integration phase
    integrate_datasets(subdirectory_path)
    
    # Dataset deletion phase
    remove_unnecessary_datasets(subdirectory_path)

    # Data deduplication phase
    sf_integrated_budget_dataset = pd.read_csv('data/staged/san_francisco_budget_data/san_francisco_integrated_budget_data.csv', low_memory=False)
    sf_integrated_budget_dataset = deduplicate_dataset(sf_integrated_budget_dataset)

    # Initialize the directory path to store the transform dataset
    target_subdirectory_path = f'data/processed/san_francisco_budget_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)

    # Load transformed dataset to the processed directory
    target_filepath = f'{target_subdirectory_path}/san_francisco_integrated_budget_data.csv'
    sf_integrated_budget_dataset.to_csv(target_filepath, index=False)
    
    # Remove integrated dataset from the directory
    if os.path.exists('data/staged/san_francisco_budget_data/san_francisco_integrated_budget_data.csv'):
        os.remove('data/staged/san_francisco_budget_data/san_francisco_integrated_budget_data.csv')
    
    print(f'Successfully perform transformation logic to san francisco budget datasets and load to the processed directory')