'''
    Utilities Module
'''
import os
from glob import glob

def display_invalid_choice_message() -> None:
    '''
        Display function to display
        invalid choice message
    '''
    os.system('cls')
    print(f'\t\tInvalid choice! Please try again.')
    input(f'\t\tPress any key to reload page: ')
    os.system('cls')

def get_the_list_of_table_names() -> list[str]:
    '''
        Get function to get the
        list of table names by 
        reading the file names
        from 'metadata' directory
    '''
    result = []

    for csv_file in glob(f'src/metadata/*.csv'):
        csv_file = str(csv_file).replace('\\', '/')
        table_name = str(csv_file).replace('src/metadata/', '').replace('.csv', '')
        result.append(table_name)

    return result