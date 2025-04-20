'''
    Transform Module
'''
import pandas as pd

def transform_table_1_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 1 dataset
    '''
    data = {
        'index': [], 
        'region_province_huc': [], 
        'all_income_groups_2018': [], 
        'first_decile_2018': [],
        'second_decile_2018': [],
        'third_decile_2018': [],
        'fourth_decile_2018': [],
        'fifth_decile_2018': [],
        'sixth_decile_2018': [],
        'seventh_decile_2018': [],
        'eighth_decile_2018': [],
        'ninth_decile_2018': [],
        'tenth_decile_2018': [],
        'all_income_groups_2021': [],
        'first_decile_2021': [],
        'second_decile_2021': [],
        'third_decile_2021': [],
        'fourth_decile_2021': [],
        'fifth_decile_2021': [],
        'sixth_decile_2021': [],
        'seventh_decile_2021': [],
        'eighth_decile_2021': [],
        'ninth_decile_2021': [],
        'tenth_decile_2021': [],
        'all_income_groups_2023': [],
        'first_decile_2023': [],
        'second_decile_2023': [],
        'third_decile_2023': [],
        'fourth_decile_2023': [],
        'fifth_decile_2023': [],
        'sixth_decile_2023': [],
        'seventh_decile_2023': [],
        'eighth_decile_2023': [],
        'ninth_decile_2023': [],
        'tenth_decile_2023': [],
        'all_income_groups_pct_change_2018_to_2021': [],
        'first_decile_pct_change_2018_to_2021': [],
        'second_decile_pct_change_2018_to_2021': [],
        'third_decile_pct_change_2018_to_2021': [],
        'fourth_decile_pct_change_2018_to_2021': [],
        'fifth_decile_pct_change_2018_to_2021': [],
        'sixth_decile_pct_change_2018_to_2021': [],
        'seventh_decile_pct_change_2018_to_2021': [],
        'eighth_decile_pct_change_2018_to_2021': [],
        'ninth_decile_pct_change_2018_to_2021': [],
        'tenth_decile_pct_change_2018_to_2021': [],
        'all_income_groups_pct_change_2021_to_2023': [],
        'first_decile_pct_change_2021_to_2023': [],
        'second_decile_pct_change_2021_to_2023': [],
        'third_decile_pct_change_2021_to_2023': [],
        'fourth_decile_pct_change_2021_to_2023': [],
        'fifth_decile_pct_change_2021_to_2023': [],
        'sixth_decile_pct_change_2021_to_2023': [],
        'seventh_decile_pct_change_2021_to_2023': [],
        'eighth_decile_pct_change_2021_to_2023': [],
        'ninth_decile_pct_change_2021_to_2023': [],
        'tenth_decile_pct_change_2021_to_2023': []
    }

    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())

    for index, row in staged_dataframe.iterrows():
        if (index < 4) or (index > 163):
            continue

        for i in range(len(columns)):
            value = row.get(columns[i])

            data[new_columns[i]].append(value)

    df = pd.DataFrame(data)
    transformed_data = {}
    
    for new_column in new_columns:
        transformed_data[new_column] = []
    
    for _, row in df.iterrows():        
        region_province_huc = str(row.get('region_province_huc')).lower()

        if region_province_huc == 'nan':
            continue

        for new_column in new_columns:
            value = str(row.get(new_column))

            if new_column == 'index':
                value = int(value)
            
            elif new_column == 'region_province_huc':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'V', 'VI', 'VII', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]
                value = ' '.join(value).replace('2/', '').replace('/', '')
                
            elif value.lower() == 'nan':
                value = 0.00

            else:
                value = round(float(value), 2)

            transformed_data[new_column].append(value)
    
    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)

    return transformed_dataframe

def transform_table_1a_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 1a dataset    
    '''
    data = {
        'index': [],
        'region_province_huc': [],
        'all_income_groups_2018': [],
        'first_decile_2018': [],
        'second_decile_2018': [],
        'third_decile_2018': [],
        'fourth_decile_2018': [],
        'fifth_decile_2018': [],
        'sixth_decile_2018': [],
        'seventh_decile_2018': [],
        'eighth_decile_2018': [],
        'ninth_decile_2018': [],
        'tenth_decile_2018': [],
        'all_income_groups_2021': [],
        'first_decile_2021': [],
        'second_decile_2021': [],
        'third_decile_2021': [],
        'fourth_decile_2021': [],
        'fifth_decile_2021': [],
        'sixth_decile_2021': [],
        'seventh_decile_2021': [],
        'eighth_decile_2021': [],
        'ninth_decile_2021': [],
        'tenth_decile_2021': [],
        'all_income_groups_2023': [],
        'first_decile_2023': [],
        'second_decile_2023': [],
        'third_decile_2023': [],
        'fourth_decile_2023': [],
        'fifth_decile_2023': [],
        'sixth_decile_2023': [],
        'seventh_decile_2023': [],
        'eighth_decile_2023': [],
        'ninth_decile_2023': [],
        'tenth_decile_2023': [],
    }
    
    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())

    for index, row in staged_dataframe.iterrows():
        if (index < 3) or (index > 162):
            continue

        for i in range(len(columns)):
            value = row.get(columns[i])
            
            data[new_columns[i]].append(value)

    df = pd.DataFrame(data)
    transformed_data = {}
    
    for new_column in new_columns:
        transformed_data[new_column] = []
    
    for _, row in df.iterrows():
        region_province_huc = str(row.get('region_province_huc')).lower()

        if region_province_huc == 'nan':
            continue

        for new_column in new_columns:
            value = str(row.get(new_column))
            
            if new_column == 'index':
                value = int(value)
            
            elif new_column == 'region_province_huc':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'V', 'VI', 'VII', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]
                value = ' '.join(value).replace('2/', '').replace('/', '')               

            elif value.lower() == 'nan':
                value = 0.00
            
            else:
                value = round(float(value), 2)
            
            transformed_data[new_column].append(value)
    
    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)

    return transformed_dataframe

def transform_table_2_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 2 dataset    
    '''
    data = {
        'index': [],
        'region_province_huc': [],
        'all_income_groups_2018': [],
        'first_decile_2018': [],
        'second_decile_2018': [],
        'third_decile_2018': [],
        'fourth_decile_2018': [],
        'fifth_decile_2018': [],
        'sixth_decile_2018': [],
        'seventh_decile_2018': [],
        'eighth_decile_2018': [],
        'ninth_decile_2018': [],
        'tenth_decile_2018': [],
        'all_income_groups_2021': [],
        'first_decile_2021': [],
        'second_decile_2021': [],
        'third_decile_2021': [],
        'fourth_decile_2021': [],
        'fifth_decile_2021': [],
        'sixth_decile_2021': [],
        'seventh_decile_2021': [],
        'eighth_decile_2021': [],
        'ninth_decile_2021': [],
        'tenth_decile_2021': [],
        'all_income_groups_2023': [],
        'first_decile_2023': [],
        'second_decile_2023': [],
        'third_decile_2023': [],
        'fourth_decile_2023': [],
        'fifth_decile_2023': [],
        'sixth_decile_2023': [],
        'seventh_decile_2023': [],
        'eighth_decile_2023': [],
        'ninth_decile_2023': [],
        'tenth_decile_2023': [],
        'all_income_groups_pct_change_2018_to_2021': [],
        'first_decile_pct_change_2018_to_2021': [],
        'second_decile_pct_change_2018_to_2021': [],
        'third_decile_pct_change_2018_to_2021': [],
        'fourth_decile_pct_change_2018_to_2021': [],
        'fifth_decile_pct_change_2018_to_2021': [],
        'sixth_decile_pct_change_2018_to_2021': [],
        'seventh_decile_pct_change_2018_to_2021': [],
        'eighth_decile_pct_change_2018_to_2021': [],
        'ninth_decile_pct_change_2018_to_2021': [],
        'tenth_decile_pct_change_2018_to_2021': [],
        'all_income_groups_pct_change_2021_to_2023': [],
        'first_decile_pct_change_2021_to_2023': [],
        'second_decile_pct_change_2021_to_2023': [],
        'third_decile_pct_change_2021_to_2023': [],
        'fourth_decile_pct_change_2021_to_2023': [],
        'fifth_decile_pct_change_2021_to_2023': [],
        'sixth_decile_pct_change_2021_to_2023': [],
        'seventh_decile_pct_change_2021_to_2023': [],
        'eighth_decile_pct_change_2021_to_2023': [],
        'ninth_decile_pct_change_2021_to_2023': [],
        'tenth_decile_pct_change_2021_to_2023': []
    }
    
    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())
    
    for index, row in staged_dataframe.iterrows():
        if (index < 5) or (index > 164):
            continue

        for i in range(len(columns)):
            value = row.get(columns[i])
            
            data[new_columns[i]].append(value)
    
    df = pd.DataFrame(data)
    transformed_data = {}

    for new_column in new_columns:
        transformed_data[new_column] = []
    
    for _, row in df.iterrows():
        region_province_huc = str(row.get('region_province_huc')).lower()
        
        if region_province_huc == 'nan':
            continue

        for new_column in new_columns:
            value = str(row.get(new_column))

            if new_column == 'index':
                value = int(value)
            
            elif new_column == 'region_province_huc':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]   
                value = ' '.join(value).replace('2/', '').replace('/', '')

            elif value.lower() == 'nan':
                value = 0.00
            
            else:
                value = round(float(value), 2)
            
            transformed_data[new_column].append(value)
    
    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)

    return transformed_dataframe

def transform_table_2a_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 2a dataset
    '''
    data = {
        'index': [],
        'region_province_huc': [],
        'all_income_groups_2018': [],
        'first_decile_2018': [],
        'second_decile_2018': [],
        'third_decile_2018': [],
        'fourth_decile_2018': [],
        'fifth_decile_2018': [],
        'sixth_decile_2018': [],
        'seventh_decile_2018': [],
        'eighth_decile_2018': [],
        'ninth_decile_2018': [],
        'tenth_decile_2018': [],
        'all_income_groups_2021': [],
        'first_decile_2021': [],
        'second_decile_2021': [],
        'third_decile_2021': [],
        'fourth_decile_2021': [],
        'fifth_decile_2021': [],
        'sixth_decile_2021': [],
        'seventh_decile_2021': [],
        'eighth_decile_2021': [],
        'ninth_decile_2021': [],
        'tenth_decile_2021': [],
        'all_income_groups_2023': [],
        'first_decile_2023': [],
        'second_decile_2023': [],
        'third_decile_2023': [],
        'fourth_decile_2023': [],
        'fifth_decile_2023': [],
        'sixth_decile_2023': [],
        'seventh_decile_2023': [],
        'eighth_decile_2023': [],
        'ninth_decile_2023': [],
        'tenth_decile_2023': []
    }
    
    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())
    
    for index, row in staged_dataframe.iterrows():
        if (index < 3) or (index > 162):
            continue

        for i in range(len(columns)):
            value = row.get(columns[i])
            
            data[new_columns[i]].append(value)
    
    df = pd.DataFrame(data)
    transformed_data = {}

    for new_column in new_columns:
        transformed_data[new_column] = []
    
    for _, row in df.iterrows():
        region_province_huc = str(row.get('region_province_huc')).lower()

        if region_province_huc == 'nan':
            continue
    
        for new_column in new_columns:
            value = str(row.get(new_column))

            if new_column == 'index':
                value = int(value)

            elif new_column == 'region_province_huc':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]
                value = ' '.join(value).replace('2/', '').replace('/', '')
            
            elif value.lower() == 'nan':
                value = 0.00
            
            else:
                value = round(float(value), 2)
            
            transformed_data[new_column].append(value)
    
    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)

    return transformed_dataframe

def transform_table_3_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 3 dataset
    '''
    data = {
        'index': [],
        'region_province_huc': [],
        'all_income_groups_2018': [],
        'first_decile_2018': [],
        'second_decile_2018': [],
        'third_decile_2018': [],
        'fourth_decile_2018': [],
        'fifth_decile_2018': [],
        'sixth_decile_2018': [],
        'seventh_decile_2018': [],
        'eighth_decile_2018': [],
        'ninth_decile_2018': [],
        'tenth_decile_2018': [],
        'all_income_groups_2021': [],
        'first_decile_2021': [],
        'second_decile_2021': [],
        'third_decile_2021': [],
        'fourth_decile_2021': [],
        'fifth_decile_2021': [],
        'sixth_decile_2021': [],
        'seventh_decile_2021': [],
        'eighth_decile_2021': [],
        'ninth_decile_2021': [],
        'tenth_decile_2021': [],
        'all_income_groups_2023': [],
        'first_decile_2023': [],
        'second_decile_2023': [],
        'third_decile_2023': [],
        'fourth_decile_2023': [],
        'fifth_decile_2023': [],
        'sixth_decile_2023': [],
        'seventh_decile_2023': [],
        'eighth_decile_2023': [],
        'ninth_decile_2023': [],
        'tenth_decile_2023': [],
        'all_income_groups_pct_change_2018_to_2021': [],
        'first_decile_pct_change_2018_to_2021': [],
        'second_decile_pct_change_2018_to_2021': [],
        'third_decile_pct_change_2018_to_2021': [],
        'fourth_decile_pct_change_2018_to_2021': [],
        'fifth_decile_pct_change_2018_to_2021': [],
        'sixth_decile_pct_change_2018_to_2021': [],
        'seventh_decile_pct_change_2018_to_2021': [],
        'eighth_decile_pct_change_2018_to_2021': [],
        'ninth_decile_pct_change_2018_to_2021': [],
        'tenth_decile_pct_change_2018_to_2021': [],
        'all_income_groups_pct_change_2021_to_2023': [],
        'first_decile_pct_change_2021_to_2023': [],
        'second_decile_pct_change_2021_to_2023': [],
        'third_decile_pct_change_2021_to_2023': [],
        'fourth_decile_pct_change_2021_to_2023': [],
        'fifth_decile_pct_change_2021_to_2023': [],
        'sixth_decile_pct_change_2021_to_2023': [],
        'seventh_decile_pct_change_2021_to_2023': [],
        'eighth_decile_pct_change_2021_to_2023': [],
        'ninth_decile_pct_change_2021_to_2023': [],
        'tenth_decile_pct_change_2021_to_2023': []
    }

    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())
    
    for index, row in staged_dataframe.iterrows():
        if (index < 4) or (index > 163):
            continue
    
        for i in range(len(columns)):
            value = row.get(columns[i])
            
            data[new_columns[i]].append(value)
    
    df = pd.DataFrame(data)
    transformed_data = {}

    for new_column in new_columns:
        transformed_data[new_column] = []
    
    for _, row in df.iterrows():
        region_province_huc = str(row.get('region_province_huc')).lower()

        if region_province_huc == 'nan':
            continue

        for new_column in new_columns:
            value = str(row.get(new_column))

            if new_column == 'index':
                value = int(value)
            
            elif new_column == 'region_province_huc':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]
                value = ' '.join(value).replace('2/', '').replace('/', '')
            
            elif value.lower() == 'nan':
                value = 0.00
            
            else:
                value = round(float(value), 2)
            
            transformed_data[new_column].append(value)
    
    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)
    
    return transformed_dataframe

def transform_table_3a_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 3a dataset    
    '''
    data = {
        'index': [],
        'region_province_huc': [],
        'all_income_groups_2018': [],
        'first_decile_2018': [],
        'second_decile_2018': [],
        'third_decile_2018': [],
        'fourth_decile_2018': [],
        'fifth_decile_2018': [],
        'sixth_decile_2018': [],
        'seventh_decile_2018': [],
        'eight_decile_2018': [],
        'ninth_decile_2018': [],
        'tenth_decile_2018': [],
        'all_income_groups_2021': [],
        'first_decile_2021': [],
        'second_decile_2021': [],
        'third_decile_2021': [],
        'fourth_decile_2021': [],
        'fifth_decile_2021': [],
        'sixth_decile_2021': [],
        'seventh_decile_2021': [],
        'eight_decile_2021': [],
        'ninth_decile_2021': [],
        'tenth_decile_2021': [],
        'all_income_groups_2023': [],
        'first_decile_2023': [],
        'second_decile_2023': [],
        'third_decile_2023': [],
        'fourth_decile_2023': [],
        'fifth_decile_2023': [],
        'sixth_decile_2023': [],
        'seventh_decile_2023': [],
        'eight_decile_2023': [],
        'ninth_decile_2023': [],
        'tenth_decile_2023': []
    }

    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())

    for index, row in staged_dataframe.iterrows():
        if (index < 3) or (index > 162):
            continue

        for i in range(len(columns)):
            value = row.get(columns[i])
        
            data[new_columns[i]].append(value)
        
    df = pd.DataFrame(data)
    transformed_data = {}

    for new_column in new_columns:
        transformed_data[new_column] = []

    for _, row in df.iterrows():
        region_province_huc = str(row.get('region_province_huc')).lower()

        if region_province_huc == 'nan':
            continue
        
        for new_column in new_columns:
            value = str(row.get(new_column))

            if new_column == 'index':
                value = int(value)
            
            elif new_column == 'region_province_huc':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]
                value = ' '.join(value).replace('2/', '').replace('/', '')
    
            elif value.lower() == 'nan':
                value = 0.00

            else:
                value = round(float(value), 2)

            transformed_data[new_column].append(value)

    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)

    return transformed_dataframe 

def transform_table_4_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 4 dataset
    '''
    data = {
        'index': [],
        'region_province_huc': [],
        'all_income_groups_2018': [],
        'first_decile_2018': [],
        'second_decile_2018': [],
        'third_decile_2019': [],
        'fourth_decile_2018': [],
        'fifth_decile_2018': [],
        'sixth_decile_2018': [],
        'seventh_decile_2018': [],
        'eighth_decile_2018': [],
        'ninth_decile_2018': [],
        'tenth_decile_2018': [],
        'all_income_groups_2021': [],
        'first_decile_2021': [],
        'second_decile_2021': [],
        'third_decile_2021': [],
        'fourth_decile_2021': [],
        'fifth_decile_2021': [],
        'sixth_decile_2021': [],
        'seventh_decile_2021': [],
        'eighth_decile_2021': [],
        'ninth_decile_2021': [],
        'tenth_decile_2021': [],
        'all_income_groups_2023': [],
        'first_decile_2023': [],
        'second_decile_2023': [],
        'third_decile_2023': [],
        'fourth_decile_2023': [],
        'fifth_decile_2023': [],
        'sixth_decile_2023': [],
        'seventh_decile_2023': [],
        'eighth_decile_2023': [],
        'ninth_decile_2023': [],
        'tenth_decile_2023': [],
        'all_income_groups_pct_change_2018_to_2021': [],
        'first_decile_pct_change_2018_to_2021': [],
        'second_decile_pct_change_2018_to_2021': [],
        'third_decile_pct_change_2018_to_2021': [],
        'fourth_decile_pct_change_2018_to_2021': [],
        'fifth_decile_pct_change_2018_to_2021': [],
        'sixth_decile_pct_change_2018_to_2021': [],
        'seventh_decile_pct_change_2018_to_2021': [],
        'eighth_decile_pct_change_2018_to_2021': [],
        'ninth_decile_pct_change_2018_to_2021': [],
        'tenth_decile_pct_change_2018_to_2021': [],
        'all_income_groups_pct_change_2021_to_2023': [],
        'first_decile_pct_change_2021_to_2023': [],
        'second_decile_pct_change_2021_to_2023': [],
        'third_decile_pct_change_2021_to_2023': [],
        'fourth_decile_pct_change_2021_to_2023': [],
        'fifth_decile_pct_change_2021_to_2023': [],
        'sixth_decile_pct_change_2021_to_2023': [],
        'seventh_decile_pct_change_2021_to_2023': [],
        'eighth_decile_pct_change_2021_to_2023': [],
        'ninth_decile_pct_change_2021_to_2023': [],
        'tenth_decile_pct_change_2021_to_2023': []
    }

    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())

    for index, row in staged_dataframe.iterrows():
        if (index < 4) or (index > 164):
            continue

        for i in range(len(columns)):
            value = row.get(columns[i])

            data[new_columns[i]].append(value)

    df = pd.DataFrame(data)
    transformed_data = {}

    for new_column in new_columns:
        transformed_data[new_column] = []
    
    for _, row in df.iterrows():
        region_province_huc = str(row.get('region_province_huc')).lower()

        if region_province_huc == 'nan':
            continue
        
        for new_column in new_columns:
            value = str(row.get(new_column))
            
            if new_column == 'index':
                value = int(value)
            
            elif new_column == 'region_province_huc':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]
                value = ' '.join(value).replace('2/', '').replace('/', '')
            
            elif value.lower() == 'nan':
                value = 0.00
            
            else:
                value = round(float(value), 2)
            
            transformed_data[new_column].append(value)
    
    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)

    return transformed_dataframe

def transform_table_4a_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 1 dataset    
    '''
    data = {
        'index': [],
        'region_province_huc': [],
        'all_income_groups_2018': [],
        'first_decile_2018': [],
        'second_decile_2018': [],
        'third_decile_2018': [],
        'fourth_decile_2018': [],
        'fifth_decile_2018': [],
        'sixth_decile_2018': [],
        'seventh_decile_2018': [],
        'eighth_decile_2018': [],
        'ninth_decile_2018': [],
        'tenth_decile_2018': [],
        'all_income_groups_2021': [],
        'first_decile_2021': [],
        'second_decile_2021': [],
        'third_decile_2021': [],
        'fourth_decile_2021': [],
        'fifth_decile_2021': [],
        'sixth_decile_2021': [],
        'seventh_decile_2021': [],
        'eighth_decile_2021': [],
        'ninth_decile_2021': [],
        'tenth_decile_2021': [],
        'all_income_groups_2023': [],
        'first_decile_2023': [],
        'second_decile_2023': [],
        'third_decile_2023': [],
        'fourth_decile_2023': [],
        'fifth_decile_2023': [],
        'sixth_decile_2023': [],
        'seventh_decile_2023': [],
        'eighth_decile_2023': [],
        'ninth_decile_2023': [],
        'tenth_decile_2023': []
    }

    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())

    for index, row in staged_dataframe.iterrows():
        if (index < 3) or (index > 162):
            continue

        for i in range(len(columns)):
            value = row.get(columns[i])

            data[new_columns[i]].append(value)

    df = pd.DataFrame(data)
    transformed_data = {}

    for new_column in new_columns:
        transformed_data[new_column] = []
    
    for _, row in df.iterrows():
        region_province_huc = str(row.get('region_province_huc')).lower()

        if region_province_huc == 'nan':
            continue

        for new_column in new_columns:
            value = str(row.get(new_column))

            if new_column == 'index':
                value = int(value)
            
            elif new_column == 'region_province_huc':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XI', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]
                value = ' '.join(value).replace('2/', '').replace('/', '')

            elif value.lower() == 'nan':
                value = 0.00
            
            else:
                value = round(float(value), 2)
            
            transformed_data[new_column].append(value)
    
    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)

    return transformed_dataframe
    
def transform_table_5_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 5
    '''
    data = {
        'index': [],
        'region_province_huc': [],
        'gini_coefficient_2018': [],
        'palma_ratio_2018': [],
        'gini_coefficient_2021': [],
        'palma_ratio_2021': [],
        'gini_coefficient_2023': [],
        'palma_ratio_2023': []
    }

    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())

    for index, row in staged_dataframe.iterrows():
        if (index < 3) or (index > 162):
            continue

        for i in range(len(columns)):
            value = row.get(columns[i])

            data[new_columns[i]].append(value)
    
    df = pd.DataFrame(data)
    transformed_data = {}

    for new_column in new_columns:
        transformed_data[new_column] = []
    
    for _, row in df.iterrows():
        region_province_huc = str(row.get('region_province_huc')).lower()

        if region_province_huc == 'nan':
            continue

        for new_column in new_columns:
            value = str(row.get(new_column))
            
            if new_column == 'index':
                value = int(value)
            
            elif new_column == 'region_province_huc':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XI', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]
                value = ' '.join(value).replace('2/', '').replace('/', '')
            
            elif value.lower() == 'nan':
                value = 0.00
            
            else:
                value = round(float(value), 2)
            
            transformed_data[new_column].append(value)

    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)

    return transformed_dataframe

def transform_table_6_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 6 dataset
    '''
    data = {
        'index': [],
        'region_province_huc_by_sources_of_income': [],
        'in_percent_2018': [],
        'in_percent_2021': [],
        'in_percent_2023': [],
        'pct_point_change_2018_to_2021': [],
        'pct_point_change_2021_to_2023': []
    }

    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())
    
    for index, row in staged_dataframe.iterrows():
        if (index < 3) or (index > 2215):
            continue

        for i in range(len(columns)):
            value = row.get(columns[i])

            data[new_columns[i]].append(value)

    df = pd.DataFrame(data)
    transformed_data = {}

    for new_column in new_columns:
        transformed_data[new_column] = []
    
    for _, row in df.iterrows():
        region_province_huc_by_sources_of_income = str(row.get('region_province_huc_by_sources_of_income')).lower()

        if region_province_huc_by_sources_of_income == 'nan':
            continue

        for new_column in new_columns:
            value = str(row.get(new_column))

            if new_column == 'index':
                value = int(value)

            elif new_column == 'region_province_huc_by_sources_of_income':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]
                value = ' '.join(value).replace('2/', '').replace('/', '')

            elif value.lower() == 'nan':
                value = 0.00
            
            else:
                value = round(float(value), 2)
            
            transformed_data[new_column].append(value)
    
    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)
    
    return transformed_dataframe

def transform_table_7_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        table 7 dataset        
    '''
    data = {
        'index': [],
        'region_province_huc_by_expenditure_group': [],
        'in_percent_2018': [],
        'in_percent_2021': [],
        'in_percent_2023': [],
        'pct_point_change_2018_to_2021': [],
        'pct_point_change_2021_to_2023': []
    }

    new_columns = list(data.keys())
    columns = list(staged_dataframe.keys())

    for index, row in staged_dataframe.iterrows():
        if (index < 3) or (index > 3041):
            continue

        for i in range(len(columns)):
            value = row.get(columns[i])
            data[new_columns[i]].append(value)
    
    df = pd.DataFrame(data)
    transformed_data = {}
    
    for new_column in new_columns:
        transformed_data[new_column] = []
    
    for _, row in df.iterrows():
        region_province_huc_by_expenditure_group = str(row.get('region_province_huc_by_expenditure_group')).lower()

        if region_province_huc_by_expenditure_group == 'nan':
            continue

        for new_column in new_columns:
            value = str(row.get(new_column))

            if new_column == 'index':
                value = int(value)
            
            elif new_column == 'region_province_huc_by_expenditure_group':
                value = value.split()
                value = [word.capitalize().strip() if word not in ['I', 'II', 'III', 'IV', 'IVA', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XI', 'XII', 'NCR', 'CAR', 'BARMM'] else word.upper().strip() for word in value]
                value = ' '.join(value).replace('2/', '').replace('/', '')

            elif value.lower() == 'nan':
                value = 0.00
            
            else:
                value = round(float(value), 2)
            
            transformed_data[new_column].append(value)
    
    transformed_dataframe = pd.DataFrame(transformed_data)
    transformed_dataframe.drop(columns=['index'], inplace=True)

    return transformed_dataframe