'''
    Remove Datasets Module
'''
import os
def remove_partitioned_and_integrated_datasets(subdirectory_path: str) -> None:
    '''
        Remove Datasets Function
    '''
    for dataset_number in range(1, 706 + 1):
        filepath = f'{subdirectory_path}/san_francisco_fire_incidents_data({dataset_number}).csv'
        
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f'Successfully removed san_francisco_fire_incidents_data({dataset_number}).csv partitioned dataset')
    
    if os.path.exists('data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_integrated_data.csv'):
        os.remove('data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_integrated_data.csv')
        print('Successfully remove san_francisco_fire_incidents_integrated_data.csv')