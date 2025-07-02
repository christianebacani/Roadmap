'''
    Data Partition Module
'''
import pandas as pd

def partition_integrated_staged_dataset(dataframe: pd.DataFrame) -> None:
    '''
        Data Partition Function
    '''
    # Perform data partitioning process
    for dataset_number, row_number in enumerate(range(0, 705908 + 1, 1000)):
        dataset_number += 1
        target_filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidentS_data({dataset_number}).csv'
        partitioned_dataframe = dataframe[row_number : row_number + 1000]
        partitioned_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully partitioned integrated staged dataset from {row_number}-{row_number + 999} rows for type casting and format revision process')