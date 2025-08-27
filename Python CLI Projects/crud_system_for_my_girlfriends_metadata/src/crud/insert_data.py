'''
    Insert Data Module
'''
import os
import pandas as pd
from src.utils.utils import display_invalid_choice_message
from src.utils.utils import get_the_list_of_table_names
from src.utils.utils import get_the_list_of_column_names
from src.utils.utils import init_connection
from src.utils.utils import init_engine

def insert_data(table_name: str) -> None:
    '''
        Insert data function to insert
        new data from the chosen table
    '''
    def init_sql_command_for_data_insertion(table_name: str, inserted_data: dict[str, str]) -> str:
        '''
            Initialize function to initialize
            SQL Command for Data Insertion
        '''
        columns = ', '.join(list(inserted_data.keys()))
        command = f'INSERT INTO {table_name} ({columns})'
        
        values = []
    
        for value in list(inserted_data.values()):
            # Check if the value can be typecasted to integer and float
            try:
                int(value)
                float(value)
                values.append(value)

            # We need to make sure when inserting string/date/time/datetime datatype values we use open and close quotation marks
            except:
                values.append(f'\'{value}\'')

        values = ', '.join(values)
        command = command + ' ' + 'VALUES' + '(' + values + ')'
        
        return command

    while True:
        columns = get_the_list_of_column_names(table_name) # Get the column names

        # Display header
        print(f'\t\t', end='')
        print('=' * 28)
        header = 'Insert Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 28)
        print()

        # Dictionary to store the new data as a value and column name as a key
        inserted_data = {}

        for column in columns:
            inserted_data[column] = None

        print(f'\t\tTable Name: {table_name}')
        
        inserted_data_not_confirm = False
        invalid_confirmation = False

        # Ask for the data to be inserted to the given table
        for column in columns:
            data = input(f'\t\tEnter the new data for {column} column: ')
            confirm_inserted_data = input(f'\t\tDid you enter the correct data (Y/N)?: ').strip().upper()

            if confirm_inserted_data == 'N':
                inserted_data_not_confirm = True
                break

            if confirm_inserted_data != 'Y':
                invalid_confirmation = True
                break
            
            if data != '':
                inserted_data[column] = data

        if inserted_data_not_confirm:
            os.system('cls')
            continue
        
        if invalid_confirmation:
            os.system('cls')
            print(f'\t\tInvalid confirmation! Please try again.')
            input(f'\t\tPress any key to reload the page: ')
            os.system('cls')
            continue

        # Display header
        os.system('cls')
        print(f'\t\t', end='')
        print('=' * 28)
        header = 'Inserted Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 28)
        print()
        
        # Display table name and the inserted data per column
        print(f'\t\tTable Name: {table_name}')

        for column, data in inserted_data.items():
            print(f'\t\t{column}: {data}')
        
        input(f'\n\t\tPress any key to insert the given data from the table: ')
        
        try:
            conn = init_connection() # Initialize a connection to the PostgreSQL Database using Pyscopg2
            cursor = conn.cursor() # Initialize a cursor from the established connection
            command = init_sql_command_for_data_insertion(table_name, inserted_data)
        
            cursor.execute(command)
            conn.commit()
            
            cursor.close()
            conn.close()
            
            engine = init_engine() # Initialize SQL Alchemy Engine for PostgreSQL Database
            dataframe = pd.read_sql(f'SELECT * FROM {table_name}', engine)
            dataframe.to_csv(f'data/{table_name}.csv', index=False)

            os.system('cls')
            print(f'\t\tSuccessfully inserted data to {table_name} table')
            input(f'\t\tPress any key to exit page: ')
            os.system('cls')
            break

        except Exception as error_message:
            os.system('cls')
            print(f'\t\tError: {error_message}')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

def insert_data_page() -> None:
    '''
        Insert Data Page function to
        insert new rows of data from
        the chosen table of my girlfriend's
        metadata
    '''
    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 28)
        header = 'Insert Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 28)
        print()

        table_names = get_the_list_of_table_names() # Get the table names

        # Display invalid message when there's no table available to be inserted
        if table_names == []:
            os.system('cls')
            print(f'\t\tCurrently there\'s no table created!')
            input(f'\t\tPress any key to exit the page: ')
            os.system('cls')
            break

        # Display options
        for number, table_name in enumerate(table_names):
            number += 1
            print(f'\t\t{number}.) Insert data to {table_name} table')

        # Display exit option
        last_number = len(table_names) + 1
        print(f'\t\t{last_number}.) Exit')

        try:
            choice = int(input(f'\n\t\tEnter your choice here: '))

            if choice == last_number:
                os.system('cls')
                break
            
            elif (choice >= 1) and (choice <= len(table_names)):
                os.system('cls')
                insert_data(table_names[choice - 1])
                continue

            else:
                display_invalid_choice_message()
                continue

        except ValueError:
            display_invalid_choice_message()
            continue            