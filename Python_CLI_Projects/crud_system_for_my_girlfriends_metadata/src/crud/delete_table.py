'''
    Delete Table Module
'''
import os
from src.utils.utils import get_the_list_of_table_names
from src.utils.utils import display_invalid_choice_message
from src.utils.utils import init_connection

def delete_table(table_name: str) -> None:
    '''
        Delete table function to delete
        based on the chosen specific table
        of my girlfriend's metadata
    '''
    while True:
        # Display Header
        print(f'\t\t', end='')
        print(f'=' * 28)
        header = 'Delete Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print(f'=' * 28)
        print()

        confirm_delete_table = input(f'\t\tAre you sure you want to delete {table_name} table (Y/N)?: ').strip().upper()

        if confirm_delete_table == 'N':
            os.system('cls')
            break

        if confirm_delete_table != 'Y':
            display_invalid_choice_message()
            continue

        conn = init_connection() # Initialize a connection to the PostgreSQL Database using Pyscopg2
        cursor = conn.cursor() # # Initialize a cursor from the established connection
        
        cursor.execute(f'DROP TABLE {table_name};')
        conn.commit()

        cursor.close()
        conn.close()

        os.remove(f'src/data/{table_name}.csv')

        os.system('cls')
        print(f'\t\tSuccessfully deleted {table_name} table!')
        input(f'\t\tPress any key to exit page: ')
        os.system('cls')
        break

def delete_table_page() -> None:
    '''
        Delete table page function
        to delete a chosen table from
        my girlfriend's metadata
    '''
    while True:
        # Display Header
        print(f'\t\t', end='')
        print(f'=' * 28)
        header = 'Delete Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print(f'=' * 28)
        print()

        table_names = get_the_list_of_table_names() # Get the table names

        # Display invalid message when there's no table available to be deleted
        if table_names == []:
            os.system('cls')
            print(f'\t\tCurrently there\'s no table created!')
            input(f'\t\tPress any key to exit the page: ')
            os.system('cls')
            break
        
        # Display options
        for number, table_name in enumerate(table_names):
            number += 1
            print(f'\t\t{number}.) Delete {table_name} table')
        
        # Display exit option
        last_number = len(table_names) + 1
        print(f'\t\t{last_number}.) Exit')

        try:
            choice = int(input(f'\n\t\tEnter your choice here: '))

            if choice == last_number:
                os.system('cls')
                break

            elif (choice >= 1) and (choice <= len(table_names)):
                os.system('cls')
                delete_table(table_names[choice - 1])
                continue

            else:
                display_invalid_choice_message()
                continue

        except ValueError:
            display_invalid_choice_message()
            continue