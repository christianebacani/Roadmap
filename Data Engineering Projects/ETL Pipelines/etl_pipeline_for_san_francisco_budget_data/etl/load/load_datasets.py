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

    # Initialize a dictionary to store table name with their corresponding columns and columns datatype for initializing DDL commands
    table_name_with_list_of_colums_datatype = {}

    # Get the data type and column constrainst of every colums for every table
    for csv_file in glob(f'data/processed/san_francisco_budget_data/*.csv'):
        base_filename = str(csv_file).replace('data/processed/san_francisco_budget_data\\', '')
        table_name = str(base_filename).replace('.csv', '')

        dataframe = pd.read_csv(csv_file)
        list_of_columns = list(dataframe.columns)

        list_of_columns_datatype = []

        for column in list_of_columns:
            if 'id' in column:
                list_of_columns_datatype.append(f'{column} INTEGER')
            
            else:
                datatype = str(dataframe[column].dtype)
                list_of_columns_datatype.append(f'{column} {column_datatypes[datatype]}')

        table_name_with_list_of_colums_datatype[table_name] = list_of_columns_datatype

    # Initialize the primary key constraints of every dimension table
    for table_name, list_of_columns_datatype in table_name_with_list_of_colums_datatype.items():
        if 'facts' in table_name:
            continue

        for i in range(len(list_of_columns_datatype)):
            column = str(list_of_columns_datatype[i]).split()[0]

            if 'id' in column:
                list_of_columns_datatype[i] = f'{column} INTEGER PRIMARY KEY'

    # Display the table name and their corresponding columns datatype and primary key constraints
    for table_name, list_of_columns_datatype in table_name_with_list_of_colums_datatype.items():
        print(f'{table_name}:')
        print(list_of_columns_datatype)
        print()

    # Close the snowflake cursor connection
    cursor.close()

def load_datasets_to_snowflake(subdirectory_path: str) -> None:
    '''
        Load function to load datasets
        to Snowflake Databases
    '''
    # Initialize a snowflake connection and create necessary database objects
    conn = init_snowflake_connection()
    create_database_objects(conn)