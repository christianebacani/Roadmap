'''
    Clean staged datasets
'''
import pandas as pd

def clean_staged_datasets(stage_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Clean function to clean staged datasets
    '''
    columns = list(stage_dataframe.keys())
    # We can just use a dictionary that will be converted into a dataframe and not concatenate because it will cause more runtime
    clean_data = {}
    
    for column in columns:
        clean_data[column] = []
    
    for index, row in stage_dataframe.iterrows():
        # Don't include index 0, because it contains the unnecessary data
        if index == 0:
            continue

        # Cleaning the values per row by their corresponding column names and replacing invalid values
        for column in columns:
            value = str(row.get(column)).strip()
    
            if column in ['size', 'industry_description']:
                value = value.replace('..', '').strip()
            
            elif column in ['geolocation', 'region']:
                value = value.replace('..', '').split()
                value = [word.capitalize() if word != 'in' else 'in' for word in value]
                value = ' '.join(value)

            elif value in ['..', '-', 'c', 's', 'nan']:
                value = 0

            else:
                value = int(value)

            clean_data[column].append(value)

    # Convert dictionary to dataframe and remove duplicate rows
    clean_staged_dataframe = pd.DataFrame(clean_data)
    clean_staged_dataframe.drop_duplicates(keep='first', inplace=True)
    
    return clean_staged_dataframe

