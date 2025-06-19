'''
    Data Schema Revision Module
'''
import pandas as pd
import os

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

def revise_schema(dataframe: pd.DataFrame) -> None:
    '''
        Data Schema Revision Function
    '''
    # Remove unnecessary columns
    dataframe.drop(columns=['data_as_of', 'data_loaded_at'], inplace=True)
    
    # Using .keys() method to get all the variable/field names
    columns = list(dataframe.keys())

    facts_data = {}
    dimensions_data = []

    # Initialize the dimensions data consisting of primary keys and non-key attributes
    for column in columns:
        if column == 'id':
            dimensions_data.append({
                'id': []
            })
            continue
        
        if column not in return_the_list_of_columns_for_facts_data():
            dimensions_data.append({
                f'{column}_id': [],
                column: []
            })
    
    # Initialize the foreign key for the facts data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        if column == 'id':
            facts_data['id'] = []
            continue

        foreign_key = f'{column}_id'
        facts_data[foreign_key] = []

    # Initialize the numeric columns for the facts data    
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            facts_data[column] = []
    
    # Initialize the values of non-key attributes of the dimension data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        values = []

        for row_number in range(0, 705909, 1000):
            group_of_values = list(dataframe[column][row_number : row_number + 1000])
            values.extend(group_of_values)
            print(f'Successfully extracted the values of column: {column} for initializing the dimension data')
        
        values = list(set(values))
        
        for i in range(len(dimensions_data)):
            if column not in dimensions_data[i]:
                continue

            dimensions_data[i][column] = values
            break
        
    # Initialize the values of key attributes of the dimension data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        if column == 'id':
            continue

        for i in range(len(dimensions_data)):
            if column not in dimensions_data[i]:
                continue
            
            total_number_of_values = len(dimensions_data[i][column])
            primary_key_values = []

            for primary_key_value in range(1, total_number_of_values + 1):
                primary_key_values.append(primary_key_value)
                print(f'Successfully extracted the primary key value: {primary_key_value} from {column} column for initializing the dimension data')
            
            primary_key = f'{column}_id'
            dimensions_data[i][primary_key] = primary_key_values
    
    # Initialize the dimension data dictionary as a dimension dataframe using the columns of integrated dataset
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        for i in range(len(dimensions_data)):
            if column not in dimensions_data[i]:
                continue

            filepath = f'data/processed/san_francisco_fire_incidents_data/dim_{column}.csv'
            dimension_dataframe = pd.DataFrame(dimensions_data[i])
            dimension_dataframe.to_csv(filepath, index=False)

            print(f'Successfully initialize dim_{column} dimension table')
    
    subdirectory_path = 'data/processed/san_francisco_fire_incidents_data'

    # Partition integrated processed dataset for faster processing of initialization of facts data
    for dataset_number, row_number in enumerate(range(0, 705909, 1000)):
        dataset_number += 1
        partitioned_dataframe = dataframe[row_number : row_number + 1000]

        filepath = f'{subdirectory_path}/san_francisco_fire_incidents_data({dataset_number}).csv'
        partitioned_dataframe.to_csv(filepath, index=False)

        print(f'Successfully partitioned {row_number}-{row_number + 1000} rows from the integrated processed dataset for data schema revision')