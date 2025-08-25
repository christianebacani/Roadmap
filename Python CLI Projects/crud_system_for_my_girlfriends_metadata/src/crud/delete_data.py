'''
    Delete Data Module
'''
import os
import pandas as pd
from src.utils.utils import get_the_list_of_table_names
from src.utils.utils import display_invalid_choice_message
from src.utils.utils import init_connection
from src.utils.utils import init_engine

def delete_data(table_name: str) -> None:
    '''
        Delete data function to delete
        a specific row based on the chosen
        table of my girlfriend's metadata
    '''
    def init_sql_command_for_data_deletion(table_name: str, deleted_data: dict[str, str]) -> str:
        '''
            Initialize function to initialize
            SQL Command for Data Deletion
        '''
        command = f'DELETE FROM {table_name}'
        where_clause = []

        for column, data in deleted_data.items():
            # Check if the data can be typecasted to integer and float
            try:
                int(data)
                float(data)
                where_clause.append(f'{column} = {data}')
                
            # We need to make sure when using string/date/time/datetime datatype values at 'WHERE' clause, we use open and close quotation marks
            except:
                where_clause.append(f'{column} = \'{data}\'')

        where_clause = ' AND '.join(where_clause)
        command = command + ' ' + 'WHERE' + ' ' + where_clause

        return command

    conn = init_connection() # Initialize a connection to the PostgreSQL Database using Pyscopg2
    dataframe = pd.read_sql(f'SELECT * FROM {table_name}', conn)    
    columns = list(dataframe.columns)
    conn.close()

    while True:
        # Display Header
        print(f'\t\t', end='')
        print(f'=' * 27)
        header = 'Delete Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print(f'=' * 27)

        # Dictionary to store the data to be remove as a value and the column as a key
        deleted_data = {}

        for column in columns:
            deleted_data[column] = None

        deleted_data_not_confirm = False
        invalid_confirmation = False
        
        # Ask for the data to be deleted from the table
        for column in columns:
            data = input(f'\t\tEnter the data to be deleted from {column} column: ')
            confirm_deleted_data = input(f'\t\tDid you enter the correct data (Y/N)?: ').strip().upper()

            if confirm_deleted_data == 'N':
                deleted_data_not_confirm = True
                break
            
            if confirm_deleted_data != 'Y':
                invalid_confirmation = True
                break
            
            if data != '':
                deleted_data[column] = data

        if deleted_data_not_confirm:
            os.system('cls')
            continue
        
        if invalid_confirmation:
            os.system('cls')
            print(f'\t\tInvalid confirmation! Please try again.')
            input(f'\t\tPress any key to reload the page: ')
            os.system('cls')
            continue
        
        # Display Header
        os.system('cls')
        print(f'\t\t', end='')
        print(f'=' * 28)
        header = 'Deleted Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print(f'=' * 28)

        # Display table name and the deleted data per column
        print(f'\t\tTable Name: {table_name}')

        for column, data in deleted_data.items():
            print(f'\t\t{column}: {data}')
        
        input(f'\n\t\tPress any key to delete the given data from the table: ')

        try:
            conn = init_connection() # Initialize a connection to the PostgreSQL Database using Pyscopg2
            cursor = conn.cursor() # # Initialize a cursor from the established connection
            command = init_sql_command_for_data_deletion(table_name, delete_data)

            cursor.execute(command)
            conn.commit()

            cursor.close()
            conn.close()

            os.system('cls')
            print(f'\t\tSuccessfully deleted data from {table_name} table')
            input(f'\t\tPress any key to exit page: ')
            os.sytem('cls')
            break

        except Exception as error_message:
            os.system('cls')
            print(f'\t\tError: {error_message}')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

def delete_data_page() -> None:
    '''
        Delete data function to
        delete a row of data from
        the chosen table of my
        girlfriend's metadata
    '''
    while True:
        # Display Header
        print(f'\t\t', end='')
        print(f'=' * 27)
        header = 'Delete Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print(f'=' * 27)
        
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
            print(f'\t\t{number}.) Delete a row from {table_name} table')
        
        # Display exit option
        last_number = len(table_names) + 1
        print(f'\t\t{last_number}.) Exit')

        try:
            choice = int(input(f'\n\t\tEnter your choice here: '))

            if choice == last_number:
                os.system('cls')
                break
            
            elif (choice >= 1 and choice <= len(table_names)):
                os.system('cls')    
                delete_data(table_names[choice - 1])
                continue

            else:
                display_invalid_choice_message()
                continue

        except ValueError:
            display_invalid_choice_message()
            continue