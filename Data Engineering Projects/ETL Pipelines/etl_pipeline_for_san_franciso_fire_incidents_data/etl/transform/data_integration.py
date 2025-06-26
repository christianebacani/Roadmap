'''
    Data Integration Module
'''
import pandas as pd
from glob import glob

def integrate_datasets(subdirectory_path: str) -> pd.DataFrame:
    '''
        Data Integration Function
    '''
    integrated_dataframe = pd.read_csv(f'{subdirectory_path}/san_francisco_fire_incidents_data(1).csv')

    for dataset_number in range(2, 706 + 1):
        dataframe = pd.read_csv(f'{subdirectory_path}/san_francisco_fire_incidents_data({dataset_number}).csv')
        integrated_dataframe = pd.concat([integrated_dataframe, dataframe], ignore_index=False)
        
        print(f'Successfully integrated san_francisco_fire_incidents_data({dataset_number}).csv dataset')
    
    return integrated_dataframe