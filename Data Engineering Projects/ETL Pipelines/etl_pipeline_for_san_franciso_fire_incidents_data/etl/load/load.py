'''
    Data Loading Module
'''
from sqlalchemy import create_engine

def load_to_postgresql_db(subdirectory_path: str) -> None:
    '''
        Data Loading Function
    '''
    username = '<YOUR_USERNAME>'
    password = '<YOUR_PASSWORD>'
    port = '<YOUR_PORT_NUMBER>'
    database_name = 'san_francisco_fire_incidents_data'