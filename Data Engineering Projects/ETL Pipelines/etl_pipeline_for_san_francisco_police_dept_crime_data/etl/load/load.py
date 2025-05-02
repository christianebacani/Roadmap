'''
    Load Module
'''
from sqlalchemy import create_engine
from glob import glob
import pandas as pd

def load_processed_datasets_to_postgresql_db(processed_subdir_path: str) -> None:
    '''
        Load function to load processed datasets to
        PostgreSQL Database Server after enforcing 
        schema to adhere to the data model
    '''
    username = '<YOUR_USERNAME>'
    password = '<YOUR_PASSWORD>'
    hostname = '<YOUR_HOSTNAME>'
    port_number = '<YOUR_PORT_NUMBER>'
    database = 'san_francisco_pd_incident_reports'

    engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port_number}/{database}')

    base_filename = processed_subdir_path.replace('data/processed/', '')
    total_datasets = len(glob(f'{processed_subdir_path}/*.csv'))

    for dataset_num in range(1, total_datasets + 1):
        processed_dataset_filepath = f'{processed_subdir_path}/{base_filename}({dataset_num}).csv'
        processed_dataframe = pd.read_csv(processed_dataset_filepath)
        table_name = base_filename
        processed_dataframe.to_sql(table_name, engine, if_exists='replace', index=False)

        print(f'Successfully loaded {base_filename}({dataset_num}) dataset to PostgreSQL Database Server')