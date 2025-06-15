'''
    Data Format Revision Module
'''
import pandas as pd

def return_the_list_of_columns_that_has_code_and_message_value_pattern() -> str:
    '''
        Return function to return the list of columns
        that has a code and message value pattern
    '''
    return [
        'primary_situation',
        'action_taken_primary',
        'action_taken_secondary',
        'action_taken_other',
        'detector_alerted_occupants',
        'property_use',
        'area_of_fire_origin',
        'ignition_cause',
        'ignition_factor_primary',
        'ignition_factor_secondary',
        'heat_source',
        'item_first_ignited',
        'human_factors_associated_with_ignition',
        'structure_type',
        'structure_status',
        'fire_spread',
        'detectors_present',
        'detector_type',
        'detector_operation',
        'detector_effectiveness',
        'detector_failure_reason',
        'automatic_extinguishing_system_present',
        'automatic_extinguishing_sytem_type',
        'automatic_extinguishing_sytem_perfomance'
    ]

def revise_format(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Data Format Revision Function
    '''
    # Using .keys() method to get all the variable/field names
    columns = list(dataframe.keys())
    
    for index, row in dataframe.iterrows():
        for column in columns:
            value = row.get(column)

            if column in ['incident_date', 'data_as_of', 'data_loaded_at'] or 'dttm' in column:
                continue

            if isinstance(value, (int, float)):
                continue
            
            # Revising the format of the values by checking the variable/field name
            if column == 'address':
                value = str(value).split()
                
                for i in range(len(value)):
                    value[i] = value[i].capitalize()
                
                value = ' '.join(value)

                street_abbreviations = {
                    'ST': 'Street',
                    'AW': 'Avenue',
                    'BL': 'Block',
                    'HW': 'Hi-way'
                }

                for abbreviation, street_name in street_abbreviations.items():
                    value = value.replace(abbreviation, street_name)
                
                dataframe.at[index, 'address'] = value

            elif column in return_the_list_of_columns_that_has_code_and_message_value_pattern():
                value = str(value).replace('-', ' ')
                value = ' '.join(value.split())
                dataframe.at[index, column] = value

            elif column == 'no_flame_spread':
                dataframe.at[index, 'no_flame_spread'] = str(value).capitalize()

            elif column == 'neighborhood_district':
                value = str(value).replace('/', ', ')
                dataframe.at[index, 'neighborhood_district'] = value

            elif column == 'point':
                value = str(value)
                value = value.replace('POINT (', '')
                value = value.replace(')', '')
                value = ', '.join(value.split())
                dataframe.at[index, 'point'] = value

            else:
                pass
    
    return dataframe