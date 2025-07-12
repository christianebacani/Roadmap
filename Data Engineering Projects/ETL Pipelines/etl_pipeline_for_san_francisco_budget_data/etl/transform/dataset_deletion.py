'''
    Dataset Deletion Module
'''
import os

def remove_unnecessary_datasets(total_number_of_datasets: int) -> None:
    '''
        Dataset Deletion Function
    '''
    # Perform dataset deletion
    for dataset_number in range(1, total_number_of_datasets + 1):
        filepath = f'data/staged/san_francisco_budget_data/san_francisco_budget_data({dataset_number}).csv'

        if os.path.exists(filepath):
            os.remove(filepath)
            print(f'Successfully removed san_francisco_budget_data({dataset_number}).csv staged dataset')