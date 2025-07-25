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
        account='<SNOWFLAKE_ACCOUNT_IDENTIFIER_>',
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

    # Initialize the primary keys for all dimension datasets
    for table_name, list_of_columns_and_datatypes in table_name_with_list_of_columns_and_datatypes.items():
        if 'fact' in table_name:
            continue

        for i in range(len(list_of_columns_and_datatypes)):
            column = str(list_of_columns_and_datatypes[i]).split()[0]

            if 'id' not in column:
                continue

            list_of_columns_and_datatypes[i] = f'{column} INTEGER PRIMARY KEY'

    # Initialize the foreign keys in facts dataset
    for table_name, list_of_columns_and_datatypes in table_name_with_list_of_columns_and_datatypes.items():
        if 'dim' in table_name:
            continue

        list_of_foreign_keys = []

        for i in range(len(list_of_columns_and_datatypes)):
            column = str(list_of_columns_and_datatypes[i]).split()[0]

            if 'id' not in column:
                continue

            base_table_name = column.replace('_id', '')
            table_name_reference = f'dim_{base_table_name}'

            foreign_key = column
            primary_key = column

            list_of_foreign_keys.append(f'FOREIGN KEY({foreign_key}) REFERENCES {table_name_reference}({primary_key})')

        list_of_columns_and_datatypes.extend(list_of_foreign_keys)

    table_name_with_columns_metadata = table_name_with_list_of_columns_and_datatypes
    table_name_and_ddl_command = {}

    # Finalizing the DDL commands for creating the necessary database objects
    for table_name, columns_metadata in table_name_with_columns_metadata.items():
        ddl_command = '(' + ', '.join(columns_metadata) + ')'
        table_name_and_ddl_command[table_name] = ddl_command

    # Create the necessary database objects using snowflake cursor
    for table_name, ddl_command in table_name_and_ddl_command.items():
        try:
            cursor.execute(f"""CREATE OR REPLACE TABLE {table_name}{ddl_command};""")
            print(f'Successfully created table: {table_name}')

        except Exception as error_message:
            print(f'Error creating table: {table_name}, error message: {error_message}')

    # Close the established snowflake connection and cursor    
    cursor.close()

def load_datasets_to_snowflake(subdirectory_path: str) -> None:
    '''
        Load function to load datasets
        to Snowflake Databases
    '''
    # Create the necessary database objects using snowflake connection as a parameter
    create_database_objects(init_snowflake_connection())