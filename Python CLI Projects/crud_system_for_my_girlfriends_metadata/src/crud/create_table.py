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

        # Validate confirmation message
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
            confirm_number_of_columns = input(f'\t\tDid you enter the correct number of columns?: ').strip().lower()

            # Validate confirmation message
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

            # Validate column names
            for primary_key in primary_keys:
                # TODO: Added validation here...
    
        except:
            os.system('cls')
            print(f'\t\tInvalid number of primary keys! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

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
            'Table Name': [],
            'Total Number of Columns': [],
            'Primary Keys': [],
            'List of Column Names': []
        }
        
        os.system('cls')
        table_metadata['Table Name'] = create_table_name()
        table_metadata['Total Number of Columns'] = initialize_total_number_of_columns(table_metadata['Table Name'])
        table_metadata['Primary Keys'] = create_primary_keys(table_metadata['Table Name'], table_metadata['Total Number of Columns'])