'''
    Data Type Cast Module
'''
import pandas as pd
from datetime import datetime
from glob import glob

def cast_datatype() -> None:
    '''
        Data Type Cast Function
    '''
    total_number_of_datasets = len(glob(f'data/staged/san_francisco_budget_data/*.csv'))

    # Perform type casting
    for dataset_number in range(1, total_number_of_datasets + 1):
        filepath = f'data/staged/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'
        partitioned_dataframe = pd.read_csv(filepath)
        
        # Initialize the dictionary that stores type casted values of every column from the dataset
        columns = list(partitioned_dataframe.keys())
        data = {}

        for column in columns:
            data[column] = []

        for _, row in partitioned_dataframe.iterrows():
            # TODO: Implement more functionalities here...

        target_filepath = filepath
        datatype_casted_dataframe = pd.DataFrame(data)
        datatype_casted_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully perform datatype casting to san_francisco_budget_data({dataset_number}).csv dataset')
    
    print(f'Successfully perform datatype casting')