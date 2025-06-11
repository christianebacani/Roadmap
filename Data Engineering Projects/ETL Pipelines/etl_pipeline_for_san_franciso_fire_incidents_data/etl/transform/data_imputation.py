'''
    Data Imputation Module
'''
import pandas as pd

def return_the_list_of_columns_that_impute_mean_values() -> str:
    '''
        List of columns that impute mean values Function
    '''
    # TODO : Get the columns that impute mean values
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
    number_of_floors_with_extreme_damage'''

def impute_values_from_the_staged_dataset(staged_dataframe: pd.DataFrame) -> None:
    '''
        Data Imputation Function
    '''
    # Get the list of columns that impute mean values for numerical data
    list_of_columns_that_impute_mean_values = return_the_list_of_columns_that_impute_mean_values().split('\n')

    for i in range(len(list_of_columns_that_impute_mean_values)):
        list_of_columns_that_impute_mean_values[i] = list_of_columns_that_impute_mean_values[i].strip()
    
    columns = list(staged_dataframe.keys())
    
    # Data imputation process by using dataframe and group of row-based extraction to optimize the data parsing
    for column in columns:
        data = {column: []}

        for row_number in range(0, 705909, 1000):
            data[column].extend(list(staged_dataframe[column][row_number : row_number + 1000]))
            print(f'Extracting data of column: {column} from {row_number}-{row_number + 1000} rows for data imputation')

        # Convert to dataframe and storing dataframe to the staging directory path as a csv file (It consumes more processing time if we use mean(). median(), or mode() right away)
        dataframe = pd.DataFrame(data)
        target_filepath = f'data/stage/san_francisco_fire_incidents_data/{column}_data.csv'
        dataframe.to_csv(target_filepath, index=False)
    
    # Initializing a dictionary to store the imputed values per column name
    imputed_values = {}