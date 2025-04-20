'''
    Extract Module
'''
from glob import glob
import pandas as pd

def extract_raw_datasets(raw_datasets_dir_path: str) -> None:
    '''
        Extract function to extract
        raw datasets from raw datasets 
        directory path
    '''
    stage_data_dir_path = 'data/stage'

    for excel_file in glob(f'{raw_datasets_dir_path}/*.xlsx'):
        filepath = str(excel_file).split('data/raw\\')
        filepath = filepath[1].replace('.xlsx', '').split()
        filepath = [word.lower().replace('.', '').replace(',', '') for word in filepath]
        filepath = '_'.join(filepath)
        
        extracted_dataframe = pd.read_excel(excel_file, engine='openpyxl')
        target_filepath = f'{stage_data_dir_path}/{filepath}.csv'
        extracted_dataframe.to_csv(target_filepath)
    
    print('Successfully staged all the raw datasets')
