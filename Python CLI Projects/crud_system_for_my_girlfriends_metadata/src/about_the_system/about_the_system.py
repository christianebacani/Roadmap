'''
    About the system Module
'''
def about_the_system_page() -> None:
    '''
        About the system page
        to display the facts
        about this CLI-based system
    '''
    # Display header
    print('=' * 25)
    header = 'About this system'
    print(f'\t\t\t{header}')
    print('=' * 25)
    print()

    # Messages stored in list
    messages = [
        'This command-line interface (CLI) was not built to manage data,',
        'it was built to manage my heart.',
        'Since you are the most important project in my life, it only makes',
        'sense that I\'d write a program to organize to organize the metadata',
        'f our relationship. This system ensures vital information from-your',
        'favorite books, series, colors, etc.',
        'It\'s a CRUD system for the most incredible, unique, and dazzling',
        'database I know: you.',
        '\n',
        'Developed by Tangalog'
    ]
    # TODO: Add more functionalities here...