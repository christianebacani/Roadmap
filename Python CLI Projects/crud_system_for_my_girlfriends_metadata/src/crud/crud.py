'''
    Login Module
'''
import os
from src.crud.create_table import create_table_main_page
from src.crud.insert_data import insert_data_main_page
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
            'Insert data',
            'Display table',
            'Update row/table',
            'Delete row/table',
            'Exit'
        ]
        for number, option in enumerate(options):
            print(f'\t\t{number + 1}.) {option}')
        
        try:
            choice = int(input(f'\n\t\tEnter your choice here: '))

            if choice == 1:
                os.system('cls')
                create_table_main_page()
                continue

            elif choice == 2:
                os.system('cls')
                insert_data_main_page()
                continue

            elif choice == 3:
                os.system('cls')
                read_table_main_page()
                continue

            elif choice != 6:
                os.system('cls')
                print(f'\t\tInvalid choice! Please try again.')
                input('\t\tPress any key to continue: ')
                os.system('cls')
                continue

            os.system('cls')
            break
        
        except:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue