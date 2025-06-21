'''
    Type Casting Module
'''
import pandas as pd
from datetime import datetime

def cast_data_type(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Type Casting Function
    '''
    # Using .keys() method to get all the variable/field names
    columns = list(dataframe.keys())

    # TODO: Add more functions here...