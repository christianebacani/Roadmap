'''
    Load Processed Dataset Module
'''
import pandas as pd
import os

def load_processed_integrated_dataset(dataframe: pd.DataFrame) -> None:
    '''
        Load Processed Dataset Function
    '''
    target_subdirectory_path = 'data/processed/san_francisco_fire_incidents_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)

    target_filepath = f'{target_subdirectory_path}/san_francisco_fire_incidents_processed_data.csv'
    dataframe.to_csv(target_filepath, index=False)

    print(f'Successfully loaded san_francisco_fire_incidents_processed_data.csv to processed data directory path')   