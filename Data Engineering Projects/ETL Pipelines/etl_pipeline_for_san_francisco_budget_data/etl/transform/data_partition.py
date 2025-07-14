'''
    Data Partition Module
'''
import pandas as pd

def partition(integrated_dataframe: pd.DataFrame) -> None:
    '''
        Data Partition Function
    '''
    # Perform data partition
    target_subdirectory_path = 'data/staged/san_francisco_budget_data'

    for dataset_number, row_number in enumerate(range(0, 360531 + 1, 1000)):
        dataset_number += 1

        target_filepath = f'{target_subdirectory_path}/san_francisco_budget_data({dataset_number}).csv'
        partitioned_dataframe = integrated_dataframe[row_number : row_number + 1000]
        partitioned_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully partitioned {row_number}-{row_number + 999} rows of data from san_francisco_integrated_budget_data.csv')
    
    print(f'Successfully perform data partitioning')