'''
    Create Table Module
'''
import os

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

        # Validate table name
        if confirm_table_name in ['no', 'nope', 'nah', 'n']:
            os.system('cls')
            continue

        if confirm_table_name not in ['yes', 'yeah', 'yah', 'y']:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input('\t\tPress any key to continue: ')
            os.system('cls')
            continue

        os.system('cls')
        return table_name

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
            input('\t\tPress any key to continue: ')
            os.system('cls')
            continue
        
        # Initialize a dictionary store the metadata of the table that the user wants to create
        table_metadata = {
            'Table Name': [],
            'Primary Key Name': [],
            'Total Number of Columns': [],
            'List of Column Names': []
        }
        os.system('cls')
        table_metadata['Table Name'] = create_table_name()