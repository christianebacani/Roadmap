'''
    Home Page Module
'''
import os
from utils.utils import display_invalid_choice_message

def display_home_page() -> None:
    '''
        Function to display home page
        after displaying the main page.
    '''
    options = [
        'Encode new material/s',
        'Search existing material/s',
        'Display existing materials',
        'Update existing material/s',
        'Delete existing material/s',
        'Enter cashier mode',
        'Generate reports',
        'Exit'
    ]

    while True:
        os.system('cls')
        header = '\t\t\tLourdes Hardware Shop Catalog System'
        print(header)
        print()

        for number, option in enumerate(options):
            print(f'\t\t\t{number + 1}. {option}')

        try:
            print()
            choice = int(input('\t\t\tEnter your choice here: '))

            if choice == 8:
                os.system('cls')
                break

        except ValueError:
            os.system('cls')
            display_invalid_choice_message()