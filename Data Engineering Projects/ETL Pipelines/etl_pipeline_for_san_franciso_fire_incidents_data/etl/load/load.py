'''
    Data Load Module
'''
from sqlalchemy import create_engine
from glob import glob

def load_to_postgresql_db(subdirectory_path: str) -> None:
    '''
        Data Load Function
    '''
    username = '<YOUR_USERNAME>'
    password = '<YOUR_PASSWORD>'
    hostname = '<YOUR_HOSTNAME>'
    port = '<YOUR_PORT_NUMBER>'
    database = 'san_francisco_fire_incidents_db'

    engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')