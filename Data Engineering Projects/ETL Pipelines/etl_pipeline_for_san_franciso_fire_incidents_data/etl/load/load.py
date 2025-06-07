'''
    Data Loading Module
'''
from load.data_integration import integrate_dataset
from load.schema_enforcement import enforce_schema
import os

def load_to_postgresql_db(subdirectory_path: str) -> None:
    '''
        Data Loading Function
    '''
    # Integrate datasets for schema manipulation process later on
    integrated_dataframe = integrate_dataset(subdirectory_path)

    # Initialize a directory path to stage dataset/s before schema enforcement and validation process
    integrated_datasets_directory_path = 'data/integrated_datasets' 
    target_subdirectory_path = f'{integrated_datasets_directory_path}/san_franscico_fire_incidents_data'

    if not os.path.exists(target_subdirectory_path):
        os.makedirs(target_subdirectory_path)
    
    # Load to the target path for testing purposes (Also to check the behavior of the variables)
    target_filepath = f'{target_subdirectory_path}/san_francisco_fire_incidents_integrated_dataset.csv'
    integrated_dataframe.to_csv(target_filepath, index=False)
    print('Successfully integrated and staged the datasets for schema enforcing and validation process')

    # Enforce schema
    enforce_schema(integrated_dataframe)