'''
    Login Module
'''
import os
from src.crud.read_table import read_table_main_page

def crud_page() -> None:
    '''
        CLI-Based CRUD Main Page
    '''
    while True:
        # Display header
        header = 'CRUD Main Page'
        print(f'\t\t\t{header}\n')

        # Display options
        options = [
            'Create table',
            'Display table',
            'Update table',
            'Delete table',
            'Exit'
        ]
        for number, option in enumerate(options):
            print(f'\t\t\t{number + 1}.) {option}')
        
        choice = input(f'\n\t\tEnter your choice here: ').strip()

        if choice == '1':
            os.system('cls')

        elif choice == '2':
            os.system('cls')
            read_table_main_page()
            continue

        elif choice != '5':
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input('\t\tPress any key to continue: ')
            os.system('cls')
            continue

        os.system('cls')
        break