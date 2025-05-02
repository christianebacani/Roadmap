'''
    Data Processing Module
'''
import os
import pandas as pd
from glob import glob
from transform.transform import transform_police_dept_inci_reports_2003_to_may_2018_datasets
from transform.transform import transform_police_dept_inci_reports_2018_to_present_datasets
from transform.transform import transform_summary_of_inci_reports_datasets

def processing_staged_datasets(stage_subdir_path: str) -> None:
    processed_datasets_dir_path = 'data/processed'
    target_subdir_path = f'{processed_datasets_dir_path}/{stage_subdir_path.replace('data/stage/', '')}'
    
    if not os.path.exists(target_subdir_path):
        os.makedirs(target_subdir_path)
    
    if len(glob(f'{target_subdir_path}/*.csv')) > 0:
        return

    base_filename = stage_subdir_path.replace('data/stage/', '')
    total_datasets = len(glob(f'{stage_subdir_path}/*.csv'))
    
    for dataset_num in range(1, total_datasets + 1):
        staged_dataset_filepath = f'{stage_subdir_path}/{base_filename}({dataset_num}).csv'
        staged_dataframe = pd.read_csv(staged_dataset_filepath)
        
        if base_filename == 'police_dept_inci_reports_2003_to_may_2018':
            transformed_dataframe = transform_police_dept_inci_reports_2003_to_may_2018_datasets(staged_dataframe)
                    
        elif base_filename == 'police_dept_inci_reports_2018_to_present':
            transformed_dataframe = transform_police_dept_inci_reports_2018_to_present_datasets(staged_dataframe)
                    
        elif base_filename == 'summary_of_inci_reports':
            transformed_dataframe = transform_summary_of_inci_reports_datasets(staged_dataframe)
        
        target_filepath = f'{target_subdir_path}/{base_filename}({dataset_num}).csv'
        transformed_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully transformed {base_filename}({dataset_num}) dataset from stage dataset directory path')