'''
    Insert Data Module
'''
import os
from glob import glob

def get_table_names() -> list[str]:
    '''
        Get function to get
        the list of table names
    '''
    result = []

    for csv_file in glob(f'src/metadata/*.csv'):
        csv_file = str(csv_file).replace('\\', '/')
        table_name = str(csv_file).replace('src/metadata/', '').replace('.csv', '')

        if table_name not in result:
            result.append(table_name)

    return result

def insert_data_main_page() -> None:
    '''
        CLI-Based Main Page for Inserting
        Data to Table
    '''
    while True:
        # Display header
        header = 'Insert Data'
        print(f'\t\t\t{header}\n')

        list_of_table_names = get_table_names()

        for number, table_name in enumerate(list_of_table_names):
            number += 1
            print(f'\t\t{number}.) Insert data to {table_name} table')

        print(f'\t\t{len(list_of_table_names) + 1}.) Exit')

        try:
            choice = int(input(f'\n\t\tEnter your choice here: '))

            if choice <= 0:
                os.system('cls')
                print(f'\t\tInvalid choice! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue

            if choice == (len(list_of_table_names) + 1):
                os.system('cls')
                break
            
            chosen_table_name = list_of_table_names[choice - 1]
            os.system('cls')
            continue

        except:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue