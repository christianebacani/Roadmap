'''
    Utilities Module
'''
import os
import psycopg2
import pandas as pd
from glob import glob
from sqlalchemy import create_engine

def display_invalid_choice_message() -> None:
    '''
        Display function to display
        invalid choice message
    '''
    os.system('cls')
    print(f'\t\tInvalid choice! Please try again.')
    input(f'\t\tPress any key to reload page: ')
    os.system('cls')

def get_the_list_of_table_names() -> list[str]:
    '''
        Get function to get the
        list of table names by 
        reading the file names
        from 'data' directory
    '''
    result = []

    for csv_file in glob(f'data/*'):
        csv_file = str(csv_file).replace('\\', '/')
        table_name = str(csv_file).replace('data/', '').replace('.csv', '')
        result.append(table_name)

    return result
    
def init_connection() -> object:
    '''
        Initialize Function to
        initialize a Psycopg2
        Connection for PostgreSQL
        Database
    '''
    conn = psycopg2.connect(
        user='<POSTGRESQL_USERNAME>',
        password='<POSTGRESQL_PASSWORD>',
        host='<HOSTNAME>',
        port='<PORT_NUMBER>',
        database='rica_metadatas'
    )
    return conn

def init_engine() -> object:
    '''
        Initialize Function to
        initialize a SQL Alchemy
        Engine for Quick Data
        Retrieval from PostgreSQL
        Database Server
    '''
    user = '<POSTGRESQL_USERNAME>'
    password = '<POSTGRESQL_PASSWORD>'
    host = '<HOSTNAME>'
    port = '<PORT_NUMBER>'
    database = 'rica_metadatas'

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    return engine

def get_the_list_of_column_names(table_name: str) -> list[str]:
    '''
        Get function to get the
        list of column names by 
        reading the table using
        pandas from the csv file
        of 'data' directory
    '''
    engine = init_engine() # Initialize SQL Alchemy Engine for PostgreSQL Database
    dataframe = pd.read_sql(f'SELECT * FROM {table_name}', engine)
    columns = list(dataframe.columns)
    return columns