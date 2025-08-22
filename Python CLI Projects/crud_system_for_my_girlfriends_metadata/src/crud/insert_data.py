'''
    Insert Data Module
'''
import os
import pandas as pd
from src.utils.utils import display_invalid_choice_message
from src.utils.utils import get_the_list_of_table_names

def insert_data(table_name: str) -> None:
    '''
        Insert data function to insert
        new data from the chosen table
    '''
    dataframe = pd.read_csv(f'src/metadata/{table_name}.csv')
    columns = list(dataframe.columns)

    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 28)
        header = 'Insert Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 28)
        print()

        # Dictionary to store the new data as a value and column name as a key
        new_data = {}

        for column in columns:
            new_data[column] = None

        print(f'\t\tTable Name: {table_name}')
        
        inserted_data_not_confirm = False
        invalid_confirmation = False
    
        for column in columns:
            data = input(f'\t\tEnter the new data for {column} column: ')
            confirm_inserted_data = input(f'\t\tDid you enter the correct data (Y/N)?: ').strip().upper()

            if confirm_inserted_data == 'N':
                inserted_data_not_confirm = True
                break

            if confirm_inserted_data != 'Y':
                invalid_confirmation = True
                break
        
        if inserted_data_not_confirm:
            os.system('cls')
            continue

        # TODO: Add more functionalities here...

def insert_data_page() -> None:
    '''
        Insert Data Page function to
        insert new rows of data from
        the existing tables of my girlfriend's
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
            
            elif (choice >= 1 and choice <= (len(table_names) + 1)):
                os.system('cls')
                # TODO: Execute a new function here from the same module 'insert_data.py'
                continue

            else:
                display_invalid_choice_message()
                continue

        except ValueError:
            display_invalid_choice_message()
            continue            