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
    
    subdirectory_path = 'data/processed/san_francisco_fire_incidents_data'

    # Partitioned the integrated processed dataset for faster processing time
    for dataset_number, row_number in enumerate(range(0, 705909, 1000)):
        dataset_number += 1
        
        target_filepath = f'{subdirectory_path}/san_francisco_fire_incidents_data({dataset_number}).csv'
        partitioned_dataframe = dataframe[row_number : row_number + 1000]
        partitioned_dataframe.to_csv(target_filepath, index=False)

        print(f'Successfully partitioned integrated processed dataset of {row_number}-{row_number + 999} rows')
    
    # Remove integrated processed dataset after partitioning
    if os.path.exists(f'{subdirectory_path}/san_francisco_fire_incidents_processed_data.csv'):
        os.remove(f'{subdirectory_path}/san_francisco_fire_incidents_processed_data.csv')
    
    # Initialize a dictionary and array to store the values of facts and dimension data
    facts_data, dimension_data = {}, []

    columns = list(dataframe.keys())

    # Initialize primary key and non-key attributes of dimension data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        if column == 'id':
            dimension_data.append({
                'id': []
            })
        
        else:
            primary_key = f'{column}_id'
            dimension_data.append(({
                primary_key: [],
                column: [] 
            }))

    # Initialize foreign keys of facts data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue
        
        if column == 'id':
            facts_data['id'] = []
        
        else:
            foreign_key = f'{column}_id'
            facts_data[foreign_key] = []

    # Initialize the numeric values of facts data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            facts_data[column] = []

    # Initialization of the non-key attributes of the dimension data    
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue
        
        values = []

        for dataset_number in range(1, 706 + 1):
            filepath = f'{subdirectory_path}/san_francisco_fire_incidents_data({dataset_number}).csv'
            partitioned_dataframe = pd.read_csv(filepath)

            values.extend(list(partitioned_dataframe[column]))
            
            print(f'Sucessfully extracted the values of column: {column} from san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset for initialization of dimension data')
        
        values = list(set(values))

        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            dimension_data[i][column] = values

    # Initialization of the key attributes of the dimension data    
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
                
                print(f'Successfully initialized the primary key value: {primary_key_value} column: {column} for the initialization of dimension data')
            
            primary_key = f'{column}_id'
            dimension_data[i][primary_key] = primary_key_values

    # Initialize the dimension data dictionary as a dataframe    
    for i in range(len(dimension_data)):
        filepath = f'{subdirectory_path}/dim_{column}.csv'
        dimension_dataframe = pd.DataFrame(dimension_data[i])
        dimension_dataframe.to_csv(filepath, index=False)

        print(f'Sucessfully initialize dim_{column} dimension dataset')
    
    # Initialize the foreign key attributes and numeric values of facts data
    for dataset_number in range(1, 706 + 1):
        filepath = f'{subdirectory_path}/san_francisco_fire_incidents_data({dataset_number}).csv'
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
                    dimension_dataframe = pd.read_csv(f'{subdirectory_path}/dim_{column}.csv')
                    target_index = dimension_dataframe.index[dimension_dataframe[column] == value].to_list()[0]

                    primary_key = f'{column}_id'
                    foreign_key_value = dimension_dataframe.iloc[target_index][primary_key]

                    foreign_key = primary_key
                    facts_data[foreign_key].append(foreign_key_value)
        
        print(f'Successfully initialized the values of facts data from san_francisco_fire_incidents_data({dataset_number}).csv')
    
    # Initialize facts data dictionary as a dataframe
    target_filepath = f'{subdirectory_path}/facts_san_francisco_fire_incidents.csv'
    facts_dataframe = pd.DataFrame(facts_data)
    facts_dataframe.to_csv(target_filepath, index=False)

    print('Successfully initialize facts_san_francisco_fire_incidents facts dataset')

    # Remove the partitioned datasets after the schema revision process
    for dataset_number in range(1, 706 + 1):    
        filepath = f'{subdirectory_path}/san_francisco_fire_incidents({dataset_number}).csv'

        if os.path.exists(filepath):
            os.remove(filepath)

            print(f'Successfully removed san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset')