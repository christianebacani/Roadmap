'''
    Data Schema Revision Module
'''
import pandas as pd
import os
from datetime import datetime

def return_the_list_of_columns_for_facts_data() -> str:
    '''
        Return function to return the list of columns
        facts data
    '''
    return [
        'suppression_units',
        'suppression_personnel',
        'ems_units',
        'ems_personnel',
        'other_unit',
        'other_personnel',
        'estimated_property_loss',
        'estimated_contents_loss',
        'fire_fatalities',
        'fire_injuries',
        'civilian_fatalities',
        'civilian_injuries',
        'number_of_alarms',
        'number_of_floors_with_minimum_damage',
        'number_of_floors_with_significant_damage',
        'number_of_floors_with_heavy_damage',
        'number_of_floors_with_extreme_damage',
        'number_of_sprinkler_heads_operating'
    ]

def get_the_foreign_key_value(dim_dataframe: pd.DataFrame, target_column: str, target_value: datetime | int | float | str) -> str | int | datetime | float:
    '''
        Get function to get the foreign key value
    '''
    for _, row in dim_dataframe.iterrows():
        primary_key = f'{target_column}_id'
        primary_key_value = row.get(primary_key)
        value = row.get(target_column)
            
        if target_column == 'incident_date':
            value = datetime.strptime(str(value), '%Y-%m-%d')
            target_value = datetime.strptime(str(target_value), '%Y-%m-%d')

        elif isinstance(target_value, datetime):
            value = datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.%f')
            target_value = datetime.strptime(str(target_value), '%Y-%m-%dT%H:%M:%S.%f')

        elif str(target_value).isdigit():
            value = int(value)
            target_value = int(target_value)
        
        elif isinstance(target_value, float):
            value = float(value)
            target_value = float(value)
        
        else:
            value = str(value)
            target_value = str(target_value)
        
        if target_value == value:
            return primary_key_value

def revise_schema(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Schema Revision Function
    '''
    # Remove unnecessary columns
    dataframe.drop(columns=['data_as_of', 'data_loaded_at'], inplace=True)

    # Get the columns
    columns = list(dataframe.keys())

    # Partition the integrated processed dataset
    for dataset_number, row_number in enumerate(range(0, 705908 + 1, 1000)):
        dataset_number += 1
        target_filepath = f'data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'

        partitioned_dataframe = dataframe[row_number : row_number + 1000]
        partitioned_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully partitioned integrated processed dataset of {row_number}-{row_number + 999} rows for data schema revision process')

    # Remove the integrated processed dataset after data partitioning
    if os.path.exists('data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_processed_data.csv'):
        os.remove('data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_processed_data.csv')

    dimension_data, facts_data = [], {}

    # Initialize the structure of dimension data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        if column == 'id':
            dimension_data.append({
                'id': []
            })

        else:
            primary_key = f'{column}_id'
            dimension_data.append({
                primary_key: [],
                column: []
            })

    # Initialize the structure of facts data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        if column == 'id':
            facts_data['id'] = []
        
        else:
            foreign_key = f'{column}_id'
            facts_data[foreign_key] = []
    
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            facts_data[column] = []

    # Initialize the non-key attributes of dimension data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue
        
        values = []

        for dataset_number in range(1, 706 + 1):
            filepath = f'data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
            partitioned_dataframe = pd.read_csv(filepath)

            values.extend(list(partitioned_dataframe[column]))
            print(f'Successfully extracted the non-key attributes of column: {column} from san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset for initialization of dimension data')
        
        values = list(set(values))

        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            dimension_data[i][column] = values
    
    # Initialize the key-attributes of dimension data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data() or column == 'id':
            continue

        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            total_number_of_key_attributes = len(dimension_data[i][column])
            key_attributes = []

            for key_attribute in range(1, total_number_of_key_attributes + 1):
                key_attributes.append(key_attribute)
                print(f'Successfully initialized the key attribute: {key_attribute} for column: {column} for initialization of dimension data')
                
            primary_key = f'{column}_id'
            dimension_data[i][primary_key] = key_attributes
    
    # Initialize the dimension data dictionary as a dataframe
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            target_filepath = f'data/processed/san_francisco_fire_incidents_data/dim_{column}.csv'
            dimension_dataframe = pd.DataFrame(dimension_data[i])
            dimension_dataframe.to_csv(target_filepath, index=False)

            print(f'Successfully initialize dim_{column} dimension table')

    # Initialize the foreign key attributes and numeric attributes of facts data
    for dataset_number in range(1, 706 + 1):
        filepath = f'data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        partitioned_dataframe = pd.read_csv(filepath)

        for _, row in partitioned_dataframe.iterrows():
            for column in columns:
                value = row.get(column)

                if column in return_the_list_of_columns_for_facts_data():
                    facts_data[column].append(value)
                    continue

                if column == 'id':
                    foreign_key_value = value
                    facts_data['id'].append(foreign_key_value)
                
                else:
                    dimension_dataframe = pd.read_csv(f'data/processed/san_francisco_fire_incidents_data/dim_{column}.csv')
                    foreign_key_value = get_the_foreign_key_value(dimension_dataframe, column, value)
                    
                    primary_key = f'{column}_id'
                    facts_data[primary_key].append(foreign_key_value)

        print(f'Successfully initialized the foreign key attributes of facts data in san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset for initialization of facts data')
    
    # Initialize the facts data dictionary as a dataframe
    target_filepath = 'data/processed/san_francisco_fire_incidents_data/facts_fire_incidents_data.csv'
    facts_dataframe = pd.DataFrame(facts_data)
    facts_dataframe.to_csv(target_filepath, index=False)

    print(f'Successfully initialize facts_fire_incidents_data facts table')

    # Remove partitioned dataset after data schema revision process
    for dataset_number in range(1, 706 + 1):
        filepath = f'data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        
        if os.path.exists(filepath):
            os.remove(filepath)

            print(f'Successfully removed san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset after transformation phase')