'''
    Data Transformation Module
'''
import pandas as pd
import os
from transform.data_imputation import impute_values_from_the_integrated_dataset
from transform.type_casting import cast_data_type
from transform.format_revision import revise_format
from transform.data_deduplication import deduplicate_integrated_dataset

def transform_staged_dataset(staged_dataframe: pd.DataFrame) -> None:
    '''
        Data Transformation Function
    '''
    # Data imputation
    staged_dataframe = impute_values_from_the_integrated_dataset(staged_dataframe)

    # NOTE: Type casting operation will perform data partitioning for faster processing
    cast_data_type(staged_dataframe)

    # Format revision for partitioned datasets
    for dataset_number in range(1, 706 + 1):
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        
        partitioned_dataframe = revise_format(pd.read_csv(filepath))
        partitioned_dataframe.to_csv(filepath, index=False)

        print(f'Successfully perform format revision to san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset')
    
    # Performing data integration
    integrated_dataframe = pd.read_csv('data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data(1).csv')

    for dataset_number in range(2, 706 + 1):
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        integrated_dataframe = pd.concat([integrated_dataframe, pd.read_csv(filepath)], ignore_index=True)

        print(f'Successfully integrated san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset for data deduplication process')

    # Data deduplication
    integrated_dataframe = deduplicate_integrated_dataset(integrated_dataframe)

    # Store the transformed integrated dataset to the processed data directory path
    if not os.path.exists('data/processed/san_francisco_fire_incidents_data'):
        os.makedirs('data/processed/san_francisco_fire_incidents_data')
    
    target_filepath = 'data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_processed_data.csv'
    integrated_dataframe.to_csv(target_filepath, index=False)

    # Remove partitioned dataset and integrated staged dataset after transformation phase
    for dataset_number in range(1, 706 + 1):
        if os.path.exists(f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'):
            os.remove(f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv')

            print(f'Successfully removed san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset after transformation phase')
    
    if os.path.exists(f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_integrated_data.csv'):
        os.remove(f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_integrated_data.csv')

        print(f'Successfully removed san_francisco_fire_incidents_integrated_data.csv integrated staged dataset after transformation phase')