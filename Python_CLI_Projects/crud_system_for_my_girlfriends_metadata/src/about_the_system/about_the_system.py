'''
    About the system Module
'''
import os

def about_the_system_page() -> None:
    '''
        About the system page
        to display the facts
        about this CLI-based system
    '''
    # Display header
    print(f'\t\t', end='')
    print('=' * 35)
    header = 'About this system'
    print(f'\t\t\t{header}')
    print(f'\t\t', end='')
    print('=' * 35)
    print()

    # Messages stored in list
    messages = [
        'This command-line interface (CLI) was not built to manage data,',
        'it was built to manage my heart.',
        'Since you are the most important project in my life, it only makes',
        'sense that I\'d write a program to organize to organize the metadata',
        'for our relationship. This system ensures vital information from-your',
        'favorite books, series, colors, etc.',
        'It\'s a CRUD system for the most incredible, unique, and dazzling',
        'database I know: you.'
    ]
    
    # Display messages about the system
    for message in messages:
        print(f'\t\t{message}')
    
    print()
    input(f'\t\tPress any key to exit the page: ')
    os.system('cls')