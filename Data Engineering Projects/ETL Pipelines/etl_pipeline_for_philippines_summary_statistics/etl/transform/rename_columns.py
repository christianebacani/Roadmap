'''
    Renaming columns from staged datasets
'''
import pandas as pd

def rename_dataset_columns(stage_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename columns from the staged datasets
    '''
    # Getting the old names as a list
    columns = list(stage_dataframe.keys())
    new_column_names = []
    
    # For loop to iterate over the sequence of rows of value per column in dataframe
    for column in columns:
        for index, value in enumerate(stage_dataframe[column]):
            value = str(value).strip()

            # Index 0 contains the column name
            if index == 0:  
                new_column_names.append(value)
                break

    renamed_columns = {}
    
    # Mapped to the dictionary by checking their index position getting the old name as a key and new column name as a value
    for old_column_index, old_column_name in enumerate(columns):
        for new_column_index, new_column_name in enumerate(new_column_names):
            if old_column_index == new_column_index:
                new_column_name_lst = str(new_column_name).split()
                new_column_name_lst = [word.lower().strip() for word in new_column_name_lst]
                new_column_name = '_'.join(new_column_name_lst)
                
                renamed_columns[old_column_name] = new_column_name

    # For-loop to check every key value pairs to check if the prefix of value contains year
    for old_column_name, new_column_name in renamed_columns.items():
        # Remove prefix year and append it at the end of the value
        if str(new_column_name).startswith('2015'):
            new_column_name = f'{new_column_name[5:]}_2015'
            renamed_columns[old_column_name] = new_column_name
        
        elif str(new_column_name).startswith('2016'):
            new_column_name = f'{new_column_name[5:]}_2016'
            renamed_columns[old_column_name] = new_column_name
        
        elif str(new_column_name).startswith('2019'):
            new_column_name = f'{new_column_name[5:]}_2019'
            renamed_columns[old_column_name] = new_column_name.replace('a/', 'at').replace('/', '_')
        
        elif str(new_column_name).startswith('2020'):
            new_column_name = f'{new_column_name[5:]}_2020'
            renamed_columns[old_column_name] = new_column_name.replace('a/', 'at').replace('/', '_')
        
        elif str(new_column_name).startswith('2021'):
            new_column_name = f'{new_column_name[5:]}_2021'
            renamed_columns[old_column_name] = new_column_name.replace('a/', 'at').replace('/', '_')

    # Rename column names
    stage_dataframe.rename(columns=renamed_columns, inplace=True)

    return stage_dataframe

    

    
    