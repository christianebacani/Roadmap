'''
    Update Data Module
'''
import os
import pandas as pd
from src.utils.utils import get_the_list_of_table_names
from src.utils.utils import display_invalid_choice_message
from src.utils.utils import get_the_list_of_column_names
from src.utils.utils import init_connection
from src.utils.utils import init_engine

def update_data(table_name: str) -> None:
    '''
        Update data function to update
        a specific row based on the chosen
        table of my girlfriend's metadata
    '''
    def is_data_available_for_update_from_table(table_name: str, searched_data: dict[str, str]) -> bool:
        '''
            Search function to search the
            data if it's available for update
            from the chosen table of my girlfriend's
            metadata
        '''
        command = f'SELECT * FROM {table_name}'
        where_clause = []

        for column, data in searched_data.items():
            try:
                int(data)
                float(data)
                where_clause.append(f'{column} = {data}')

            except:
                where_clause.append(f'{column} = \'{data}\'')
        
        where_clause = ' AND '.join(where_clause)
        command = command + ' ' + 'WHERE' + ' ' + where_clause

        engine = init_engine() # Initialize SQL Alchemy Engine for PostgreSQL Database
        dataframe = pd.read_sql(command, engine)

        for column in list(searched_data.keys()):
            if list(dataframe[column]) != []:
                return True
        
        return False

    def init_sql_command_for_data_update(table_name: str, updated_data: dict[str, str]) -> str:
        '''
            Initialize function to initialize
            SQL Command for Data Update
        '''
        columns = list(updated_data.keys())
        command = f'UPDATE FROM {table_name}'
        
        set_clause = []
        where_clause = []

        for column, data in updated_data.items():
            # Check if the data can be typecasted to integer and float
            try:
                int(data)
                float(data)
                set_clause.append(f'{column} = {data}')
                where_clause.append(f'{column} = {data}')

            # We need to make sure when using string/date/time/datetime datatype values at 'SET' and 'WHERE' clause, we use open and close quotation marks    
            except:
                set_clause.append(f'{column} = \'{data}\'')
                where_clause.append(f'{column} = \'{data}\'')

        set_clause = ', '.join(set_clause)
        where_clause = ' AND '.join(where_clause)        
        command = command = ' ' + 'SET' + ' ' + set_clause + ' ' + 'WHERE' + ' ' + where_clause

        return command

    while True:
        columns = get_the_list_of_column_names(table_name) # Get the column names

        # Display Header
        print(f'\t\t', end='')
        print(f'=' * 27)
        header = 'Update Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print(f'=' * 27)

        # Dictionary to store the data to check if it's available from the table for update as a value and the column as a key
        searched_data = {}

        for column in columns:
            searched_data[column] = None

        searched_data_not_confirm = False
        invalid_confirmation = False

        # Ask for the data to check if it's available from the table for update
        for column in columns:
            data = input(f'\t\tEnter the data to search if it\'s available for update from {column} column: ')
            confirm_searched_data = input(f'\t\tDid you enter the correct data (Y/N)?: ').strip().upper()

            if confirm_searched_data == 'N':
                searched_data_not_confirm = True
                break
            
            if confirm_searched_data != 'Y':
                invalid_confirmation = True
                break
            
            if data != '':
                searched_data[column] = data

        if searched_data_not_confirm:
            os.system('cls')
            continue
        
        if invalid_confirmation:
            os.system('cls')
            print(f'\t\tInvalid confirmation! Please try again.')
            input(f'\t\tPress any key to reload the page: ')
            os.system('cls')
            continue
        
        data_available_for_update = is_data_available_for_update_from_table(table_name, searched_data) # Check if the data is available for update (The data was present to the table)

        if not data_available_for_update:
            os.system('cls')
            print(f'\t\tThe data was not available from the {table_name} table! Please try again.')
            input(f'\t\tPress any key to reload the page: ')
            os.system('cls')
            continue

        # Display Header
        os.system('cls')
        print(f'\t\t', end='')
        print(f'=' * 27)
        header = 'Update Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print(f'=' * 27)

        # Dictionary to store the update data as a value and the column as a key
        updated_data = {}

        for column in columns:
            updated_data[column] = None
        
        updated_data_not_confirm = False
        invalid_confirmation = False

        for column in columns:
            data = input(f'\t\tEnter the updated data for {column} column: ')
            confirm_updated_data = input(f'\t\tDid you enter the correct data (Y/N)?: ').strip().upper()

            if confirm_updated_data == 'N':
                updated_data_not_confirm = True
                break
            
            if confirm_updated_data != 'Y':
                invalid_confirmation = True
                break
            
            if data != '':
                updated_data[column] = data

        if updated_data_not_confirm:
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
        header = 'Updated Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print(f'=' * 28)

        # Display table name with the previous and updated data per column
        print(f'\t\tTable Name: {table_name}')
        print()

        for column, data in updated_data.items():
            print(f'\t\tColumn: {column}')
            print(f'\t\tPrevious data: {searched_data[column]}')
            print(f'\t\tUpdated data: {updated_data[column]}')
            print()

        input(f'\t\tPress any key to update the given data from the table: ')

        try:
            conn = init_connection() # Initialize a connection to the PostgreSQL Database using Pyscopg2
            cursor = conn.cursor() # # Initialize a cursor from the established connection
            command = init_sql_command_for_data_update(table_name, updated_data)
            
            cursor.execute(command)
            conn.commit()

            cursor.close()
            conn.close()

            engine = init_engine() # Initialize SQL Alchemy Engine for PostgreSQL Database
            dataframe = pd.read_sql(f'SELECT * FROM {table_name}', engine)
            dataframe.to_csv(f'data/{table_name}.csv', index=False)

            os.system('cls')
            print(f'\t\tSuccessfully updated data from {table_name} table')
            input(f'\t\tPress any key to exit page: ')
            os.system('cls')
            break
 
        except Exception as error_message:
            os.system('cls')
            print(f'\t\tError: {error_message}')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

def update_data_page() -> None:
    '''
        Update data page function to
        update a row data from the 
        chosen table of my girlfriend's 
        metadata
    '''
    while True:
        # Display Header
        print(f'\t\t', end='')
        print(f'=' * 27)
        header = 'Update Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print(f'=' * 27)

        table_names = get_the_list_of_table_names() # Get the table names

        # Display invalid message when there's no table available to be deleted
        if table_names == []:
            os.system('cls')
            print(f'\t\tCurrently there\'s no table created!')
            input(f'\t\tPress any key to exit the page: ')
            os.system('cls')
            break
    
        # Display options
        for number, table_name in enumerate(table_names):
            number += 1
            print(f'\t\t{number}.) Update a row from {table_name} table')
        
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
                update_data(table_names[choice - 1])
                continue

            else:
                display_invalid_choice_message()
                continue

        except ValueError:
            display_invalid_choice_message()
            continue