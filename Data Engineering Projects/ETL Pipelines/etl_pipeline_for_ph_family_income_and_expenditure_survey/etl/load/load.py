'''
    Load Module
'''
import pandas as pd
from glob import glob
from sqlalchemy import create_engine
from load.table_name_to_rename_function_mappings import map_table_name_to_rename_functions

def load_processed_datasets_to_postgresql_db(processed_datasets_dir_path: str) -> None:
    '''
        Load function to load
        processed datasets to 
        PostgreSQL Database Server 
        using SQLAlchemy Engine
    '''
    username = '<YOUR_USERNAME_CREDENTIALS_FOR_POSTGRESQL_DB_SERVER>'
    password = '<YOUR_PASSWORD_CREDENTIALS_FOR_POSTGRESQL_DB_SERVER>'
    hostname = '<YOUR_OWN_SPECIFIC_HOSTNAME>'
    port = '5432'
    database = 'ph_family_income_and_expenditure_surveys'    
    engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')

    base_table_name_to_sql_table_name_mappings = {
        'table1': 'avg_annual_fam_income_per_capita',
        'table1a': 'coefficient_variation_of_avg_annual_fam_income',
        'table2': 'avg_annual_fam_expenditure_per_capita',
        'table2a': 'coefficient_variation_of_avg_annual_fam_expend',
        'table3': 'total_annual_fam_income_per_capita',
        'table3a': 'coefficient_variation_of_total_annual_fam_income',
        'table4': 'total_annual_fam_expend_per_capita',
        'table4a': 'coefficient_variation_of_total_annual_fam_expend',
        'table5': 'gini_coefficient_and_palma_ratio',
        'table6': 'share_to_total_annual_fam_income',
        'table7': 'share_to_total_fam_expend'
    }
    
    for csv_file in glob(f'{processed_datasets_dir_path}/*.csv'):
        filepath = str(csv_file).split('data/processed\\')
        filepath = filepath[1]
        table_name = filepath[:8].replace('_', '')
        
        validated_base_table_names = list(base_table_name_to_sql_table_name_mappings.keys())
        
        if table_name in validated_base_table_names:
            rename_functions = map_table_name_to_rename_functions()
            processed_dataframe = rename_functions[table_name]
            processed_dataframe.to_sql(base_table_name_to_sql_table_name_mappings[table_name], engine, if_exists='replace', index=False)

    print(f'Successfully loaded datasets to PostgreSQL Database Server')