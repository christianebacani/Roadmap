'''
    Load Datasets Module
'''
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from glob import glob

def init_snowflake_connection():
    '''
        Initialize function to initialize
        Snowflake Connection using 
    '''
    conn = snowflake.connector.connect(
        user='<SNOWFLAKE_USERNAME>',
        password='<SNOWFLAKE_PASSWORD>',
        account='<SNOWFLAKE_ACCOUNT_IDENTIFIER>',
        warehouse='san_francisco_budget_data_warehouse',
        database='san_francisco_budget_data',
        schema='san_francisco_budget_data_star_schema'
    )
    return conn

def create_database_objects(conn):
    '''
        Create function to create
        necessary database objects
    '''
    # Initialize a snowflake connection cursor
    cursor = conn.cursor()

    # Initialize a dictionary for necessary column constraints of column datatypes for object creation
    column_datatypes = {
        'object': 'VARCHAR(255)',
        'int64': 'INTEGER',
        'float64': 'NUMBER(11, 2)'
    }

    # Close the snowflake cursor connection
    cursor.close()

def load_datasets_to_snowflake(subdirectory_path: str) -> None:
    '''
        Load function to load datasets
        to Snowflake Databases
    '''