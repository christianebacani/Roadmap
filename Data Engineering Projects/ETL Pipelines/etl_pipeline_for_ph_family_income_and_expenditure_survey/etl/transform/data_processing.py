'''
    Data Processing Module
'''
from glob import glob
from transform.tables_to_transform_function_mappings import map_tables_to_transformation_functions

def processing_staged_datasets(stage_datasets_dir_path: str) -> None:
    '''
        Processing function to process
        staged datasets from stage datasets 
        directory path
    '''
    transform_dataset_functions = map_tables_to_transformation_functions()
    processed_datasets_dir_path = 'data/processed'

    for csv_file in glob(f'{stage_datasets_dir_path}/*.csv'):
        filepath = str(csv_file).split('data/stage\\')
        filepath = filepath[1]
        table_name = filepath[:8].replace('_', '')
        
        available_table_names_to_transform = list(transform_dataset_functions.keys())

        if table_name in available_table_names_to_transform:
            transformed_dataframe = transform_dataset_functions[table_name]
            target_filepath = f'{processed_datasets_dir_path}/{filepath}'
            transformed_dataframe.to_csv(target_filepath, index=False)

    print('Successfully transformed all staged datasets')
    