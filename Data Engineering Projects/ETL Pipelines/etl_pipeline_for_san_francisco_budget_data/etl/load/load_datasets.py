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

def create_database_objects(conn):
    '''
        Create function to create
        necessary database objects
    '''
    # Establish a snowflake connection and use connection cursor
    conn = init_snowflake_connection()
    cursor = conn.cursor()

    # Initialize a dictionary for necessary column constraints of column datatypes for object creation
    column_datatypes = {
        'object': 'VARCHAR(255)',
        'int64': 'INTEGER',
        'float64': 'NUMBER(11, 2)'
    }

    # Initialize a dictionary to store the table name and their corresponding columns and data types
    table_name_with_list_of_columns_and_datatypes = {}

    for csv_file in glob(f'data/processed/san_francisco_budget_data/*.csv'):
        base_filename = str(csv_file).replace('data/processed/san_francisco_budget_data\\', '')
        table_name = str(base_filename).replace('.csv', '')

        dataframe = pd.read_csv(csv_file)
        list_of_columns = list(dataframe.columns)

        list_of_columns_and_datatypes = []

        for column in list_of_columns:
            if 'id' in column:
                list_of_columns_and_datatypes.append(f'{column} INTEGER')
                continue
            
            datatype = str(dataframe[column].dtype)
            list_of_columns_and_datatypes.append(f'{column} {column_datatypes[datatype]}')

        table_name_with_list_of_columns_and_datatypes[table_name] = list_of_columns_and_datatypes

    # TODO: Add functionality to initialize the primary keys, foreign keys, and establish a query for transaction for database object creation

    # Close the established snowflake connection
    conn.close()

def load_datasets_to_snowflake(subdirectory_path: str) -> None:
    '''
        Load function to load datasets
        to Snowflake Databases
    '''