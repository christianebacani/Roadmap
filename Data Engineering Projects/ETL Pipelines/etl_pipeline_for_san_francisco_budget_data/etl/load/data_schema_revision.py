'''
    Data Schema Revision Module
'''
import pandas as pd
import os
from glob import glob

def partition(transformed_dataframe: pd.DataFrame) -> None:
    '''
        Data Partition Function for faster
        initialization of dimension and facts data
    '''
    # Perform data partition
    for dataset_number, row_number in enumerate(range(0, 360531 + 1, 1000)):
        dataset_number += 1

        filepath = f'data/processed/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'
        partitioned_dataframe = transformed_dataframe[row_number : row_number + 1000]
        partitioned_dataframe.to_csv(filepath, index=False)

        print(f'Successfully partitioned {row_number}-{row_number + 999} rows of data from san_francisco_integrated_budget_data.csv')

def revise_schema(transformed_dataframe: pd.DataFrame) -> None:
    '''
        Revise Schema Function
    '''
    # Remove unnecessary columns
    transformed_dataframe.drop(columns=['data_as_of', 'data_loaded_at'], inplace=True)

    # Perform data partitioning for faster initialization of dimension and facts data
    partition(transformed_dataframe)

    # Remove integrated dataset from processed directory
    if os.path.exists('data/processed/san_francisco_budget_data/san_francisco_integrated_budget_data.csv'):
        os.remove('data/processed/san_francisco_budget_data/san_francisco_integrated_budget_data.csv')

    total_number_of_datasets = len(glob(f'data/processed/san_francisco_budget_data/*.csv'))

    print(total_number_of_datasets)