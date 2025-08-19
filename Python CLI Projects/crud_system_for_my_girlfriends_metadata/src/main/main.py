'''
    Main Module
'''
import os
from src.utils.utils import display_invalid_choice_message

def main_page() -> None:
    '''
        Main Page Function to 
        display the main page
    '''
    # Display welcome message
    print(f'\tWelcome to CLI-Based CRUD System for managing my girlfriend\'s metadata!')
    input(f'\t\tPress any key to start: ')
    os.system('cls')

    while True:
        # Display header
        header = 'Main Page'
        print(f'\t\t\t{header}\n')

        options = [
            'Start',
            'About the system',
            'Exit'
        ]
        
        # Display options
        for number, option in enumerate(options):
            number += 1
            print(f'\t\t{number}.) {option}')
        
        try:
            # Enter user choice
            print()
            choice = int(input(f'\t\tEnter your choice here: '))

            if choice == 2:
                os.system('cls')
                # TODO: Add a function from other modules here outside the 'main' package
                continue

            elif choice != 3:
                display_invalid_choice_message()
                continue
            
            else:
                os.system('cls')
                break

        except ValueError:
            display_invalid_choice_message()
            continue
            
if __name__ == '__main__':
    os.system('cls')
    main_page()