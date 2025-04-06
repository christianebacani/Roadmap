'''
    Load the processed datasets to the local postgresql database
'''
from glob import glob
import pandas as pd
from database_connection.database_connection import connect
from load.rename_tables import rename_tables

def load(processed_dir: str) -> None:
    '''
        Load function to load the processed datasets to the local postgresql database
    '''
    # Separating the function for providing connection to the local postgresql server for security reasons
    engine = connect()

    # Using glob function to extract datasets from the sub-directory path
    for processed_datasets_subdir in glob(f'{processed_dir}/*'):
        subdir_name = processed_datasets_subdir.replace(f'{processed_dir}\\', '')
        
        for dataset in glob(f'{processed_datasets_subdir}/*.csv'):
            # Getting the base filename by splitting filepath name
            dataset_lst = str(dataset).split(f'\\{subdir_name}\\')
            base_filename = dataset_lst[1].replace('.csv', '')
            processed_dataframe = pd.read_csv(dataset)
            
            # Execute a function to get the table name by using base filename as a parameter
            table_name = str(base_filename).replace('summary_statistics_for_', '')
            table_name = rename_tables(table_name)
            year = subdir_name[:4]
            table_name = f'{table_name}_{year}' # Appending year because every year contains the same dataset name
            
            processed_dataframe.to_sql(table_name, engine, if_exists='replace', index=False) # Mapped to the corresponding table to the postgresql server
            print(f'Successfully loaded {table_name} table to psa_summary_stats database')


