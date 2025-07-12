'''
    Data Integration Module
'''
import pandas as pd

def integrate_datasets(total_number_of_datasets: int) -> None:
    '''
        Data Integration Function
    '''
    # Perform data integration 
    integrated_dataframe = pd.read_csv('data/staged/san_francisco_budget_data/san_francisco_budget_data(1).csv')

    for dataset_number in range(2, total_number_of_datasets + 1):
        filepath = f'data/staged/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'
        integrated_dataframe = pd.concat([integrated_dataframe, pd.read_csv(filepath)], ignore_index=True)

        print(f'Successfully integrate san_francisco_budget_data({dataset_number}).csv')
    
    target_filepath = f'data/staged/san_francisco_budget_data/san_francisco_integrated_budget_data.csv'
    integrated_dataframe.to_csv(target_filepath, index=False)
    print(f'Successfully perform data integration')