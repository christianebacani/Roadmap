'''
    Data Transformation Module
'''
import pandas as pd
from transform.data_imputation import impute_values_from_the_integrated_datasetr
from transform.type_casting import cast_data_type
from transform.format_revision import revise_format

def transform_staged_dataset(staged_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Transformation Function
    '''
    # Data imputation using a function from other modules
    staged_dataframe = impute_values_from_the_integrated_datasetr(staged_dataframe)

    # Chunked the integrated dataset for other transformation process for scalability and faster processing time    
    for dataset_number, row_number in enumerate(range(0, 705909, 1000)):
        dataset_number += 1

        dataframe = staged_dataframe[row_number : row_number + 1000]
        target_filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        dataframe.to_csv(target_filepath, index=False)
        print(f'Successfully chunked {row_number}-{row_number} rows from the integrated staged dataset for other transformation processes')

    # Performing other transformation processes (Type casting, Data format revision, and Data Deduplication)
    for dataset_number in range(1, 707):
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        
        type_casted_dataframe = cast_data_type(pd.read_csv(filepath))
        format_revised_dataframe = revise_format(type_casted_dataframe)

        transformed_dataframe = format_revised_dataframe
        transformed_dataframe.to_csv(filepath, index=False)

        print(f'Successfully transformed the dataset san_francisco_fire_incidents_data({dataset_number}).csv')