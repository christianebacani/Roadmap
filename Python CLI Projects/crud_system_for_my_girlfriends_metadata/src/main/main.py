'''
    Main Module
'''
import os
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
from src.crud.crud import crud_page
from src.main.about import about_page

def main_page() -> None:
    '''
        Implement a CLI-Based Main Page
    '''
    while True:
        # Display header
        header = 'CRUD CLI-Based System for Managing Rica\'s Metadata'
        print(f'\t\t{header}\n')

        # Display options
        options = [
            'Start',
            'About',
            'Exit'
        ]
        for number, option in enumerate(options):
            print(f'\t\t\t{number + 1}.) {option}')

        choice = input('\n\t\tEnter your choice here: ').strip()

        if choice == '1':
            os.system('cls')
            crud_page()
            os.system('cls')

        elif choice == '2':
            os.system('cls')
            about_page()
            os.system('cls')

        elif choice == '3':
            os.system('cls')
            break

        else:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

if __name__ == '__main__':
    os.system('cls')
    main_page()