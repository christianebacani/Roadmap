'''
    Utils Module
'''
from sqlalchemy import create_engine

def init_engine() -> object:
    '''
        Initialize function to initialize
        SQL Alchemy Engine
    '''
    # Engine Parameters
    username = '<POSTGRESQL_USERNAME>'
    password = '<POSTGRESQL_PASSWORD>'
    hostname = '<HOSTNAME>'
    port = '<PORT_NUMBER>'
    database = 'rica_metadatas'

    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}')
    return engine