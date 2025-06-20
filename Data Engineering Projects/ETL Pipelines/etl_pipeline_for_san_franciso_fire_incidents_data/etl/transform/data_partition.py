'''
    Data Partition Module
'''
import pandas as pd

def partition_integrated_dataset(dataframe: pd.DataFrame) -> None:
    '''
        Data Partition Function
    '''
    # Initializing target directory path

    target_directory_path = 'data/stage'
    target_subdirectory_path = f'{target_directory_path}/san_francisco_fire_incidents_data'

    # Partitioning process for better processing of different transformation phases
    for dataset_number, row_number in enumerate(range(0, 705909, 1000)):
        dataset_number += 1
        partitioned_dataframe = dataframe[row_number : row_number + 1000]
        
        target_filepath = f'{target_subdirectory_path}/san_francisco_fire_incidents_data({dataset_number}).csv'
        partitioned_dataframe.to_csv(target_filepath, index=False)
        print(f'Successfully partitioned {row_number}-{row_number + 999} rows from the integrated staged dataset for data transformation phase')