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
        
        # Initialize the dictionary that stores type casted values of every column
        columns = list(partitioned_dataframe.keys())
        data = {}

        for column in columns:
            data[column] = []

        for _, row in partitioned_dataframe.iterrows():
            for column in columns:
                value = row.get(column)

                if str(value).lower() == 'nan':
                    data[column].append(pd.NA)
                    continue

                try:
                    value = datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.%f')
                    data[column].append(value)
                    continue

                except:
                    pass

                if str(value).isdigit():
                    value = int(value)
                    data[column].append(value)
                    continue

                try:
                    value = float(value)
                    data[column].append(value)
                
                except:
                    value = str(value)
                    data[column].append(value)
        
        target_filepath = filepath
        datatype_casted_dataframe = pd.DataFrame(data)
        datatype_casted_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully perform datatype casting to san_francisco_budget_data({dataset_number}).csv dataset')
    
    print(f'Successfully perform datatype casting')