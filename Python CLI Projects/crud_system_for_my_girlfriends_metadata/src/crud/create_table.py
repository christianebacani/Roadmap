'''
    Create Table Module
'''
import os
import re

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

def create_primary_keys(table_name: str, number_of_columns: int) -> list[str]:
    '''
        Create function to create
        primary keys of the table
    '''
    while True:
        # Display header
        header = 'Create Tables'
        print(f'\t\t\t{header}\n')

        print(f'\t\tTable Name: {table_name}')
        print(f'\t\tHow many number of columns you want to create?: {number_of_columns}')

        try:
            # Ask for how many primary keys
            number_of_primary_keys = int(input(f'\t\tHow many primary keys you want to create?: '))

            # Validate number of primary keys
            if number_of_primary_keys > number_of_columns:
                os.system('cls')
                print(f'\t\tInvalid number of primary keys! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue

            confirm_number_of_primary_keys = input(f'\t\tDid you enter the correct number of primary keys?: ')

            # Validate confirmation message for the number of primary keys
            if confirm_number_of_primary_keys in ['no', 'nope', 'nah', 'n']:
                os.system('cls')
                continue
            
            if confirm_number_of_primary_keys not in ['yes', 'yeah', 'yah', 'y']:
                os.system('cls')
                print(f'\t\tInvalid choice! Please try again.')
                input('\t\tPress any key to reload page: ')
                os.system('cls')
                continue
            
            # Return the value if the user don't want to create any primary keys
            if number_of_primary_keys == 0:
                os.system('cls')
                return []

            # Ask for the primary keys
            primary_keys = []

            for number in range(number_of_primary_keys):
                number += 1
                primary_keys.append(input(f'\t\t{number}.) Primary key: '))

            confirm_primary_keys = input(f'\t\tDid you enter the correct primary keys?: ').strip().lower()

            # Validate confirmation message for primary keys
            if confirm_primary_keys in ['no', 'nope', 'nah', 'n']:
                os.system('cls')
                continue
            
            if confirm_primary_keys not in ['yes', 'yeah', 'yah', 'y']:
                os.system('cls')
                print(f'\t\tInvalid choice! Please try again.')
                input('\t\tPress any key to reload page: ')
                os.system('cls')

            # Validate primary key names
            primary_keys_are_valid = True

            for primary_key in primary_keys:
                if not re.search(r'^[A-Za-z\_]+[A-Za-z0-9\_]*$', primary_key) or (len(primary_key) < 1 or len(primary_key) > 63):
                    primary_keys_are_valid = False            
                    break

            if not primary_keys_are_valid:
                os.system('cls')
                print(f'\t\tInvalid name of primary key/s')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue

            os.system('cls')
            return primary_keys

        except:
            os.system('cls')
            print(f'\t\tInvalid number of primary keys! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

def create_columns(table_name: str, number_of_columns: int, primary_keys: list[str]) -> list[str]:
    '''
        Create function to create columns
    '''
    while True:
        if len(primary_keys) == number_of_columns:
            os.system('cls')
            return []

        # Display header
        header = 'Create Tables'
        print(f'\t\t\t{header}\n')

        print(f'\t\tTable Name: {table_name}')
        print(f'\t\tHow many number of columns you want to create?: {number_of_columns}')
        print(f'\t\tHow many primary keys you want to create?: {len(primary_keys)}')
        
        subheader = 'Creating columns'
        print(f'\n\t\t\t{subheader}\n')

        # Ask for the column names
        non_key_columns = []

        for number in range(number_of_columns - len(primary_keys)):
            number += 1
            non_key_columns.append(input(f'\t\tColumn Name: '))

        # Validate non key columns
        if len(primary_keys) == 0 and non_key_columns == []:
            os.system('cls')
            print(f'\t\tYou didn\'t create any columns! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

        confirm_non_key_columns = input(f'\t\tDid you enter the correct column names?: ').strip().lower()
            
        # Validate confirmation message for non key columns
        if confirm_non_key_columns in ['no', 'nope', 'nah', 'n']:
            os.system('cls')
            continue
            
        if confirm_non_key_columns not in ['yes', 'yeah', 'yah', 'y']:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

        # Validate non key columns
        non_key_columns_are_valid = True
    
        for non_key_column in non_key_columns:
            if not re.search(r'^[A-Za-z\_]+[A-Za-z0-9\_]*$', non_key_column) or (len(non_key_column) < 1 or len(non_key_column) > 63):
                non_key_columns_are_valid = False
                break
            
        if not non_key_columns_are_valid:
            os.system('cls')
            print(f'\t\tInvalid non key columns! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

        os.system('cls')
        return non_key_columns

def validate_table(table_metadata: dict[str, int, list[str]]) -> bool:
    '''
        Validate function to
        validate table's metadata (Table name, number of columns, primary keys, non-key columns)
        before creation
    '''
    while True:
        # Display header
        header = f'Create table'
        print(f'\t\t\t{header}\n')

        print(f'\t\tTable Name: {table_metadata['Table Name']}')
        print(f'\t\tTotal Number of Columns: {table_metadata['Total Number of Columns']}')
        
        if table_metadata['Primary Keys'] == []:
            print(f'\t\tPrimary Keys: None')
        
        else:
            print(f'\t\tPrimary Keys: {', '.join(table_metadata['Primary Keys'])}')
        
        if table_metadata['List of Column Names'] == []:
            print(f'List of Column Names: None')
        
        else:
            print(f'\t\tList of Column Names: None')
        
        print()
        confirm_table = input(f'\t\tDo you want to create this table? ').strip().lower()

        # Validate confirmation message for creating table
        if confirm_table in ['no', 'nope', 'nah', 'n']:
            os.system('cls')
            return False

        if confirm_table not in ['yes', 'yeah', 'yah', 'y']:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
        
        os.sytem('cls')
        return True

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
            'Primary Keys': [],
            'List of Column Names': []
        }

        os.system('cls')
        table_metadata['Table Name'] = create_table_name()
        table_metadata['Total Number of Columns'] = initialize_total_number_of_columns(table_metadata['Table Name'])
        table_metadata['Primary Keys'] = create_primary_keys(table_metadata['Table Name'], table_metadata['Total Number of Columns'])
        table_metadata['List of Column Names'] = create_columns(table_metadata['Table Name'], table_metadata['Total Number of Columns'], table_metadata['Primary Keys'])

        os.system('cls')
        
        if validate_table(table_metadata) is False:
            continue