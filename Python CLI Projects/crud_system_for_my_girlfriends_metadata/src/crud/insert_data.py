'''
    Insert Data Module
'''
import os
import re
import pandas as pd
from glob import glob
from datetime import datetime
from src.utils.utils import init_connection
from src.utils.utils import init_engine

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

def insert_data_to_chosen_table(table_name: str) -> None:
    '''
        Insert function to insert
        new data to chosen table  
    '''
    def init_ddl_command_for_data_insertion(table_name: str, inserted_data: dict[str, str]) -> str:
        '''
            Initialize function to initialize
            DDL (Data Definition Language) 
            command for data insertion to the
            chosen table
        '''
        columns = []

        for column in list(inserted_data.keys()):
            columns.append(column)
        
        columns = ', '.join(columns)
        result = f'INSERT INTO {table_name} ({columns})'

        values = []

        for value in list(inserted_data.values()):
            if value is None:
                values.append(None)
                continue

            try:
                int(value)
                float(value)
                values.append(value)
            
            except:
                values.append(f'\'{value}\'')
        
        values = ', '.join(values)
        result = result + ' ' + f'VALUES ({values})'

        return result

    while True:
        # Display header
        header = 'Insert Data'
        print(f'\t\t\t{header}\n')

        dataframe = pd.read_csv(f'src/metadata/{table_name}.csv')
        list_of_columns = list(dataframe.columns)
        inserted_data = {}
        
        inserted_is_correct = True
        valid_confirmation_message = True
    
        for column in list_of_columns:
            inserted_data[column]= input(f'\t\tEnter new data for {column} column: ')
            confirm_inserted_data = input(f'\t\tDid you enter the correct data?: ').strip().lower()
 
            # Validate confirmation message for inserted data
            if confirm_inserted_data in ['no', 'nope', 'nah', 'n']:
                inserted_is_correct = False
                break
            
            if confirm_inserted_data not in ['yes', 'yeah', 'yah', 'y']:
                valid_confirmation_message = False
                break

        if not inserted_is_correct:
            os.system('cls')
            continue
        
        if not valid_confirmation_message:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

        # Validate inserted data
        number_of_missing_values = 0

        for column, data in inserted_data.items():
            if (str(data).strip() == '') or (str(data).strip().lower() in ['none', 'nan', 'n/a']):
                number_of_missing_values += 1

        if number_of_missing_values == len(list_of_columns):
            os.system('cls')
            print(f'\t\tAll columns consist of null values! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue

        os.system('cls')
        # Display header again
        print(f'\t\t\t{header}\n')

        print(f'\t\tTable: {table_name}')
        print()

        for column, data in inserted_data.items():
            if (str(data).strip() == '') or (str(data).strip().lower() in ['none', 'nan', 'n/a']):
                inserted_data[column] = None

            print(f'\t\tColumn: {column}')
            print(f'\t\tData: {data}')
            print()
        
        input(f'\t\tPress any key to insert the given data: ')
        
        try:
            conn = init_connection()
            cursor = conn.cursor()

            command = init_ddl_command_for_data_insertion(table_name, inserted_data)
            cursor.execute(command)
            conn.commit() # Commit the changes

            engine = init_engine()
            dataframe = pd.read_sql(f'SELECT * FROM {table_name}', engine)
            dataframe.to_csv(f'src/metadata/{table_name}.csv', index=False) # Update the csv file

            cursor.close()
            conn.close()

        except Exception as error_message:
            os.system('cls')
            print(f'\t\tError inserting to table: {table_name}')
            print(f'\t\tError message: {error_message}')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue
        
        os.system('cls')
        break

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
            insert_data_to_chosen_table(chosen_table_name)

            print(f'\t\tSuccessfully inserted data to table: {table_name}')
            input(f'\t\tPress any key to exit page: ')
            os.system('cls')
            break

        except:
            os.system('cls')
            print(f'\t\tInvalid choice! Please try again.')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue