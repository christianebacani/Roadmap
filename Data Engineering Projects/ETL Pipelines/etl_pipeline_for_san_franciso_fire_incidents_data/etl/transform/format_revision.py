'''
    Data Format Revision Module
'''
import pandas as pd
from datetime import datetime

def revise_data_format(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Format Revision Function
    '''
    # Initializing a dictionary for storing data after data format revisioning proces
    columns = list(dataframe.keys())
    data = {}

    for column in columns:
        data[column] = []
    
    # Format revisioning for making sure the values are consistent to minimize deviation
    for _, row in dataframe.iterrows():
        for column in columns:
            value = row.get(column)

            if column == 'address':
                street_type_abbreviations = {
                    'St.': 'Street',
                    'Rd.': 'Road',
                    'Av.': 'Avenue',
                    'Blvd.': 'Boulevard',
                    'Dr.': 'Drive',
                    'Ln.': 'Lane',
                    'Wy.': 'Way,',
                    'Ct.': 'Court',
                    'Pl.': 'Place',
                    'Cir.': 'Circle',
                    'Hy.': 'Highway',
                    'Tpke.': 'Turnpike',
                    'Expy.': 'Expressway',
                    'Sq.': 'Square',
                    'Bl': 'Block'
                }
                for abbreviation, street_type in street_type_abbreviations.items():
                    value = str(value).replace(abbreviation, street_type)
                
                value = value.split()
                
                for i in range(len(value)):
                    value[i] = value[i].capitalize()
                
                value = ' '.join(value)

            elif column == 'city':
                abbreviations = {
                    'SFO': 'San Francisco International Airport area',
                    'SF': 'San Francisco'
                }

                for abbreviation, name in abbreviations.items():
                    value = str(value).replace(abbreviation, name)

            elif column == 'point':
                value = str(value).replace('POINT (', '')
                value = str(value).replace(')', '')
                value = ', '.join(value.split())
            
            elif isinstance(value, str) and '-' in value:
                value = str(value).replace('-', ' - ')
            
            else:
                pass

            data[column].append(value)
    
    return pd.DataFrame(data)