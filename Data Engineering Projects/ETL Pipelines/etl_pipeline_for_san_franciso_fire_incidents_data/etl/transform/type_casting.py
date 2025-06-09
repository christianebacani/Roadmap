'''
    Data Type Casting Module
'''
import pandas as pd
from datetime import datetime

def cast_datatype(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Type Casting Function
    '''
    # Initializing a dictionary for storing data after type casting process
    columns = list(dataframe.keys())
    data = {}

    for column in columns:
        data[column] = []

   # TODO : Refactor the type casting process from the function