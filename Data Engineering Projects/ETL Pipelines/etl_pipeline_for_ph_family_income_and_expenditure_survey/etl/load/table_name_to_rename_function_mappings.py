'''
    Table name to rename functions from rename module
    mappings
'''
import pandas as pd
from load.rename import rename_table_1_processed_dataset_columns, rename_table_1a_processed_dataset_columns
from load.rename import rename_table_2_processed_dataset_columns, rename_table_2a_processed_dataset_columns
from load.rename import rename_table_3_processed_dataset_columns, rename_table_3a_processed_dataset_columns
from load.rename import rename_table_4_processed_dataset_columns, rename_table_4a_dataset_columns
from load.rename import rename_table_5_dataset_columns
from load.rename import rename_table_6_dataset_columns
from load.rename import rename_table_7_dataset_columns

def map_table_name_to_rename_functions() -> dict[str, pd.DataFrame]:
    '''
        Map function to map base table name
        to rename functions from rename module
    '''
    rename_functions = {
        'table1': rename_table_1_processed_dataset_columns(pd.read_csv('data/processed/table_1_2018_2021_and_2023p_average_annual_family_income_by_per_capita_income_decile_class_and_by_region_province_and_hucs.csv')),
        'table1a': rename_table_1a_processed_dataset_columns(pd.read_csv('data/processed/table_1a_cv_2018_2021_and_2023p_average_annual_family_income_by_per_capita_income_decile_class_and_by_region_province_and_hucs.csv')),
        'table2': rename_table_2_processed_dataset_columns(pd.read_csv('data/processed/table_2_2018_2021_and_2023p_average_annual_family_expenditure_by_per_capita_income_decile_class_and_by_region_province_and_huc.csv'))        ,
        'table2a': rename_table_2a_processed_dataset_columns(pd.read_csv('data/processed/table_2a_cv_2018_2021_and_2023p_average_annual_family_expenditure_by_per_capita_income_decile_class_and_by_region_province_and_huc.csv')),
        'table3': rename_table_3_processed_dataset_columns(pd.read_csv('data/processed/table_3_2018_2021_and_2023p_total_annual_family_income_by_per_capita_income_decile_and_by_region_province_and_huc.csv')),
        'table3a': rename_table_3a_processed_dataset_columns(pd.read_csv('data/processed/table_3a_cv_2018_2021_and_2023p_total_annual_family_income_by_per_capita_income_decile_and_by_region_province_and_huc.csv')),
        'table4': rename_table_4_processed_dataset_columns(pd.read_csv('data/processed/table_4_2018_2021_and_2023p_total_annual_family_expenditure_by_per_capita_income_decile_and_by_region_province_and_huc.csv')),
        'table4a': rename_table_4a_dataset_columns(pd.read_csv('data/processed/table_4a_cv_2018_2021_and_2023p_total_annual_family_expenditure_by_per_capita_income_decile_and_by_region_province_and_huc.csv')),
        'table5': rename_table_5_dataset_columns(pd.read_csv('data/processed/table_5_2018_2021_and_2023p_gini_coefficient_and_palma_ratio_by_region_province_and_huc.csv')),
        'table6': rename_table_6_dataset_columns(pd.read_csv('data/processed/table_6_2018_2021_and_2023p_share_to_total_annual_family_income_by_region_province_and_huc.csv')),
        'table7': rename_table_7_dataset_columns(pd.read_csv('data/processed/table_7_2018_2021_and_2023p_share_to_total_family_expenditure_by_region_province_and_huc.csv'))
    }
    
    return rename_functions