'''
    Data Schema Enforcement Module
'''
import pandas as pd

def return_the_list_of_facts_data_columns() -> str:
    '''
        Returning the list of facts data function
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

def enforce_data_schema() -> None:
    '''
        Data Schema Enforcement Function
    '''
    # Initialize a directory path to store structured datasets after schema enforcement
    target_directory_path = 'data/structured_datasets'

    list_of_facts_data_columns = return_the_list_of_facts_data_columns().split('\n')

    for index, facts_data_column in enumerate(list_of_facts_data_columns):
        list_of_facts_data_columns[index] = facts_data_column.strip()
    
    filepath = 'data/integrated_datasets/san_francisco_fire_incidents_integrated_data.csv'
    dataframe = pd.read_csv(filepath, low_memory=False) # Set low memory to false because some variables/fields contains mixed data type/s
    columns = list(dataframe.keys())

    # Mapped the values of the dimension data to the corresponding dimension dataset
    for column in columns:
        if column in list_of_facts_data_columns:
            continue
            
        dimension_dataframe = pd.DataFrame({f'dim_{column}': []})
        dimension_data = {f'dim_{column}': []}

        for row_number in range(0, 705909, 1000):
            values = list(dataframe[column][row_number : row_number + 1000])
            dimension_data[f'dim_{column}'].extend(values)

            print(f'Successfully mapped {row_number}-{(row_number + 999)} rows from dim_{column} to dimension dataframe')
        
        dimension_data[f'dim_{column}'] = list(set(dimension_data[f'dim_{column}']))
        dimension_data = pd.DataFrame(dimension_data)
        
        dimension_dataframe = pd.concat([dimension_dataframe, dimension_data], ignore_index=True)
        target_filepath = f'{target_directory_path}/dim_{column}.csv'
        dimension_dataframe.to_csv(target_filepath, index=False)