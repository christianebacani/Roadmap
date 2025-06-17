'''
    Data Transformation Module
'''
import pandas as pd
from transform.data_imputation import impute_values_from_the_integrated_datasetr
from transform.data_partition import partition_integrated_dataset
from transform.type_casting import cast_data_type
from transform.format_revision import revise_format
from transform.data_deduplication import deduplicate_integrated_dataset
import os

def transform_staged_dataset(staged_dataframe: pd.DataFrame) -> None:
    '''
        Data Transformation Function
    '''
    # Data imputation using a function from other modules
    staged_dataframe = impute_values_from_the_integrated_datasetr(staged_dataframe)

    # Data partition using a function from other modules also
    partition_integrated_dataset(staged_dataframe)
    
    # Performing other transformation processes (Type casting, Data format revisi.on, and Data Deduplication) from the partitioned datasets
    for dataset_number in range(1, 707):
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'

        type_casted_dataframe = cast_data_type(pd.read_csv(filepath))
        format_revised_dataframe = revise_format(type_casted_dataframe)
        
        transformed_dataframe = format_revised_dataframe
        transformed_dataframe.to_csv(filepath, index=False)

        print(f'Successfully transformed the partitioned dataset san_francisco_fire_incidents_data({dataset_number}).csv')
    
    # Integrate the datasets for deduplication process
    integrated_dataframe = pd.read_csv('data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data(1).csv')
    
    for dataset_number in range(2, 707):
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        integrated_dataframe = pd.concat([integrated_dataframe, pd.read_csv(filepath)])

        print(f'Successfully integrated san_francisco_fire_incidents_data({dataset_number}).csv transformed dataset')
    
    # Remove the partitioned datasets from the directory path
    for dataset_number in range(1, 707):
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'

        if os.path.exists(filepath):
            os.remove(filepath)
            print(f'Successfully removed san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset')
    
    # Deduplicate the integrated dataset using function from other modules
    integrated_dataframe = deduplicate_integrated_dataset(integrated_dataframe)
    
    # Store the processed dataset to the target directory path
    target_directory_path = 'data/processed'
    target_subdirectory_path = f'{target_directory_path}/san_francisco_fire_incidents_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)

    target_filepath = f'{target_subdirectory_path}/san_francisco_fire_incidents_processed_data.csv'
    integrated_dataframe.to_csv(target_filepath, index=False)

    print(f'Successfully transformed the integrated staged dataset')