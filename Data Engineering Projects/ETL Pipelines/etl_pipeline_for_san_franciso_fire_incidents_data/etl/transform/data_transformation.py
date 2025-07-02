'''
    Data Transformation Module
'''
import os
import pandas as pd
from transform.data_imputation import impute_values_from_the_integrated_dataset
from transform.data_type_extraction import get_the_data_type_of_every_column
from transform.data_partition import partition_integrated_staged_dataset
from transform.type_casting import cast_data_type
from transform.format_revision import revise_format
from transform.data_integration import integrate_datasets
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
    integrated_dataframe = integrate_datasets('data/stage/san_francisco_fire_incidents_data')

    # Perform data deduplication to the integrated dataset
    deduplicated_dataframe = deduplicate_integrated_dataset(integrated_dataframe)

    # Load transform dataset to processed directory path
    target_subdirectory_path = 'data/processed/san_francisco_fire_incidents_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)
    
    target_filepath = f'{target_subdirectory_path}/san_francisco_fire_incidents_processed_data.csv'
    deduplicated_dataframe.to_csv(target_filepath, index=False)
    print(f'Successfully load san_francisco_fire_incidents_data_processed_data.csv to processed directory path after transformation process')

    # Remove unnecessary datasets and subdirectory path after transformation phase
    if os.path.exists('data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_integrated_data.csv'):
        os.remove('data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_integrated_data.csv')
        print(f'Successfully remove san_francisco_fire_incidents_integrateed_data.csv after transformation phase')

    for dataset_number in range(1, 706 + 1):
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        os.remove(filepath)
        print(f'Successfully remove san_francisco_fire_incidents_data({dataset_name}).csv partitioned dataset after transformation phase')
    
    if os.path.exists('data/stage/san_francisco_fire_incidents_data'):
        os.rmdir('data/stage/san_francisco_fire_incidents_data')
        print(f'Successfully remove \'stage\' subdirectory path after transformation phase')