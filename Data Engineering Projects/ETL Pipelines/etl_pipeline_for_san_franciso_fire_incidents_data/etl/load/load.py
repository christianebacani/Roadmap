'''
    Data Load Module
'''
from glob import glob
import pandas as pd
from sqlalchemy import create_engine

def load_to_postgresql_db(subdirectory_path: str) -> None:
    '''
        Data Load Function
    '''
    # Initialize the PostgreSQL Database Server Credentials
    username = '<YOUR_USERNAME>'
    password = '<YOUR_PASSWORD>'
    hostname = '<YOUR_HOSTNAME>'
    port = '<YOUR_PORT_NUMBER>'
    database = 'san_francisco_fire_incidents_db'

    # Initialize the query engine to map the dataframes to the database objects
    engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')

    # Display the table name for debugging purposes only
    for csv_file in glob(f'{subdirectory_path}/*.csv'):
        dataframe = pd.read_csv(csv_file)

        base_filename = str(csv_file).replace('data/processed/san_francisco_fire_incidents_data/', '')
        table_name = base_filename.replace('.csv', '')
        
        dataframe.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f'Successfully loaded {table_name} table to the PostgreSQL Database Server')