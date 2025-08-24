'''
    Read Data Module
'''
import os
import pandas as pd
from src.utils.utils import display_invalid_choice_message
from src.utils.utils import get_the_list_of_table_names
from src.utils.utils import init_connection

def read_data(table_name: str) -> None:
    '''
        Read data function to display
        the data, based on the table_name parameter
    '''
    conn = init_connection() # Initialize a connection to the PostgreSQL Database using Pyscopg2
    dataframe = pd.read_sql(f'SELECT * FROM {table_name}', conn)
    print(dataframe)

    input(f'\n\t\tPress any key to exit page: ')
    os.system('cls')
    
    conn.close()

def read_data_page() -> None:
    '''
        Read Data Page function to
        read data from chosen table 
        of my girlfriend's metadata
    '''
    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 26)
        header = 'Read Data'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 26)
        print()

        table_names = get_the_list_of_table_names() # Get the table names

        # Display invalid message when there's no table available to display
        if table_names == []:
            os.system('cls')
            print(f'\t\tCurrently there\'s no table created!')
            input(f'\t\tPress any key to exit the page: ')
            os.system('cls')
            break

        # Display options
        for number, table_name in enumerate(table_names):
            number += 1
            print(f'\t\t{number}.) Display {table_name} table')

        # Display exit option
        last_number = len(table_names) + 1
        print(f'\t\t{last_number}.) Exit')

        try:
            choice = int(input('\n\t\tEnter your choice here: '))

            if choice == last_number:
                os.system('cls')
                break

            elif (choice >= 1 and choice <= (len(table_names) + 1)):
                os.system('cls')
                read_data(table_names[choice - 1])
                continue

            else:
                display_invalid_choice_message()
                continue
            
        except ValueError:
            display_invalid_choice_message()
            continue