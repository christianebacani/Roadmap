'''
    Read Table Module
'''
import os
import pandas as pd
from src.utils.utils import init_engine
from src.utils.utils import get_table_names

def display_table(table_name: str) -> None:
    '''
        Display function to 
        display chosen table
    '''
    engine = init_engine()
    # Query using SQL Alchemy Engine
    dataframe = pd.read_sql(f'SELECT * FROM {table_name}', engine)

    print(dataframe)
    input('\n\t\tPress any key to exit: ')

def read_table_main_page() -> None:
    '''
        CLI-Based Main Page for Reading Tables
    '''
    while True:
        # Display header
        header = 'Read Tables'
        print(f'\t\t\t{header}\n')

        # Display options
        options = get_table_names()
        for number, option in enumerate(options):
            print(f'\t\t\t{number + 1}.) Read {option} table')
        
        print(f'\t\t\t{len(options) + 1}.) Exit')

        try:
            choice = int(input('\n\t\tEnter your choice here: ').strip())
            
            if choice < 1 or choice > (len(options) + 1):
                os.system('cls')
                print(f'\t\tInvalid choice! Please try again.')
                input('\t\tPress any key to continue: ')
                os.system('cls')
                continue

            if choice == (len(options) + 1):
                os.system('cls')
                break
    
            os.system('cls')
            display_table(options[int(choice) - 1])
            os.system('cls')
            continue

        except:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input('\t\tPress any key to continue: ')
            os.system('cls')
            continue