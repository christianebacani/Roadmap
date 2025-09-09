'''
    Create Table Module
'''
import os
import pandas as pd
from src.utils.utils import display_invalid_choice_message
from src.utils.utils import init_connection
from src.utils.utils import init_engine

def create_table_name() -> str:
    '''
        Create function to create the
        table name of the new table
    '''
    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 30)
        header = 'Creating Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 30)
        print()

        table_name = input(f'\t\tTable name of the new table: ')
        confirm_table_name = input(f'\t\tDid you enter the correct table (Y/N)?: ').strip().upper()

        if confirm_table_name == 'N':
            os.system('cls')
            continue

        if confirm_table_name != 'Y':
            display_invalid_choice_message()
            continue
        
        os.system('cls')
        return table_name

def get_the_total_number_of_columns(table_metadata: dict[str, str | int | dict[str, str]]) -> int:
    '''
        Get function to get the
        total number of columns
        for the new table
    '''
    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 30)
        header = 'Creating Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 30)
        print()
        
        print(f'\t\tTable Name: {table_metadata['Table Name']}')

        try:
            number_of_columns = int(input('\t\tHow many number of columns you want to create?: '))
            
            if number_of_columns <= 0:
                display_invalid_choice_message()
                continue

            if number_of_columns >= 10:
                display_invalid_choice_message()
                continue

            confirm_number_of_columns = input(f'\t\tDid you enter the correct number of columns (Y/N)?: ').strip().upper()

            if confirm_number_of_columns == 'N':
                os.system('cls')
                continue

            if confirm_number_of_columns != 'Y':
                display_invalid_choice_message()
                continue

            os.system('cls')
            return number_of_columns

        except ValueError:
            display_invalid_choice_message()
            continue

def create_primary_keys(table_metadata: dict[str, str | int | dict[str, str]]) -> dict[str, str]:
    '''
        Create function to create
        primary keys for the new table
    '''
    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 30)
        header = 'Creating Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 30)
        print()
        
        print(f'\t\tTable Name: {table_metadata['Table Name']}')
        print(f'\t\tNumber of Columns: {table_metadata['Number of Columns']}')

        try:
            number_of_primary_keys = int(input(f'\t\tHow many number of primary keys you want to create?: '))

            if number_of_primary_keys < 0:
                display_invalid_choice_message()
                continue

            if number_of_primary_keys == 0:
                os.system('cls')
                return {}

            if number_of_primary_keys > table_metadata['Number of Columns']:
                display_invalid_choice_message()
                continue
            
            confirm_number_of_primary_keys = input(f'\t\tDid you enter the correct number of primary keys (Y/N)?: ').strip().upper()

            if confirm_number_of_primary_keys == 'N':
                os.system('cls')
                continue

            if confirm_number_of_primary_keys != 'Y':
                display_invalid_choice_message()
                continue

            # Display header
            os.system('cls')
            print(f'\t\t', end='')
            print('=' * 30)
            header = 'Creating Table'
            print(f'\t\t\t{header}')
            print(f'\t\t', end='')
            print('=' * 30)
            print()

            datatypes = [
                'INTEGER',
                'VARCHAR',
                'CHAR',
                'FLOAT'
            ]
            primary_keys_and_datatype = {}

            primary_key_not_confirm = False
            invalid_confirmation = False
            invalid_character_size = False
            invalid_floating_point_size = False
            invalid_floating_point_decimal_digits = False
            chosen_datatype_not_confirm = False

            for _ in range(number_of_primary_keys):
                primary_key = input(f'\t\tEnter your primary key here: ')
                confirm_primary_key = input(f'\t\tDid you enter the correct primary key (Y/N)?: ').strip().upper()

                if confirm_primary_key == 'N':
                    primary_key_not_confirm = True
                    break
                
                if confirm_primary_key != 'Y':
                    invalid_confirmation = True
                    break
                
                print()

                for number, datatype in enumerate(datatypes):
                    number += 1
                    print(f'\t\t\t{number}.) {datatype}')

                chosen_datatype = int(input(f'\n\t\tEnter the datatype of {primary_key} primary key: '))

                if datatypes[chosen_datatype - 1] in ['VARCHAR', 'CHAR']:
                    size = input(f'\t\tEnter the size of character from {primary_key} primary key: ')
                
                elif datatypes[chosen_datatype - 1] == 'FLOAT':
                    size = input(f'\t\tEnter the floating-point size of {primary_key} primary key: ')
                    decimal_digits = input(f'\t\tEnter the decimal digits of {primary_key} primary key: ')

                else:
                    pass

                if (datatypes[chosen_datatype - 1] in ['VARCHAR', 'CHAR']) and (int(size) <= 0 or int(size) > 255):
                    invalid_character_size = True
                    break
                
                if (datatypes[chosen_datatype - 1] == 'FLOAT') and (int(size) <= 0 or int(size) > 32):
                    invalid_floating_point_size = True
                    break
                
                if (datatypes[chosen_datatype - 1] == 'FLOAT') and (int(decimal_digits) <= 0 or int(decimal_digits) > 9):
                    invalid_floating_point_decimal_digits = True
                    break                    

                confirm_chosen_datatype = input(f'\t\tDid you enter the correct datatype (Y/N)?: ').strip().upper()

                if confirm_chosen_datatype == 'N':
                    chosen_datatype = True
                    break
                
                if confirm_chosen_datatype != 'Y':
                    invalid_confirmation = True
                    break
                
                if (datatypes[chosen_datatype - 1] in ['VARCHAR', 'CHAR']):
                    primary_keys_and_datatype[primary_key] = f'{datatypes[chosen_datatype - 1]}({size})'
                
                elif (datatypes[chosen_datatype - 1] == 'FLOAT'):
                    primary_keys_and_datatype[primary_key] = f'{datatypes[chosen_datatype - 1]}({size}, {decimal_digits})'
                
                else:
                    primary_keys_and_datatype[primary_key] = datatypes[chosen_datatype - 1]

                print()

            if primary_key_not_confirm:
                os.system('cls')
                continue

            if invalid_confirmation:
                display_invalid_choice_message()
                continue

            if invalid_character_size:
                os.system('cls')
                print(f'\t\tInvalid character size! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue
                
            if invalid_floating_point_size:
                os.system('cls')
                print(f'\t\tInvalid floating-point size! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue
            
            if invalid_floating_point_decimal_digits:
                os.system('cls')
                print(f'\t\tInvalid floating-point decimal digits! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue
            
            if chosen_datatype_not_confirm:
                os.system('cls')
                continue
            
            os.system('cls')
            return primary_keys_and_datatype

        except ValueError:
            display_invalid_choice_message()
            continue

def create_non_key_columns(table_metadata: dict[str, str | int | dict[str, str]]) -> dict[str, str]:
    '''
        Create function to
        create non-key columns
        for new table
    '''
    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 30)
        header = 'Creating Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 30)
        print()

        print(f'\t\tTable Name: {table_metadata['Table Name']}')
        print(f'\t\tNumber of Columns: {table_metadata['Number of Columns']}')

        if table_metadata['Primary Keys'] == {}:
            print(f'\t\tPrimary Key: None')

        else:
            print('\n\t\tPrimary Keys:\n')

            for primary_key, datatype in table_metadata['Primary Keys'].items():
                print(f'\t\t\tPrimary Key: {primary_key}')
                print(f'\t\t\tData Type: {datatype}')
                print()

        try:
            number_of_non_key_columns = int(input(f'\t\tHow many number of non-key columns you want to create?: '))

            if number_of_non_key_columns < 0:
                display_invalid_choice_message()
                continue
                
            if number_of_non_key_columns > table_metadata['Number of Columns']:
                display_invalid_choice_message()
                continue

            if (number_of_non_key_columns + len(table_metadata['Primary Keys'].keys())) > table_metadata['Number of Columns']:
                display_invalid_choice_message()
                continue
            
            if (number_of_non_key_columns + len(table_metadata['Primary Keys'].keys())) < table_metadata['Number of Columns']:
                display_invalid_choice_message()
                continue

            if (len(table_metadata['Primary Keys'].keys()) == table_metadata['Number of Columns']) and (number_of_non_key_columns == 0):
                return {}

            # Display header
            os.system('cls')
            print(f'\t\t', end='')
            print('=' * 30)
            header = 'Creating Table'
            print(f'\t\t\t{header}')
            print(f'\t\t', end='')
            print('=' * 30)
            print()

            datatypes = [
                'INTEGER',
                'VARCHAR',
                'CHAR',
                'FLOAT',
                'DATE',
                'TIME',
                'DATETIME',
                'BOOLEAN',
                'TEXT'
            ]
            non_key_column_and_datatypes = {}
            
            non_key_column_not_confirm = False
            invalid_confirmation = False
            invalid_chosen_datatype = False
            invalid_character_size = False
            invalid_floating_point_size = False
            invalid_floating_point_decimal_digits = False
            chosen_datatype_not_confirm = False

            for _ in range(number_of_non_key_columns):
                non_key_column = input(f'\t\tEnter your non-key column here: ')
                confirm_non_key_columns = input(f'\t\tDid you enter the correct non-key column (Y/N)?: ').strip().upper()

                if confirm_non_key_columns == 'N':
                    non_key_column_not_confirm = True
                    break
                
                if confirm_non_key_columns != 'Y':
                    invalid_confirmation = True
                    break

                print()

                for number, datatype in enumerate(datatypes):
                    number += 1
                    print(f'\t\t\t{number}.) {datatype}')
                
                chosen_datatype = int(input(f'\n\t\tEnter the datatype of {non_key_column} non-key column: '))

                if chosen_datatype <= 0:
                    invalid_chosen_datatype = True
                    break

                if chosen_datatype > len(datatypes):
                    invalid_chosen_datatype = True
                    break

                if datatypes[chosen_datatype - 1] in ['VARCHAR', 'CHAR']:
                    size = input(f'\t\tEnter the character size of {non_key_column} non-key column: ')
                
                elif datatypes[chosen_datatype - 1] == 'FLOAT':
                    size = input(f'\t\tEnter the floating-point size of {non_key_column} non-key column: ')
                    decimal_digits = input(f'\t\tEnter the floating-point decimal digit of {non_key_column} non-key column: ')
                
                else:
                    pass

                if (datatypes[chosen_datatype - 1] in ['VARCHAR', 'CHAR']) and (int(size) <= 0 or int(size) > 255):
                    invalid_character_size = True
                    break
                
                if (datatypes[chosen_datatype - 1] == 'FLOAT') and (int(size) <= 0 or int(size) > 32):
                    invalid_floating_point_size = True
                    break
                
                if (datatypes[chosen_datatype - 1] == 'FLOAT') and (int(decimal_digits) <= 0 or int(decimal_digits) > 9):
                    invalid_floating_point_decimal_digits = True
                    break

                confirm_chosen_datatype = input(f'\t\tDid you enter the correct datatype (Y/N)?: ').strip().upper()

                if confirm_chosen_datatype == 'N':
                    chosen_datatype_not_confirm = True
                    break
                
                if confirm_chosen_datatype != 'Y':
                    invalid_confirmation = True
                    break

                if datatypes[chosen_datatype - 1] in ['VARCHAR', 'CHAR']:
                    non_key_column_and_datatypes[non_key_column] = f'{datatypes[chosen_datatype - 1]}({size})'
                
                elif datatypes[chosen_datatype - 1] == 'FLOAT':
                    non_key_column_and_datatypes[non_key_column] = f'{datatypes[chosen_datatype - 1]}({size, {decimal_digits}})'
                
                else:
                    non_key_column_and_datatypes[non_key_column] = datatypes[chosen_datatype - 1]

                print()

            if non_key_column_not_confirm:
                os.system('cls')
                continue
            
            if invalid_confirmation:
                display_invalid_choice_message()
                continue

            if invalid_chosen_datatype:
                display_invalid_choice_message()
                continue
                
            if invalid_character_size:
                os.system('cls')
                print(f'\t\tInvalid character size! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue
            
            if invalid_floating_point_size:
                os.system('cls')
                print(f'\t\tInvalid floating-point size! Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue
            
            if invalid_floating_point_decimal_digits:
                os.system('cls')
                print(f'\t\tInvalid floating-point decimal digits!b Please try again.')
                input(f'\t\tPress any key to reload page: ')
                os.system('cls')
                continue
            
            if chosen_datatype_not_confirm:
                os.system('cls')
                continue
            
            os.system('cls')
            return non_key_column_and_datatypes

        except ValueError:
            display_invalid_choice_message()
            continue

def init_sql_command_for_table_creation(table_metadata: dict[str, str | int | dict[str, str]]) -> str:
    '''
        Initialize function to initialize
        SQL Command for creating the new table
    '''
    command = f'CREATE TABLE {table_metadata['Table Name']}'
    columns = []

    for primary_key, datatype in table_metadata['Primary Keys'].items():
        columns.append(f'{primary_key} {datatype}')

    for non_key_column, datatype in table_metadata['Non-Key Columns'].items():
        columns.append(f'{non_key_column} {datatype}')

    columns = ', '.join(columns)
    command = command + '(' + columns
    
    if table_metadata['Primary Keys'] != {}:
        primary_keys = list(table_metadata['Primary Keys'].keys())
        primary_keys = ', '.join(primary_keys)
        command = command + ', ' + 'PRIMARY KEY' + '(' + primary_keys + ')' + ')' + ';'

    else:
        command = command + ')' + ';'
    
    return command

def create_table_page() -> None:
    '''
        Create Table Page function
        to create a new table from the
        exiting database
    '''
    while True:
        # Display header
        print(f'\t\t', end='')
        print('=' * 28)
        header = 'Create Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 28)
        print()

        confirm = input(f'\t\tDo you want to create a new table (Y/N)?: ').strip().upper()

        if confirm == 'N':
            os.system('cls')
            break

        if confirm != 'Y':
            display_invalid_choice_message()
            continue

        table_metadata = {
            'Table Name': '',
            'Number of Columns': 0,
            'Primary Keys': {},
            'Non-Key Columns': {}
        }

        os.system('cls')
        table_metadata['Table Name'] = create_table_name()
        table_metadata['Number of Columns'] = get_the_total_number_of_columns(table_metadata)
        table_metadata['Primary Keys'] = create_primary_keys(table_metadata)
        table_metadata['Non-Key Columns'] = create_non_key_columns(table_metadata)

        # Display header
        os.system('cls')
        print(f'\t\t', end='')
        print('=' * 38)
        header = 'Validate Created Table'
        print(f'\t\t\t{header}')
        print(f'\t\t', end='')
        print('=' * 38)
        print()

        # Display created table and columns
        print(f'\t\tTable Name: {table_metadata['Table Name']}')

        if table_metadata['Primary Keys'] == {}:
            print(f'\t\tPrimary Keys: None')

        else:
            print(f'\n\t\tPrimary Keys:\n')

            for primary_key, datatype in table_metadata['Primary Keys'].items():
                print(f'\t\t\tPrimary Key: {primary_key}')
                print(f'\t\t\tDatatype: {datatype}')
                print()

        if table_metadata['Non-Key Columns'] == {}:
            print(f'\t\tNon-Key Columns: None')

        else:
            if table_metadata['Primary Keys'] == {}:
                print(f'\n\t\tNon-Key Columns:\n')

            else:
                print(f'\t\tNon-Key Columns:\n')

            for non_key_column, datatype in table_metadata['Non-Key Columns'].items():
                print(f'\t\t\tNon-Key Colunn: {non_key_column}')
                print(f'\t\t\tDatatype: {datatype}')
                print()
        
        if table_metadata['Non-Key Columns'] == {}:
            confirm_created_table = input(f'\n\t\tDid you enter the correct details for the {table_metadata['Table Name']} table (Y/N)?: ').strip().upper()
        
        else:
            confirm_created_table = input(f'\t\tDid you enter the correct details for the {table_metadata['Table Name']} table (Y/N)?: ').strip().upper()
        
        if confirm_created_table == 'N':
            os.system('cls')
            continue

        if confirm_created_table != 'Y':
            display_invalid_choice_message()
            continue
        
        try:
            conn = init_connection() # Initialize a connection to the PostgreSQL Database using Pyscopg2
            cursor = conn.cursor() # Initialize a cursor from the established connection
            command = init_sql_command_for_table_creation(table_metadata)
            
            cursor.execute(command)
            conn.commit()

            cursor.close()
            conn.close()

            engine = init_engine() # Initialize SQL Alchemy Engine for PostgreSQL Database
            dataframe = pd.read_sql(f'SELECT * FROM {table_metadata['Table Name']}', engine)
            dataframe.to_csv(f'src/data/{table_metadata['Table Name']}.csv', index=False)

            os.system('cls')
            print(f'\t\tSuccessfully created {table_metadata['Table Name']} table!')
            input(f'\t\tPress any key to exit page: ')
            os.system('cls')
            break

        except Exception as error_message:
            os.system('cls')
            print(f'\t\tError creating table {table_metadata['Table Name']}!')
            print(f'\t\tError message: {error_message}')
            input(f'\t\tPress any key to reload page: ')
            os.system('cls')
            continue