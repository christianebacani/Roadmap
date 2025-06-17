'''
    Data Schema Revision Module
'''
import pandas as pd

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

    # Initialize the dimensions data    
    for column in columns:
        if column == 'id':
            dimensions_data.append({
                'dim_id': []
            })
            continue
        
        if column not in return_the_list_of_columns_for_facts_data():
            dimensions_data.append({
                f'{column}_id': [],
                f'dim_{column}': []
            })

    # Get the foreign key of every keys of dimensions data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        if column == 'id':
            facts_data['id'] = []
            continue

        facts_data[f'{column}_id'] = []
    
    # Initialize the facts data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            facts_data[column] = []

    # Extracting the values of dimensions data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue
        
        values = []

        for row_number in range(0, 705909, 1000):
            values.extend(list(dataframe[column][row_number : row_number + 1000]))
            print(f'Successfully extracted the values that consist {row_number}-{row_number + 1000} rows from {column} column for data schema revision process')

        values = list(set(values))

        for i in range(len(dimensions_data)):
            if f'dim_{column}' in dimensions_data[i]:
                dimensions_data[i][f'dim_{column}'] = values

    # Initializing primary key values of every dimension data
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue
        
        if column == 'id':
            continue

        for i in range(len(dimensions_data)):
            if f'dim_{column}' not in dimensions_data[i]:
                continue

            total_number_of_primary_key_values = len(dimensions_data[i][f'dim_{column}'])
            primary_key_values = []

            for primary_key_value in range(1, total_number_of_primary_key_values + 1):
                primary_key_values.append(primary_key_value)
                print(f'Successfully initializes a primary key value: {primary_key_value} from dim_{column} column of dimension data for data schema revision process')

            dimensions_data[i][f'{column}_id'] = primary_key_values

    target_subdirectory_path = 'data/processed/san_francisco_fire_incidents_data'

    # Stage the dimensions data as a dataframe
    # NOTE: For debugging purposes only

    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        for i in range(len(dimensions_data)):
            if f'dim_{column}' not in dimensions_data[i]:
                continue
            
            target_filepath = f'{target_subdirectory_path}/dim_{column}.csv'
            dimension_dataframe = pd.DataFrame(dimensions_data[i])
            dimension_dataframe.to_csv(target_filepath, index=False)

            print(f'Successfully staged dim_{column}.csv dimension dataset for debugging purposes')