'''
    Create Table Module
'''
import os
from src.utils.utils import display_invalid_choice_message

def create_table_name() -> str:
    '''
        Create function to create the
        table name of the new table
    '''
    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 30)
        header = 'Creating Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 30)
        print()

        table_name = input(f'\t\tTable name of the new table: ')
        confirm_table_name = input(f'\t\tDid you enter the correct table (Y/N)?: ').strip().upper()

        if confirm_table_name == 'N':
            os.system('cls')
            continue

        if confirm_table_name != 'Y':
            display_invalid_choice_message()
            continue
        
        os.system('cls')
        return table_name

def get_the_total_number_of_columns(table_name: dict[str, str | int | list]) -> int:
    '''
        Get function to get the
        total number of columns
        for the new table
    '''
    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 30)
        header = 'Creating Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 30)
        print()
        
        print(f'\t\tTable Name: {table_name['Table Name']}')
        
        try:
            number_of_columns = int(input('\t\tHow many number of columns you want to create?: '))
            
            if number_of_columns <= 0:
                display_invalid_choice_message()
                continue

            if number_of_columns >= 10:
                display_invalid_choice_message()
                continue

            confirm_number_of_columns = input(f'\t\tDid you enter the correct number of columns (Y/N)?: ').strip().upper()

            if confirm_number_of_columns == 'N':
                os.system('cls')
                continue

            if confirm_number_of_columns != 'Y':
                display_invalid_choice_message()
                continue

            os.system('cls')
            return number_of_columns

        except ValueError:
            display_invalid_choice_message()
            continue

def create_table_page() -> None:
    '''
        Create Table Page function
        to create a new table from the
        exiting database
    '''
    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 28)
        header = 'Create Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 28)
        print()

        confirm = input(f'\t\tDo you want to create a new table (Y/N)?: ').strip().upper()

        if confirm == 'N':
            os.system('cls')
            break

        if confirm != 'Y':
            display_invalid_choice_message()
            continue

        table_metadata = {
            'Table Name': '',
            'Number of Columns': 0,
            'Primary Keys': [],
            'Non-Key Columns': []
        }

        os.system('cls')
        table_metadata['Table Name'] = create_table_name()
        table_metadata['Number of Columns'] = get_the_total_number_of_columns(table_metadata)
        break