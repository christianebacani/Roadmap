'''
    Data Type Cast Module
'''
import pandas as pd

def cast_datatype(total_number_of_datasets: int) -> None:
    '''
        Data Type Cast Function
    '''
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

                # TODO: Implement more functionalities here...