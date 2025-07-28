'''
    Load Datasets Module
'''
import pandas as pd
import snowflake.connector
from glob import glob

def init_snowflake_connection() -> None:
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

def create_database_objects(cursor) -> None:
    '''
        Create function to create
        necessary database objects
    '''
    # Initialize a dictionary for necessary column constraints of column datatypes for object creation
    column_datatypes = {
        'object': 'VARCHAR(255)',
        'int64': 'INTEGER',
        'float64': 'NUMBER(11,2)'
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

    # Initialize the foreign key and foreign key constraints of facts table
    for table_name, list_of_columns_datatype in table_name_with_list_of_colums_datatype.items():
        if 'dim' in table_name:
            continue

        list_of_foreign_key_constraints = []

        for i in range(len(list_of_columns_datatype)):
            column = str(list_of_columns_datatype[i]).split()[0]

            if 'id' in column:
                base_table_name = str(column).replace('_id', '')
                table_name_reference = f'dim_{base_table_name}s'

                foreign_key = column
                primary_key = column

                list_of_foreign_key_constraints.append(f'FOREIGN KEY({foreign_key}) REFERENCES {table_name_reference}({primary_key})')

        list_of_columns_datatype.extend(list_of_foreign_key_constraints)

    # Initialize the table name with their corresponding columns metadata
    table_name_with_columns_metadata = {}

    for table_name, list_of_columns_datatype in table_name_with_list_of_colums_datatype.items():
        columns_metadata = '(' + ', '.join(list_of_columns_datatype) + ')' + ';'
        table_name_with_columns_metadata[table_name] = columns_metadata
    
    # Create necessary database objects
    for table_name, columns_metadata in table_name_with_columns_metadata.items():
        try:
            cursor.execute(f"""CREATE OR REPLACE TABLE {table_name}{columns_metadata};""")
            print(f'Successfully created a a table: {table_name}')

        except Exception as error_message:
            print(f'Error creating table: {table_name}. Error message: {error_message}')

def load_datasets_to_snowflake(subdirectory_path: str) -> None:
    '''
        Load function to load datasets
        to Snowflake Databases
    '''
    # Established a snowflake connection and cursor
    conn = init_snowflake_connection()
    cursor = conn.cursor()

    # Create necessary database objects using cursor parameter
    create_database_objects(cursor)

    # Create temporary stage to store processed datasets before loading it to snowflake tables
    try:
        cursor.execute("""CREATE OR REPLACE TEMPORARY STAGE processed_datasets
                          FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"');""")
    
    except Exception as error_message:
        print(f'Error creating temporary stage: processed_datasets. Error message: {error_message}')

    # Load processed datasets to temporary stage
    for csv_file in glob(f'{subdirectory_path}/*.csv'):
        csv_file = str(csv_file).replace('\\', '/')
        base_filename = str(csv_file).replace('data/processed/san_francisco_budget_data/', '')

        try:
            cursor.execute(f"""PUT file://{csv_file} @processed_datasets OVERWRITE = TRUE;""")
            print(f'Successfully loaded data: {base_filename} to temporary stage: processed_datasets')

        except Exception as error_message:
            print(f'Error loading data: {base_filename} to temporary stage: processed_datasets')    

    # TODO: Implement more functionalities like loading datasets from temporary stage to snowflake tables and removing processed datasets from 'processed' directory path

    # Close established snowflake connection and cursor
    cursor.close()
    conn.close()

    print(f'Successfully perform data loading phase')