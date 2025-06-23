'''
    Data Transformation Module
'''
import pandas as pd
import os
from transform.data_imputation import impute_values_from_the_integrated_dataset
from transform.data_partition import partition_integrated_staged_dataset
from transform.type_casting import get_the_data_type_of_every_column
from transform.type_casting import cast_data_type
from transform.format_revision import revise_format
from transform.data_deduplication import deduplicate_integrated_dataset

def transform_staged_dataset(staged_dataframe: pd.DataFrame) -> None:
    '''
        Data Transformation Function
    '''
    # Data imputation
    staged_dataframe = impute_values_from_the_integrated_dataset(staged_dataframe)

    # Get the data types of every column from integrated staged dataset for type casting process
    column_and_data_type = get_the_data_type_of_every_column(staged_dataframe)

    # Partition integrated staged dataset for type casting and format revision process
    partition_integrated_staged_dataset(staged_dataframe)
    
    for dataset_number in range(1, 706 + 1):
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        partitioned_dataframe = pd.read_csv(filepath)

        dataset_name = f'san_francisco_fire_incidents_data({dataset_number}).csv'

        type_casted_dataframe = cast_data_type(partitioned_dataframe, column_and_data_type, dataset_name)
        format_revised_dataframe = revise_format(type_casted_dataframe, dataset_name)

        transformed_dataframe = format_revised_dataframe
        transformed_dataframe.to_csv(filepath, index=False)
    
    # Integrate partitioned dataset after type casting and format revision process
    integrated_dataframe = pd.read_csv('data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data(1).csv')

    for dataset_number in range(2, 706 + 1):
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        integrated_dataframe = pd.concat([integrated_dataframe, pd.read_csv(filepath)], ignore_index=True)

        print(f'Successfully integrated san_francisco_fire_incidents_data({dataset_number}).csv dataset')
    
    # Data deduplication
    integrated_dataframe = deduplicate_integrated_dataset(integrated_dataframe)
    
    # Store the integrated processed dataset to the processed directory path for loading phase
    target_subdirectory_path = 'data/processed/san_francisco_fire_incidents_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)
    
    target_filepath = f'{target_subdirectory_path}/san_francisco_fire_incidents_processed_data.csv'
    integrated_dataframe.to_csv(target_filepath, index=False)

    # Remove partitioned and integrated dataset after transformation phase
    for dataset_number in range(1, 706 + 1):
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'

        if os.path.exists(filepath):
            os.remove(filepath)
            print(f'Successfully removed san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset')
    
    if os.path.exists('data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_integrated_data.csv'):
        os.remove('data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_integrated_data.csv')
        print('Successfully remove san_francisco_fire_incidents_integrated_data.csv')