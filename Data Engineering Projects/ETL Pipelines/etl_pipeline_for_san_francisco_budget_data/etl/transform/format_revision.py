'''
    Format Revision Module
'''
import pandas as pd
from glob import glob

def revise_dataset_format() -> None:
    '''
        Format Revision Function
    '''
    # Perform format revision
    total_number_of_datasets = len(glob(f'data/staged/san_francisco_budget_data/*.csv'))
    
    for dataset_number in range(1, total_number_of_datasets + 1):
        filepath = f'data/staged/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'
        partitioned_dataframe = pd.read_csv(filepath)
        
        # Initialize the dictionary that stores formatted/standardized values of every column from the dataset
        columns = list(partitioned_dataframe.keys())
        data = {}

        for column in columns:
            data[column] = []

        # Initialize the json file that consist of all the values that needs to be formatted/standardized from san francisco budget datasets column
        sf_budget_datasets_formatted_values = pd.read_json('etl/transform/san_francisco_budget_datasets_formatted_values.json')
        
        for _, row in partitioned_dataframe.iterrows():
            for column in columns:
                value = row.get(column)
                
                if str(value).lower() == 'nan':
                    data[column].append(pd.NA)
                    continue

                if column not in ['department', 'object', 'sub_object']:
                    data[column].append(value)
                    continue

                try:
                    value = sf_budget_datasets_formatted_values[str(value)][0]
                    data[column].append(value)
                
                except KeyError:
                    data[column].append(value)
        
        target_filepath = filepath
        formatted_dataframe = pd.DataFrame(data)
        formatted_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully perform format revisioning to san_francisco_budget_data({dataset_number}).csv dataset')
    
    print(f'Successfully perform format revisioning')