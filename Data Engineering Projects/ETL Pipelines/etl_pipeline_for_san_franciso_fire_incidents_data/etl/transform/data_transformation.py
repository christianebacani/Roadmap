'''
    Data Transformation Module
'''
import pandas as pd
from transform.data_imputation import impute_values_from_the_integrated_datasetr
from transform.type_casting import cast_data_type

def transform_staged_dataset(staged_dataframe: pd.DataFrame) -> None:
    '''
        Data Transformation Function
    '''
    # Data imputation and type casting
    staged_dataframe = impute_values_from_the_integrated_datasetr(staged_dataframe)

    # TODO: Implement more functionalities here...