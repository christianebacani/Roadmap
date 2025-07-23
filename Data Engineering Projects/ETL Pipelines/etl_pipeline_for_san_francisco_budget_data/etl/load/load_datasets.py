'''
    Load Datasets Module
'''
import pandas as pd
import snowflake.connector
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
        database='san_francisco_budget_db'
    )
    return conn

def load_datasets_to_snowflake(subdirectory_path: str) -> None:
    '''
        Load function to load datasets
        to Snowflake Databases
    '''
    # Initialize a connection to Snowflake
    conn = init_snowflake_connection()
    cursor = conn.cursor()

    # Initialize a dictionary that consist of data types of every column for every table (facts and/or dimension data)
    column_data_types = {
        'object': 'VARCHAR(255)',
        'int64': 'INTEGER',
        'float64': 'NUMBER(11, 2)'
    }

    # Close the established snowflake connection
    cursor.close()