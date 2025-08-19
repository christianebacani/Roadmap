'''
    Utilities Module
'''
import os

def display_invalid_choice_message() -> None:
    '''
        Display function to display
        invalid choice message
    '''
    os.system('cls')
    print(f'\t\tInvalid choice! Please try again.')
    input(f'\t\tPress any key to reload page: ')
    os.system('cls')