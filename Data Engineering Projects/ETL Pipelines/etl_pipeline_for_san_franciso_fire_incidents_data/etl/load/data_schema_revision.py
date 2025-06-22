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

def revise_schema(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Schema Revision Function
    '''
    columns = list(dataframe.keys())
    dimension_data, facts_data = [], {}

    # Initialize the structure of dimension data that consist of primary key and non-key attributes
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

    # Initialize the foreign key attributes of facts data
    for column in columns:
        if columns in return_the_list_of_columns_for_facts_data():
            continue
            
        if column == 'id':
            facts_data['id'] = []
        
        else:
            foreign_key = f'{column}_id'
            facts_data[foreign_key] = []

    # Initialize the numeric attributes of facts data
    for column in columns:
        if columns in return_the_list_of_columns_for_facts_data():
            facts_data[column] = []
    
    # Initialize the non-key attributes of every dimension data    
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        values = []

        for row_number in range(0, 705908 + 1, 1000):
            values.extend(list(dataframe[column][row_number : row_number + 1000]))

            print(f'Successfully extracted the values of column: {column} from {row_number}-{row_number + 999} rows for initialization of dimension data')

        values = list(set(values))

        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            dimension_data[i][column] = values
    
    for column in columns:
        if column in return_the_list_of_columns_for_facts_data():
            continue

        if column == 'id':
            continue

        for i in range(len(dimension_data)):
            if column not in dimension_data[i]:
                continue

            # TODO: Implement more functionalities here...