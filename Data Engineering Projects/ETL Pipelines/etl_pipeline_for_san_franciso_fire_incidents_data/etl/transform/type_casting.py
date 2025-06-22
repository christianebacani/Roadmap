'''
    Type Casting Module
'''
import pandas as pd
from datetime import datetime

def cast_data_type(dataframe: pd.DataFrame) -> None:
    '''
        Type Casting Function
    '''
    # Using .keys() method to get all the variable/field names
    columns = list(dataframe.keys())

    columns_and_distinct_values = {}

    # Get the distinct values of every columns to know the data type
    for column in columns:
        values = []

        for row_number in range(0, 705908 + 1, 1000):
            values.extend(list(dataframe[column][row_number : row_number + 1000]))

            print(f'Successfully extracted the values of column: {column} from {row_number}-{row_number + 999} rows for type casting process')
        
        values = list(set(values))
        columns_and_distinct_values[column] = values

    columns_and_data_type = {}

    # Get the maximum frequencies of data type per value of every columns to initialize their standard data type
    for column, distinct_values in columns_and_distinct_values.items():
        datatype_frequencies = {
            'nan': 0,
            'datetime': 0,
            'integer': 0,
            'float': 0,
            'string': 0
        }
        
        for value in distinct_values:
            if str(value).lower() == 'nan':
                datatype_frequencies['nan'] = datatype_frequencies['nan'] + 1
                continue
            
            try:
                datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.%f')
                datatype_frequencies['datetime'] = datatype_frequencies['datetime'] + 1
                continue

            except ValueError:
                pass

            if str(value).isdigit():
                datatype_frequencies['integer'] = datatype_frequencies['integer'] + 1
                continue

            try:
                float(value)
                datatype_frequencies['float'] = datatype_frequencies['float'] + 1
            
            except ValueError:
                datatype_frequencies['string'] = datatype_frequencies['string'] + 1
        
        if datatype_frequencies['string'] > 0:
            columns_and_data_type[column] = 'string'
            continue

        maximum_frequencies = max(datatype_frequencies.values())

        for data_type, frequency in datatype_frequencies.items():
            if maximum_frequencies != frequency:
                continue

            columns_and_data_type[column] = data_type
            break
    
    # Partition integrated staged dataset for faster processing
    for dataset_number, row_number in enumerate(range(0, 705908 + 1, 1000)):
        dataset_number += 1
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'

        partitioned_dataframe = dataframe[row_number : row_number + 1000]
        partitioned_dataframe.to_csv(filepath, index=False)

        print(f'Successfully partitioned integrated staged dataset to san_francisco_fire_incidents_data({dataset_number}).csv for type casting process')
    
    # Perform type casting operation for the partitioned dataset
    for dataset_number in range(1, 706 + 1):
        data = {}

        for column in columns:
            data[column] = []
        
        filepath = f'data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        partitioned_dataframe = pd.read_csv(filepath)
        
        for _, row in partitioned_dataframe.iterrows():
            for column in columns:
                value = row.get(column)

                if str(value).lower() == 'nan':
                    data[column].append(None)
                    continue
                
                if columns_and_data_type[column] == 'integer':
                    value = int(value)
                
                elif columns_and_data_type[column] == 'float':
                    value = float(value)
                
                elif columns_and_data_type[column] == 'string':
                    value = str(value)
                
                elif column == 'incident_date':
                    value = datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.%f').date()
                
                else:
                    value = datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.%f')
                
                data[column].append(value)

        type_casted_dataframe = pd.DataFrame(data)
        type_casted_dataframe.to_csv(filepath, index=False)

        print(f'Successfully perform type casting to san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset')