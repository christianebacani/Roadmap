'''
    CRUD Module
'''
import os
from src.utils.utils import display_invalid_choice_message
from src.crud.create_table import create_table_page
from src.crud.insert_data import insert_data_page
from src.crud.read_data import read_data_page
from src.crud.update_data import update_data_page
from src.crud.delete_data import delete_data_page
from src.crud.delete_table import delete_table_page

def crud_page() -> None:
    '''
        CRUD Page function to
        display functionality
        about options for managing
        metadata using CRUD
    '''
    while True:
        # Display header
        print('\t\t', end='')
        print('=' * 25)
        header = 'CRUD Page'
        print(f'\t\t\t{header}')
        print('\t\t', end='')
        print('=' * 25)
        print()

        options = [
            'Create Table',
            'Insert Data',
            'Read Data',
            'Update Data',
            'Delete Data',
            'Delete Table',
            'Exit'
        ]

        # Display options
        for number, option in enumerate(options):
            number += 1
            print(f'\t\t{number}.) {option}')

        try:
            choice = int(input(f'\n\t\tEnter your choice here: '))

            if choice == 1:
                os.system('cls')
                create_table_page()
                continue

            elif choice == 2:
                os.system('cls')
                insert_data_page()
                continue

            elif choice == 3:
                os.system('cls')
                read_data_page()
                continue
            
            elif choice == 4:
                os.system('cls')
                update_data_page()
                continue

            elif choice == 5:
                os.system('cls')
                delete_data_page()
                continue
            
            elif choice == 6:
                os.system('cls')
                delete_table_page()
                continue
            
            elif choice == 7:
                os.system('cls')
                break
            
            else:
                display_invalid_choice_message()
                continue

        except ValueError:
            display_invalid_choice_message()
            continue