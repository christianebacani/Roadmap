'''
    Rename Module
'''
import re
import pandas as pd

def rename_table_1_processed_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 1 dataset columns
        from processed directory 
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())
        
    for i in range(len(columns)):
        if re.search(r'^(all_income_groups_)\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'avg_annual_fam_income_per_capita_of_all_income_groups_{year}'

        elif re.search(r'^.*(decile_)\d{4}$', columns[i]):
            decile_class = '_'.join(str(columns[i]).split('_')[:2])
            year = columns[i][-4:]
            new_column = f'avg_annual_fam_income_per_capita_of_{decile_class}_class_{year}'

        elif re.search(r'^(all_income_groups_pct_change_).*$', columns[i]):
            year_range = str(columns[i]).split('_')[-3] + '-' + str(columns[i]).split('_')[-1]
            new_column = f'pct_change_of_avg_annual_fam_income_of_all_income_groups_in_{year_range}'

        elif re.search(r'^.*(decile_pct_change).*$', columns[i]):
            decile_class = '_'.join(str(columns[i]).split('_')[:2])
            year_range = str(columns[i]).split('_')[-3] + '-' + str(columns[i]).split('_')[-1]
            new_column = f'pct_change_of_avg_annual_fam_income_of_{decile_class}_in_{year_range}'

        else:
            continue

        new_columns[columns[i]] = new_column
    
    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe

def rename_table_1a_processed_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 1a dataset columns
        from processed directory
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())

    for i in range(len(columns)):
        if re.search(r'^(all_income_groups_)\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'coefficient_of_var_of_all_income_groups_{year}'

        elif re.search(r'^.*(_decile_)\d{4}$', columns[i]):
            decile_class = str(columns[i]).split('_')[0] + '_' + str(columns[i]).split('_')[1]
            year = columns[i][-4:]
            new_column = f'coefficient_of_var_of_{decile_class}_class_{year}'
        
        else:
            continue
        
        new_columns[columns[i]] = new_column
    
    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe

def rename_table_2_processed_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 2 dataset columns
        from processed directory
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())

    for i in range(len(columns)):
        if re.search(r'^(all_income_groups_)\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'avg_annual_fam_expenditure_of_all_income_groups_{year}'

        elif re.search(r'^.*(_decile_)\d{4}$', columns[i]):
            decile_class = str(columns[i]).split('_')[0] + '_' + str(columns[i]).split('_')[1]
            year = columns[i][-4:]
            new_column = f'avg_annual_fam_expenditure_of_{decile_class}_class_{year}'

        elif re.search(r'^(all_income_groups_pct_change_).*$', columns[i]):
            year_range = str(columns[i]).split('_')[-3] + '-' + str(columns[i]).split('_')[-1]
            new_column = f'pct_change_of_annual_fam_expend_of_all_income_groups_{year_range}'
            
        elif re.search(r'^.*(_decile_pct_change_).*$', columns[i]):
            decile_class = str(columns[i]).split('_')[0] + '_' + str(columns[i]).split('_')[1]
            year_range = str(columns[i]).split('_')[-3] + '-' + str(columns[i]).split('_')[-1]
            new_column = f'pct_change_of_annual_fam_expend_of_{decile_class}_{year_range}'

        else:
            continue

        new_columns[columns[i]] = new_column
    
    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe

def rename_table_2a_processed_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 2a dataset columns
        from processed directory
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())

    for i in range(len(columns)):
        if re.search(r'^(all_income_groups_)\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'coe_var_of_avg_annual_fam_expend_for_all_income_groups_{year}'

        elif re.search(r'^.*(_decile_)\d{4}$', columns[i]):
            decile_class = str(columns[i]).split('_')[0] + '_' + str(columns[i]).split('_')[1]
            year = columns[i][-4:]
            new_column = f'coe_var_of_avg_annual_fam_expend_for_{decile_class}_class_{year}'

        else:
            continue

        new_columns[columns[i]] = new_column
    
    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe

def rename_table_3_processed_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 3 dataset columns
        from processed directory
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())

    for i in range(len(columns)):
        if re.search(r'^(all_income_groups)_\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'total_annual_fam_income_for_all_income_groups_{year}'
        
        elif re.search(r'^.*(_decile_)\d{4}$', columns[i]):
            decile_class = str(columns[i]).split('_')[0] + '_' + str(columns[i]).split('_')[1]
            year = columns[i][-4:]
            new_column = f'total_annual_fam_income_for_{decile_class}_class_{year}'
        
        elif re.search(r'^(all_income_groups_pct_change_).*$', columns[i]):
            year_range = str(columns[i]).split('_')[-3] + '-' + str(columns[i]).split('_')[-1]
            new_column = f'pctchange_of_total_annual_fam_income_all_income_grps_{year_range}'

        elif re.search(r'^.*(_decile_pct_change_).*$', columns[i]):
            decile_class = str(columns[i]).split('_')[0] + '_' + str(columns[i]).split('_')[1][:3]
            year_range = str(columns[i]).split('_')[-3] + '-' + str(columns[i]).split('_')[-1]
            new_column = f'pctchange_of_total_annual_fam_income_{decile_class}_{year_range}'

        else:
            continue

        new_columns[columns[i]] = new_column
    
    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe

def rename_table_3a_processed_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 3a dataset columns
        from processed directory
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())

    for i in range(len(columns)):
        if re.search(r'^(all_income_groups_).*$', columns[i]):
            year = columns[i][-4:]
            new_column = f'coe_var_of_total_annual_fam_income_for_all_income_grps_{year}'

        elif re.search(r'^.*(_decile_)\d{4}$', columns[i]):
            decile_class = str(columns[i]).split('_')[0] + '_' + str(columns[i]).split('_')[1][:3]
            year = columns[i][-4:]
            new_column = f'coe_var_of_total_annual_fam_income_for_{decile_class}_class_{year}'
        
        else:
            continue

        new_columns[columns[i]] = new_column
    
    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe

def rename_table_4_processed_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 4 dataset columns
        from processed directory
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())

    for i in range(len(columns)):
        if re.search(r'^(all_income_groups_)\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'total_annual_fam_income_for_all_income_grps_{year}'
        
        elif re.search(r'^.*(_decile_).\d{4}$', columns[i]):
            decile_class = str(columns[i]).split('_')[0] + '_' + str(columns[i]).split('_')[1]
            year = columns[i][-4:]
            new_column = f'total_annual_fam_income_for_{decile_class}_class_{year}'
        
        elif re.search(r'^(all_income_groups_pct_change_).*$', columns[i]):
            year_range = str(columns[i]).split('_')[-3] + '-' + str(columns[i]).split('_')[-1]
            new_column = f'pctchange_of_total_annual_fam_income_all_income_grps_{year_range}'
        
        elif re.search(r'^.*(_decile_pct_change_).*$', columns[i]):
            decile_class = str(columns[i]).split('_')[0] + '_' + str(columns[i]).split('_')[1][:3]
            year_range = str(columns[i]).split('_')[-3] + '-' + str(columns[i]).split('_')[-1]
            new_column = f'pctchange_of_total_annual_fam_income_{decile_class}_class_{year_range}'
        
        else:
            continue

        new_columns[columns[i]] = new_column
    
    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe

def rename_table_4a_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 4a dataset columns
        from processed directory 
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())

    for i in range(len(columns)):
        if re.search(r'^(all_income_groups_)\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'coe_var_total_annual_fam_expend_all_income_grps_{year}'
        
        elif re.search(r'^.*(_decile_)\d{4}$', columns[i]):
            decile_class = str(columns[i]).split('_')[0] + '_' + str(columns[i]).split('_')[1][:3]
            year = columns[i][-4:]
            new_column = f'coe_var_total_annual_fam_expend_{decile_class}_class_{year}'
    
        else:
            continue

        new_columns[columns[i]] = new_column
    
    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe

def rename_table_5_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 5 dataset columns
        from processed directory 
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())

    for i in range(len(columns)):
        if re.search(r'^(gini_coefficient_)\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'gini_coefficient_at_{year}'
        
        elif re.search(r'^(palma_ratio_)\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'palma_ratio_at_{year}'
        
        else:
            continue

        new_columns[columns[i]] = new_column

    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe

def rename_table_6_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 6 dataset columns
        from processed directory 
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())

    for i in range(len(columns)):
        if columns[i] == 'region_province_huc_by_sources_of_income':
            new_column = f'sources_of_income_per_region_province_huc'
    
        elif re.search(r'^(in_percent_)\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'share_to_total_annual_fam_income_in_pct_{year}'

        else:
            year_range = str(columns[i]).split('_')[-3] + '-' + str(columns[i]).split('_')[-1]
            new_column = f'share_to_total_annual_fam_income_pct_pt_change_{year_range}'

        new_columns[columns[i]] = new_column
    
    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe

def rename_table_7_dataset_columns(processed_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        table 7 dataset columns
        from processed directory 
    '''
    new_columns = {}
    columns = list(processed_dataframe.keys())

    for i in range(len(columns)):
        if columns[i] == 'region_province_huc_by_expenditure_group':
            new_column = 'share_to_total_fam_expend_per_region_province_huc'
        
        elif re.search(r'^(in_percent_)\d{4}$', columns[i]):
            year = columns[i][-4:]
            new_column = f'share_to_total_fam_expend_in_pct_{year}'
        
        else:
            year_range = str(columns[i]).split('_')[-3] + '-' + str(columns[i]).split('_')[-1]
            new_column = f'share_to_total_fam_expend_pct_pt_change_{year_range}'
        
        new_columns[columns[i]] = new_column
    
    processed_dataframe.rename(columns=new_columns, inplace=True)
    return processed_dataframe