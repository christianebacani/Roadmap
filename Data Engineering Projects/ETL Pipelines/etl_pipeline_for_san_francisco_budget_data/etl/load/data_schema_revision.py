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
    columns = list(pd.read_csv('data/processed/san_francisco_budget_data/san_francisco_budget_data(1).csv').keys())

    # Initialize the structure of the dimension data
    dimension_data = []

    for column in columns:
        if column == 'budget':
            continue

        primary_key = f'{column}_id'
        dimension_data.append({
            primary_key: [],
            column: []
        })
    
    # Initialize the non-key attributes of all dimension data
    for column in columns:
        if column == 'budget':
            continue

        values = []

        for dataset_number in range(1, total_number_of_datasets + 1):
            filepath = f'data/processed/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'
            partitioned_dataframe = pd.read_csv(filepath)
            values.extend(list(partitioned_dataframe[column]))

        distinct_values = []

        for i in range(len(values)):
            if str(values[i]).lower() == 'nan':
                continue

            if values[i] in distinct_values:
                continue

            distinct_values.append(values[i])

        values = distinct_values
        
        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            dimension_data[i][column] = values

        print(f'Successfully initializes non-key attributes of dim_{column} dimension data')
    
    # Initialize the key attributes of all dimension data
    for column in columns:
        if column == 'budget':
            continue

        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue
            
            primary_key_values = []
            total_number_of_values = len(dimension_data[i][column])

            for primary_key_value in range(1, total_number_of_values + 1):
                primary_key_values.append(primary_key_value)

            primary_key = f'{column}_id'
            dimension_data[i][primary_key] = primary_key_values
        
        print(f'Successfully initializes key attributes of dim_{column} dimension data')
    
    # Initialize all dimension data as a dataframe  
    for column in columns:
        if column == 'budget':
            continue

        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            target_filepath = f'data/processed/san_francisco_budget_data/dim_{column}.csv'
            dimension_dataframe = pd.DataFrame(dimension_data[i])
            dimension_dataframe.to_csv(target_filepath, index=False)

            print(f'Successfully initialize dim_{column} dimension data as a dataframe')

    # Initialize the structure of facts data    
    facts_data = {}

    for column in columns:
        if column == 'budget':
            continue

        foreign_key = f'{column}_id'
        facts_data[foreign_key] = []

    for column in columns:
        if column == 'budget':
            facts_data['budget'] = []
            break
    
    column_and_dimension_df = {}

    for column in columns:
        if column == 'budget':
            continue

        # TODO: Initialize the dimension column as a key and the corresponding dimension dataframe as a value for the dictionary 'column_and_dimension_df'