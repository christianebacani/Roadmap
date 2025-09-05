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

def get_the_total_number_of_columns(table_metadata: dict[str, str | int | dict[str, str]]) -> int:
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
        
        print(f'\t\tTable Name: {table_metadata['Table Name']}')

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

def create_primary_keys(table_metadata: dict[str, str | int | dict[str, str]]) -> dict[str, str]:
    '''
        Create function to create
        primary keys for the new table
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
        
        print(f'\t\tTable Name: {table_metadata['Table Name']}')
        print(f'\t\tNumber of Columns: {table_metadata['Number of Columns']}')

        try:
            number_of_primary_keys = int(input(f'\t\tHow many number of primary keys you want to create?: '))

            if number_of_primary_keys < 0:
                display_invalid_choice_message()
                continue

            if number_of_primary_keys == 0:
                os.system('cls')
                return {}

            if number_of_primary_keys > table_metadata['Number of Columns']:
                display_invalid_choice_message()
                continue
            
            confirm_number_of_primary_keys = input(f'\t\tDid you enter the correct number of primary keys (Y/N)?: ').strip().upper()

            if confirm_number_of_primary_keys == 'N':
                os.system('cls')
                continue

            if confirm_number_of_primary_keys != 'Y':
                display_invalid_choice_message()
                continue

            # Display header
            os.system('cls')
            print(f'\t\t', end='')
            print('=' * 30)
            header = 'Creating Table'
            print(f'\t\t\t{header}')
            print(f'\t\t', end='')
            print('=' * 30)
            print()

            datatypes = [
                'INTEGER',
                'VARCHAR',
                'CHAR',
                'FLOAT'
            ]
            
            primary_key_not_confirm = False
            invalid_confirmation = False
            invalid_character_size = False
            invalid_floating_point_size = False

            for _ in range(number_of_primary_keys):
                primary_key = input(f'\t\tEnter your primary key here: ')
                confirm_primary_key = input(f'\t\tDid you enter the correct primary key (Y/N)?; ').strip().upper()

                if confirm_primary_key == 'N':
                    primary_key_not_confirm = True
                    break
                
                if confirm_primary_key != 'Y':
                    invalid_confirmation = True
                    break
                
                print()

                for number, datatype in enumerate(datatypes):
                    number += 1
                    print(f'\t\t\t{number}.) {datatype}')

                chosen_datatype = int(input(f'\t\tEnter the datatype of {primary_key} primary key: '))

                if datatypes[chosen_datatype - 1] in ['VARCHAR', 'CHAR']:
                    size = input(f'\t\tEnter the size of character from {primary_key} primary key: ')
                
                elif datatypes[chosen_datatype - 1] == 'FLOAT':
                    size = input(f'\t\tEnter the floating-point size of {primary_key} primary key: ')
                    decimal_digits = input(f'\t\tEnter the decimal digits of {primary_key} primary key: ')

                else:
                    pass

                if (datatypes[chosen_datatype - 1] in ['VARCHAR', 'CHAR']) and (int(size) <= 0 or int(size) > 255):
                    invalid_character_size = True
                    break
                
                if (datatype[chosen_datatype - 1] == 'FLOAT') and (int(size) <= 0 or int(size) > 32):
                    invalid_floating_point_size = True
                    break
                
                # TODO: Add more validations here...

            if primary_key_not_confirm:
                os.system('cls')
                continue

            if invalid_confirmation:
                display_invalid_choice_message()
                continue

            if invalid_character_size:
                os.system('cls')
                print(f'\t\tInvalid character size! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue
                
            if invalid_floating_point_size:
                os.system('cls')
                print(f'\t\tInvalid floating-point size! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue

        except Exception as error_message:
            print(f'\t\tError message: {error_message}')
            continue

def create_non_key_columns(table_metadata: dict[str, str | int | dict[str, str]]) -> dict[str, str]:
    '''
        Create function to
        create non-key columns
        for new table
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

        print(f'\t\tTable Name: {table_metadata['Table Name']}')
        
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
            'Primary Keys': {},
            'Non-Key Columns': {}
        }

        os.system('cls')
        table_metadata['Table Name'] = create_table_name()
        table_metadata['Number of Columns'] = get_the_total_number_of_columns(table_metadata)
        table_metadata['Primary Keys'] = create_primary_keys(table_metadata)
        break