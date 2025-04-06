'''
    Extracting raw data by staging it
    to a target directory path
'''
from glob import glob
import os
import pandas as pd
def extract(raw_datasets_dir: str) -> None:
    '''
        Extract function of raw data by staging it
        to a target directory path
    '''
    stage_raw_datasets_dir = 'ETL Pipeline for Philippine PSA Summary Statistics/data/stage'
    
    # Staging the datasets per sub-directory path of raw directory so we use glob function
    for raw_datasets_subdir in glob(f'{raw_datasets_dir}/*'):
        subdir_name = str(raw_datasets_subdir).replace('ETL Pipeline for Philippine PSA Summary Statistics/data/raw\\', '')

        extracted_dataframes = {}

        for dataset in glob(f'{raw_datasets_subdir}/*.csv'):
            # Getting the filename by splitting the filepath name string
            dataset_lst = str(dataset).split(f'\\{subdir_name}\\')
            filename = dataset_lst[1]

            extracted_dataframe = pd.read_csv(dataset, encoding='cp1252')
            print(f'Successfully extracted {dataset}')

            # Mapped to dictionary so that it can store also the filename and dataframe as a key value pair
            extracted_dataframes[filename] = extracted_dataframe

        # We use os routine for checking if the target directory path are already exists or not
        target_stage_raw_datasets_subdir = f'{stage_raw_datasets_dir}/{subdir_name}'

        if not os.path.exists(target_stage_raw_datasets_subdir):
            os.makedirs(target_stage_raw_datasets_subdir)

        # We can use the key which is filename to store the dataframe together with the filename key and the target directory path
        for filename, dataframe in extracted_dataframes.items():
            filepath = f'{target_stage_raw_datasets_subdir}/{filename}'
            dataframe.to_csv(filepath)
            print(f'Successfully staged datasets from {subdir_name} sub-directory')






    
        


