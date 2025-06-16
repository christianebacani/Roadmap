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
    # Using .keys() method to get all the variable/field names
    columns = list(dataframe.keys())
    facts_data = {}
    dimensions_data = []
    
    for column in columns:
        if column == 'id':
            dimensions_data.append({
                f'dim_id': []
            })
            continue
        
        if column not in return_the_list_of_columns_for_facts_data():
            dimensions_data.append({
                f'{column}_id': [],
                f'dim_{column}': []
            })

    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        if column == 'id':
            facts_data['id'] = []
            continue

        facts_data[f'{column}_id'] = []
    
    for column in columns:
        if columns in return_the_list_of_columns_for_facts_data():
            facts_data[column] = []