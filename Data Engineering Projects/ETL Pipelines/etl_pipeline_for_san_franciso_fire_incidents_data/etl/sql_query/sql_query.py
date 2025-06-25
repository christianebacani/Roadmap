'''
    SQL Query Module
'''
from sqlalchemy import create_engine
import pandas as pd

def query(query_command: str) -> None:
    '''
        SQL Query Function
    '''
    # Initialize the PostgreSQL Database Server Credentials
    username = '<USERNAME>'
    password = '<PASSWORD>'
    hostname = '<HOSTNAME>'
    port = '<PORT_NUMBER>'
    database = 'san_francisco_fire_incidents_db'

    # Initialize the query engine to test sql queries
    engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')

    # SQL Query
    print(pd.read_sql(query_command, engine))