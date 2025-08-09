'''
    Utils Module
'''
import psycopg2
from glob import glob
from sqlalchemy import create_engine

def init_engine() -> object:
    '''
        Initialize function to initialize
        SQL Alchemy Engine
    '''
    # Engine Parameters
    username = '<POSTGRESQL_USERNAME>'
    password = '<POSTGRSQL_PASSWORD>'
    hostname = '<HOSTNAME>'
    port = '<PORT_NUMBER>'
    database = 'rica_metadatas'

    engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')
    return engine

def init_cursor() -> object:
    '''
        Initialize function to initialize
        Pyscopgy2 Cursor for executing PostgreSQL
        Database commands using Python script
    '''
    
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