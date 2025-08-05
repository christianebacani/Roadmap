'''
    Login Module
'''
import os

def login_page() -> None:
    '''
        CLI-Based Login Page
    '''
    while True:
        # Display header
        header = 'Login'
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
        
        choice = input(f'\n\t\tEnter your choice here: ')

        if choice != '5':
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input('\t\tPress any key to continue: ')
            os.system('cls')
            continue

        os.system('cls')
        break