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

def create_database_objects():
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
    table_name_and_ddl = {}

    # Finalizing the DDL for creating the necessary database objects
    for table_name, columns_metadata in table_name_with_columns_metadata.items():
        columns_metadata = '(' + ', '.join(columns_metadata) + ')'
        table_name_and_ddl[table_name] = columns_metadata

    # Display the table name and DDL for debugging purposes only    
    for table_name, ddl in table_name_and_ddl.items():
        print(f'{table_name}')
        print(ddl)
        print()

    # TODO: Implement a functionality to create the necessary database objects using the initialized DDLs

    # Close the established snowflake connection
    conn.close()

def load_datasets_to_snowflake(subdirectory_path: str) -> None:
    '''
        Load function to load datasets
        to Snowflake Databases
    '''
    # Create database objects if necessary
    create_database_objects()