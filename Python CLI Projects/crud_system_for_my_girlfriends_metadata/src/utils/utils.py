'''
    Utils Module
'''
import psycopg2
from glob import glob
from sqlalchemy import create_engine

def init_engine() -> object:
    '''
        Initialize function to initialize
        SQL Alchemy Engine for Reading Data
        from PostgreSQL Database
    '''
    # Engine Parameters
    username = '<POSTGRESQL_ACCOUNT_USERNAME>'
    password = '<POSTGRESQL_ACCOUNT_PASSWORD>'
    host = '<HOSTNAME>'
    port = '<PORT_NUMBER>'
    database = 'rica_metadatas'

    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
    return engine

def init_connection() -> object:
    '''
        Initialize function to initialize
        a connection to PostgreSQL Database
        using Psycopg2 for CRUD Process
    '''
    conn = psycopg2.connect(
        user='<POSTGRESQL_ACCOUNT_USERNAME>',
        password='<POSTGRESQL_ACCOUNT_PASSWORD>',
        host='<HOSTNAME>',
        port='<PORT_NUMBER>',
        database='rica_metadatas'
    )
    return conn

def get_table_names() -> list[str]:
    '''
        Get function to extract all table names
        from PostgreSQL Database
    '''
    list_of_table_names = []

    for csv_file in glob(f'src/metadata/*.csv'):
        csv_file = str(csv_file).replace('\\', '/')
        table_name = str(csv_file).replace('src/metadata/', '')
        table_name = str(table_name).replace('.csv', '')

        list_of_table_names.append(table_name)

    return list_of_table_names