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

    # Remove the integrated processed dataset after partitioning
    if os.path.exists('data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_processed_data.csv'):
        os.remove('data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_processed_data.csv')
    
    columns = list(dataframe.keys())
    dimension_data = []

    # Initialize the structure of dimension tables
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

    # Initializing the non-key attributes of the dimension tables    
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue
        
        values = []

        for dataset_number in range(1, 706 + 1):
            filepath = f'data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv'
            partitioned_dataframe = pd.read_csv(filepath)
            values.extend(list(partitioned_dataframe[column]))

            print(f'Successfully initialized non-key attributes of column: {column} from san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset for initialization of dimension tables')
        
        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            dimension_data[i][column] = list(set(values))
    
    # Initializingf the key attributes of dimension tables
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        if column == 'id':
            continue

        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            total_number_of_values = len(dimension_data[i][column])
            primary_key_values = []

            for primary_key_value in range(1, total_number_of_values + 1):
                primary_key_values.append(primary_key_value)
                print(f'Successfully initialized key attribute: {primary_key_value} from column: {column} for initialization of dimension tables')
            
            primary_key = f'{column}_id'
            dimension_data[i][primary_key] = primary_key_values
    
    # Initialize the dimension tables as a dataframe
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            dimension_dataframe = pd.DataFrame(dimension_data[i])
            target_filepath = f'data/processed/san_francisco_fire_incidents_data/dim_{column}.csv'
            dimension_dataframe.to_csv(target_filepath, index=False)

            print(f'Successfully initialize dim_{column} dimension table')

    facts_data = {}

    # Initialize the structure of facts table
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
            continue

        facts_data[column] = []
    
    # Initialize foreign key and numeric values of facts table
    for dataset_number in range(1, 706 + 1):
        partitioned_dataframe = pd.read_csv(f'data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_data({dataset_number}).csv')

        for _, row in partitioned_dataframe.iterrows():
            for column in columns:
                value = row.get(column)

                if column in return_the_list_of_columns_for_facts_data():
                    facts_data[column].append(value)
                    continue

                if column == 'id':
                    facts_data['id'].append(value)
                    continue

                dimension_dataframe = pd.read_csv(f'data/processed/san_francisco_fire_incidents_data/dim_{column}.csv')

                try:
                    target_index = dimension_dataframe.index[dimension_dataframe[column] == value].tolist()[0]
                
                except IndexError:
                    target_index = dimension_dataframe.index[dimension_dataframe[column] == str(value)].tolist()[0]
                
                primary_key = f'{column}_id'
                foreign_key_value = dimension_dataframe.iloc[target_index][primary_key]
                facts_data[primary_key].append(foreign_key_value)
        
        print(f'Successfully initialized numeric and foreign key values for initializing facts table')
    
    # Display the values of every column in facts table for debugging purposes
    for column, value in facts_data.items():
        print(f'{column}: {value}')
        print()