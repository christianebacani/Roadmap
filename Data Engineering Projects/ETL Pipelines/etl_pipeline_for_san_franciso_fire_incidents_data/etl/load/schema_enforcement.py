'''
    Data Schema Enforcement Module
'''
import pandas as pd

def return_the_list_of_facts_data() -> str:
    '''
        List of Facts Data Function
    '''
    return '''suppression_units
    suppression_personnel
    ems_units
    ems_personnel
    other_units
    other_personnel
    estimated_property_loss
    estimated_contents_loss
    fire_fatalities
    fire_injuries
    civilian_fatalities
    civilian_injuries
    number_of_alarms
    number_of_floors_with_minimum_damage
    number_of_floors_with_significant_damage
    number_of_floors_with_heavy_damage
    number_of_floors_with_extreme_damage
    number_of_sprinkler_heads_operating'''

def enforce_schema(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Schema Enforcement Function
    '''
    # Delete fields that are unnecessary before the schema enforcement process occur
    dataframe.drop(columns=['data_as_of', 'data_loaded_at'], inplace=True)

    # Get the list of facts data
    list_of_facts_data = return_the_list_of_facts_data().split('\n')

    for i in range(len(list_of_facts_data)):
        list_of_facts_data[i] = list_of_facts_data[i].strip()

    # Initialize a dictionary to store facts and dimensions data
    columns = list(dataframe.keys())
    facts_data = {}
    dimensions_data = []

    for column in columns:
        if column in list_of_facts_data:
            continue

        if column == 'id':
            facts_data['id'] = []
            dimensions_data.append({
                'id': []
            })
        
        else:
            foreign_key = column + '_id'
            facts_data[foreign_key] = []

            primary_key = foreign_key
            dimensions_data.append({
                primary_key: [],
                column: []
            })

    for column in columns:
        if columns in list_of_facts_data:
            facts_data[column] = []

    # Schema Enforcement Process
    for _, row in dataframe.iterrows():
        for column in columns:
            value = row.get(column)
            
            if column in list_of_facts_data:
               continue
            
            # Store the values of the dimensions data
            for i in range(len(dimensions_data)):
                if column in list(dimensions_data[i].keys()):
                    dimensions_data[i][column].append(value)