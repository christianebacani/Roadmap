'''
    Create Table Module
'''
import os
import re
from src.utils.utils import init_cursor

def create_table_name() -> str:
    '''
        Create function to create
        the table name
    '''
    while True:
        # Display header
        header = 'Create Tables'
        print(f'\t\t\t{header}\n')

        # Ask for table name
        table_name = input(f'\t\tTable Name: ').strip().lower()
        confirm_table_name = input(f'\t\tDid you enter the correct table name?: ').strip().lower()

        # Validate confirmation message for table name
        if confirm_table_name in ['no', 'nope', 'nah', 'n']:
            os.system('cls')
            continue

        if confirm_table_name not in ['yes', 'yeah', 'yah', 'y']:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input('\t\tPress any key to reload page: ')
            os.system('cls')
            continue
        
        # Validation of table name
        if not re.search(r'^[A-Za-z\_]+[A-Za-z0-9\_]*$', table_name) or (len(table_name) < 1 or len(table_name) > 63):
            os.system('cls')
            print('\t\tInvalid table name!')
            input('\t\tPress any key to reload page: ')
            os.system('cls')
            continue

        os.system('cls')
        return table_name

def initialize_total_number_of_columns(table_name: str) -> int:
    '''
        Create function to initialize 
        the total number of columns        
    '''
    while True:
        # Display header
        header = 'Create Tables'
        print(f'\t\t\t{header}\n')

        print(f'\t\tTable Name: {table_name}')

        try:
            # Ask for total number of columns
            number_of_columns = int(input(f'\t\tHow many number of columns you want to create?: '))

            # Validate total number of columns
            if number_of_columns == 0 or number_of_columns > 10:
                os.system('cls')
                print(f'\t\tInvalid number of columns! Please try again.')
                input('\t\tPress any key to reload page: ')
                os.system('cls')
                continue

            confirm_number_of_columns = input(f'\t\tDid you enter the correct number of columns?: ').strip().lower()

            # Validate confirmation message for number of columns
            if confirm_number_of_columns in ['no', 'nope', 'nah', 'n']:
                os.system('cls')
                continue
    
            if confirm_number_of_columns not in ['yes', 'yeah', 'yah', 'y']:
                os.system('cls')
                return number_of_columns

        except:
            os.system('cls')
            print(f'\t\tInvalid number of columns! Please try again.')
            input('\t\tPress any key to reload page: ')
            os.system('cls')
            continue

def create_primary_keys(table_name: str, number_of_columns: int) -> dict[str, str]:
    '''
        Create function to create
        primary keys
    '''
    def init_primary_keys_with_datatype(number_of_primary_keys: str, available_datatypes: list[str]) -> dict[str, str]:
        '''
            Initialize function to
            initialize primary keys
            and their data type
        '''
        while True:
            # Display subheader
            subheader = 'Create Primary Keys'
            print(f'\n\t\t\t{subheader}\n')

            primary_keys_are_valid = True
            primary_keys_datatype_are_valid = True
            result = {}

            for number in range(number_of_primary_keys):
                number += 1
                primary_key = input(f'\t\tPrimary Key Name: ')

                # Validate primary key
                if not re.search(r'^[A-Za-z\_]+[A-Za-z0-9\_]*$', primary_key) or (len(primary_key) < 1 or len(primary_key) > 63):
                    primary_keys_are_valid = False
                    break

                print()

                for datatype_number, datatype in enumerate(available_datatypes):
                    datatype_number += 1
                    print(f'\t\t\t{datatype_number}.) {datatype}')

                # Validate chosen datatype
                try:
                    chosen_datatype = int(input(f'\n\t\tChoose the datatype of {primary_key}: '))
                    result[primary_key] = available_datatypes[chosen_datatype - 1]

                except:
                    primary_keys_datatype_are_valid = False
                    break

            if not primary_keys_are_valid:
                os.system('cls')
                print(f'\t\tInvalid primary key name! Please try again.')
                input(f'\t\tPress any key to reload page ')
                os.system('cls')
                continue

            if not primary_keys_datatype_are_valid:
                os.system('cls')
                print(f'\t\tInvalid primary key datatype! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue
            
            os.system('cls')
            return result

    available_datatypes = [
        'INTEGER',
        'CHAR',
        'VARCHAR',
        'DATE',
        'TIMESTAMP'
    ]

    while True:
        # Display header
        header = 'Create Tables'
        print(f'\t\t\t{header}\n')

        print(f'\t\tTable Name: {table_name}')
        print(f'\t\tHow many number of columns you want to create?: {number_of_columns}')
        
        try:
            number_of_primary_keys = int(input(f'\t\tHow many number of primary keys you want to create?: '))

            # Return immediately if the user does not want any primary keys
            if number_of_primary_keys == 0:
                os.system('cls')
                return {}

            # Validate number of primary keys
            if number_of_primary_keys > number_of_columns:
                os.system('cls')
                print(f'\t\tInvalid number of primary keys! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')

            confirm_number_of_primary_keys = input(f'\t\tDid you enter the correct number of primary keys?: ').strip().lower()

            # Validate confirmation message for the number of primary keys
            if confirm_number_of_primary_keys in ['no', 'nope', 'nah', 'n']:
                os.system('cls')
                continue

            if confirm_number_of_primary_keys not in ['yes', 'yeah', 'yah', 'y']:
                os.system('cls')
                print(f'\t\tInvalid choice! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')

            os.system('cls')
            primary_keys = init_primary_keys_with_datatype(number_of_primary_keys, available_datatypes)

            # Display subheader
            subheader = 'Create Primary Keys'
            print(f'\t\t\t{subheader}\n')

            for primary_key, datatype in primary_keys.items():
                print(f'\t\tPrimary Key: {primary_key}')
                print(f'\t\tData Type: {datatype}')
                print()
            
            confirm_primary_keys = input(f'\t\tDid you enter the correct primary keys and datatype?: ').strip().lower()
            
            # Validate confirmation message for primary keys
            if confirm_primary_keys in ['no', 'nope', 'nah', 'n']:
                os.system('cls')
                continue
            
            if confirm_primary_keys not in ['yes', 'yeah', 'yah', 'y']:
                os.system('cls')
                print(f'\t\tInvalid choice! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
            
            os.system('cls')
            return primary_keys

        except:
            os.system('cls')
            print(f'\t\tInvalid number of primary keys! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')

def create_non_key_columns(table_name: str, number_of_columns: int, primary_keys: dict[str, str]) -> dict[str, str]:
    '''
        Create function to create
        non-key columns
    '''
    while True:
        # Display header
        header = 'Create Tables'
        print(f'\t\t\t{header}\n')

        print(f'\t\tTable Name: {table_name}')
        print(f'\t\tHow many number of columns you want to create?: {number_of_columns}')
        print(f'\t\tHow many number of primary keys you want to create?: {len(list(primary_keys.keys()))}')

        if primary_keys != {}:
            subheader = 'Primary Keys'
            print(f'\n\t\t\t{subheader}\n')

            for primary_key, data_type in primary_keys.items():
                print(f'\t\tPrimary Key: {primary_key}')
                print(f'\t\tData Type: {data_type}')
                print()

        try:
            number_of_non_key_columns = int(input(f'\t\tHow many number of non-key columns you want to create?: '))

            # Validate number of non-key columns
            if (len(list(primary_keys.keys())) + number_of_non_key_columns) <= 0:
                os.system('cls')
                print(f'\t\tInvalid number of non-key columns! Please try again.')
                print(f'\t\tPress any key to reload page: ')
                os.system('cls')

        except:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')

def create_table_main_page() -> None:
    '''
        CLI-Based Main Page for Creating Tables
    '''
    while True:
        # Confirmation message
        confirm = input('\t\tDo you want to create a new table?: ').strip().lower()

        # Validation for confirmation message
        if confirm in ['no', 'nope', 'nah', 'n']:
            os.system('cls')
            break

        if confirm not in ['yes', 'yeah', 'yah', 'y']:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input('\t\tPress any key to reload page: ')
            os.system('cls')
            continue
        
        # Initialize a dictionary store the metadata of the table that the user wants to create
        table_metadata = {
            'Table Name': '',
            'Total Number of Columns': 0,
            'Primary Keys': {},
            'List of Column Names': {}
        }

        os.system('cls')
        table_metadata['Table Name'] = create_table_name()
        table_metadata['Total Number of Columns'] = initialize_total_number_of_columns(table_metadata['Table Name'])
        table_metadata['Primary Keys'] = create_primary_keys(table_metadata['Table Name'], table_metadata['Total Number of Columns'])