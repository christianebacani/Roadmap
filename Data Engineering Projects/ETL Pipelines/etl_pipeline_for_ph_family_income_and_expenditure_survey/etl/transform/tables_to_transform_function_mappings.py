'''
    Tables to Transform Function Mappings Module
'''
import pandas as pd
from transform.transform import transform_table_1_dataset, transform_table_1a_dataset
from transform.transform import transform_table_2_dataset, transform_table_2a_dataset
from transform.transform import transform_table_3_dataset, transform_table_3a_dataset
from transform.transform import transform_table_4_dataset, transform_table_4a_dataset
from transform.transform import transform_table_5_dataset
from transform.transform import transform_table_6_dataset
from transform.transform import transform_table_7_dataset

def map_tables_to_transformation_functions() -> dict[str, pd.DataFrame]:
    '''
        Map function to map
        corresponding table name
        to equivalent transformation function
        from transform module
    '''
    transform_dataset_functions = {
        'table1': transform_table_1_dataset(pd.read_csv('data/stage/table_1_2018_2021_and_2023p_average_annual_family_income_by_per_capita_income_decile_class_and_by_region_province_and_hucs.csv')),
        'table1a': transform_table_1a_dataset(pd.read_csv('data/stage/table_1a_cv_2018_2021_and_2023p_average_annual_family_income_by_per_capita_income_decile_class_and_by_region_province_and_hucs.csv')),
        'table2': transform_table_2_dataset(pd.read_csv('data/stage/table_2_2018_2021_and_2023p_average_annual_family_expenditure_by_per_capita_income_decile_class_and_by_region_province_and_huc.csv')),
        'table2a': transform_table_2a_dataset(pd.read_csv('data/stage/table_2a_cv_2018_2021_and_2023p_average_annual_family_expenditure_by_per_capita_income_decile_class_and_by_region_province_and_huc.csv')),
        'table3': transform_table_3_dataset(pd.read_csv('data/stage/table_3_2018_2021_and_2023p_total_annual_family_income_by_per_capita_income_decile_and_by_region_province_and_huc.csv')),
        'table3a': transform_table_3a_dataset(pd.read_csv('data/stage/table_3a_cv_2018_2021_and_2023p_total_annual_family_income_by_per_capita_income_decile_and_by_region_province_and_huc.csv')),
        'table4': transform_table_4_dataset(pd.read_csv('data/stage/table_4_2018_2021_and_2023p_total_annual_family_expenditure_by_per_capita_income_decile_and_by_region_province_and_huc.csv')),
        'table4a': transform_table_4a_dataset(pd.read_csv('data/stage/table_4a_cv_2018_2021_and_2023p_total_annual_family_expenditure_by_per_capita_income_decile_and_by_region_province_and_huc.csv')),
        'table5': transform_table_5_dataset(pd.read_csv('data/stage/table_5_2018_2021_and_2023p_gini_coefficient_and_palma_ratio_by_region_province_and_huc.csv')),
        'table6': transform_table_6_dataset(pd.read_csv('data/stage/table_6_2018_2021_and_2023p_share_to_total_annual_family_income_by_region_province_and_huc.csv')),
        'table7': transform_table_7_dataset(pd.read_csv('data/stage/table_7_2018_2021_and_2023p_share_to_total_family_expenditure_by_region_province_and_huc.csv'))
    }
    return transform_dataset_functions    
    
    