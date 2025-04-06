'''
    Transform Module
'''
import pandas as pd

def transform_extracted_data(extracted_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform extracted data
    '''
    transformed_data = {
        'title': [],
        'price_euros': [],
        'star_rating': [],
        'product_status': []
    }

    for _, row in extracted_dataframe.iterrows():
        star_rating_dict = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
    
        title = str(row.get('title')).strip()
        product_price = float(str(row.get('product_price')).replace('£', ''))
        star_rating = str(row.get('star_rating')).capitalize()
        star_rating = int(star_rating_dict[star_rating])
        product_availability = str(row.get('product_availability')).strip()
        
        transformed_data['title'].append(title)
        transformed_data['price_euros'].append(product_price)
        transformed_data['star_rating'].append(star_rating)
        transformed_data['product_status'].append(product_availability)
    
    transformed_dataframe = pd.DataFrame(transformed_data)

    processed_dataset_dir_path = 'data/processed'
    transformed_dataframe.to_csv(f'{processed_dataset_dir_path}/books.csv', index=False)
    
    return transformed_dataframe
