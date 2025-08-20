'''
    Main Module
'''
import os
from src.utils.utils import display_invalid_choice_message
from src.about_the_system.about_the_system import about_the_system_page

def main_page() -> None:
    '''
        Main Page Function to 
        display the main page
    '''
    while True:
        # Display header
        print('\t\t', end='')
        print('=' * 25)
        header = 'Main Page'
        print(f'\t\t\t{header}')
        print('\t\t', end='')
        print('=' * 25)
        print()

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

            if choice == 1:
                os.system('cls')
                # TODO: Execute a function here from other module outsidee 'main' package
                continue
                
            elif choice == 2:
                os.system('cls')
                about_the_system_page()
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