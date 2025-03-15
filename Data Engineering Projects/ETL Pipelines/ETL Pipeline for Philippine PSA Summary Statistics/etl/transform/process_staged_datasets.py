'''
    Processing staged datasets from directory
'''
from glob import glob
from transform.transform_staged_datasets import transform

def process(stage_datasets_dir: str) -> None:
    '''
        Process function to staged datasets from directory
    '''
    
    # Getting the datasets per sub-directory path by using glob function
    for staged_datasets_subdir in glob(f'{stage_datasets_dir}/*'):
        subdir_name = str(staged_datasets_subdir).replace('ETL Pipeline for Philippine PSA Summary Statistics/data/stage\\', '')
        transform(staged_datasets_subdir, subdir_name)
            