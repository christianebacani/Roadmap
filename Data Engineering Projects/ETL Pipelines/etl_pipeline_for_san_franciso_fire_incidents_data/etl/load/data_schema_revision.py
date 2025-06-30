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

def initialize_dimension_tables() -> None:
    '''
        Initialize Dimension Tables Function
    '''
    # Initialize the columns
    columns = list(pd.read_csv('data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data(1).csv').keys())
    dimension_tables = []

    # Initialize the structure of the dimension tables
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        if column == 'id':
            dimension_tables.append({
                'id': []
            })
        
        else:
            primary_key = f'{column}_id'
            dimension_tables.append({
                primary_key: [],
                column: []
            })

    # Initialize the non-key attributes of dimension tables    
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue
        
        values = []

        for dataset_number in range(1, 706 + 1):
            filepath = f'data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
            partitioned_dataframe = pd.read_csv(filepath)

            values.extend(list(partitioned_dataframe[column]))
            print(f'Successfully initialize the non-key attributes of column: {column} from san_francisco_fire_incidents_data({dataset_number}).csv for initialization of dimension tables')

        for i in range(len(dimension_tables)):
            if column not in dimension_tables[i]:
                continue

            dimension_tables[i][column] = list(set(values))

    # Initialize the key attributes of dimension tables    
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data() or column == 'id':
            continue

        for i in range(len(dimension_tables)):
            if column not in dimension_tables[i]:
                continue
            
            total_number_of_values = len(dimension_tables[i][column])
            primary_key_values = []

            for primary_key_value in range(1, total_number_of_values + 1):
                primary_key_values.append(primary_key_value)
                print(f'Successfully initialize primary key value: {primary_key_value} from column: {column} for initialization of dimension tables')
            
            primary_key = f'{column}_id'
            dimension_tables[i][primary_key] = primary_key_values

    # Initialize the dimension tables as a dataframe    
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        for i in range(len(dimension_tables)):
            if column not in dimension_tables[i]:
                continue
            
            target_filepath = f'data/processed/san_francisco_fire_incidents_data/dim_{column}.csv'
            dimension_dataframe = pd.DataFrame(dimension_tables[i])
            dimension_dataframe.to_csv(target_filepath, index=False)
            
            print(f'Successfully initialize dim_{column} dimension tables')

def initialize_facts_table() -> None:
    '''
        Initialize Facts Table Function
    '''
    # TODO: Implement more functionalities here...

def revise_schema(dataframe: pd.DataFrame) -> None:
    '''
        Revise schema Function
    '''
    # Remove unnecessary columns
    dataframe.drop(columns=['data_as_of', 'data_loaded_at'], inplace=True)

    # Data partitioning for faster processing of initialization of dimension and facts table/s
    for dataset_number, row_number in enumerate(range(0, 705908 + 1, 1000)):
        dataset_number += 1
        
        target_filepath = f'data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
        partitioned_dataframe = dataframe[row_number : row_number + 1000]
        partitioned_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully partitioned integrated processed dataset from {row_number}-{row_number + 999} rows for data schema revision process')

    # Remove the processed dataset after partitioning
    if os.path.exists('data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_processed_data.csv'):
        os.remove('data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_processed_data.csv')
    
    # Initialize the dimension tables
    initialize_dimension_tables()