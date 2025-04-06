'''
    Load Module
'''
import pandas as pd
from sqlalchemy import create_engine

def load_transformed_data(transformed_dataframe: pd.DataFrame) -> object:
    '''
        Load function to load transformed dataframe
        to PostgreSQL Database Server based on it's existing
        data model
    '''
    dim_title = {
        'title_id': [],
        'title': []
    }
    dim_product_status = {
        'product_status_id': [],
        'product_status': []
    }
    fact_books = {
        'title_id': [],
        'product_status_id': [],
        'price_euros': [],
        'star_rating': []
    }

    for _, row in transformed_dataframe.iterrows():
        title = row.get('title')
        product_status = row.get('product_status')

        if title not in dim_title['title']:
            dim_title['title'].append(title)
            dim_title['title_id'].append(len(dim_title['title_id']) + 1)
    
        if product_status not in dim_product_status['product_status']:
            dim_product_status['product_status'].append(product_status)
            dim_product_status['product_status_id'].append(len(dim_product_status['product_status_id']) + 1)

    for _, row in transformed_dataframe.iterrows():
        title = str(row.get('title'))
        price_euros = float(row.get('price_euros'))
        star_rating = int(row.get('star_rating'))
        product_status = str(row.get('product_status'))

        titles = dim_title['title']
        product_statuses = dim_product_status['product_status']

        for i in range(len(titles)):
            if title == titles[i]:
                title_id = i + 1
                break
        
        for i in range(len(product_statuses)):
            if product_status == product_statuses[i]:
                product_status_id = i + 1
                break
        
        fact_books['title_id'].append(title_id)
        fact_books['product_status_id'].append(product_status_id)
        fact_books['price_euros'].append(price_euros)
        fact_books['star_rating'].append(star_rating)

    dim_title = pd.DataFrame(dim_title)
    dim_product_status = pd.DataFrame(dim_product_status)
    fact_books = pd.DataFrame(fact_books)
    
    username = '<YOUR_USERNAME>'
    password = '<YOUR_PASSWORD>'
    hostname = '<YOUR_HOSTNAME>'
    port = '<YOUR_PORT>'
    database = '<YOUR_DATABASE>'
    
    engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')
    
    dim_title.to_sql('dim_title', engine, if_exists='replace', index=False)
    dim_product_status.to_sql('dim_product_status', engine, if_exists='replace', index=False)
    fact_books.to_sql('fact_books', engine, if_exists='replace', index=False)

    return engine