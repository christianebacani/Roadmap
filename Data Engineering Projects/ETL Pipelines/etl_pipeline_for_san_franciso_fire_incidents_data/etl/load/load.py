'''
    Data Loading Module
'''
from sqlalchemy import create_engine
from load.data_integration import integrate_dataset

def load_to_postgresql_db(subdirectory_path: str) -> None:
    '''
        Data Loading Function
    '''
    # PostgreSQL Database Credentials
    username = '<USERNAME>'
    password = '<PASSWORD>'
    hostname = '<HOSTNAME>'
    port = '<PORT_NUMBER_OF_YOUR_POSTGRESQL_DB>'
    database = 'san_francisco_fire_incidents_db'

    # Initializing SQLAlchemy Engine
    engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')

    # Integrate datasets for schema manipulation process later on
    integrate_dataset(subdirectory_path)