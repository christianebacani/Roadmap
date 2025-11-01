'''
    Main Page Module
'''
import os
import sys
sys.path.insert(0, os.path.abspath('src'))
from home.home import display_home_page

def display_main_page() -> None:
    '''
        Function to display main page
        when running the system.
    '''
    os.system('cls')
    print('\t\t\tWelcome to Lourdes Hardware Shop Catalog System!')
    input('\t\t\t\tPress any key to start: ')
    display_home_page()

if __name__ == '__main__':
    display_main_page()