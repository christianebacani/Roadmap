'''
    Data Integration Module
'''
import pandas as pd
from glob import glob

def integrate_dataset(subdirectory_path: str) -> pd.DataFrame:
    '''
        Data Integration Function
    '''
    # Initialize the first dataframe to be the base dataframe for integration using pd.concat() method
    first_dataframe = pd.read_csv(f'{subdirectory_path}/san_francisco_fire_incidents_data(1).csv')
    integrated_dataframe = first_dataframe

    dataset_name = 'san_francisco_fire_incidents_data'
    total_dataset = len(glob(f'{subdirectory_path}/*.csv'))

    for dataset_number in range(2, total_dataset + 1):
        filepath = f'{subdirectory_path}/{dataset_name}({dataset_number}).csv'
        dataframe = pd.read_csv(filepath)
        integrated_dataframe = pd.concat([integrated_dataframe, dataframe], ignore_index=True)

        print(f'Successfully integrate {dataset_name}({dataset_number}).csv to the dataset')

    return integrated_dataframe