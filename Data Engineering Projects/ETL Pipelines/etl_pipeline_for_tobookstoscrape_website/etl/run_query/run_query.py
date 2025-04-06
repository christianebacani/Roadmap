'''
    Run query module
'''
import pandas as pd

def run_sql_query(engine: object) -> pd.DataFrame:
    '''
        Run query function to run sql query using
        sqlalchemy engine
    '''
    df = pd.read_sql('SELECT dim_title.title, dim_product_status.product_status, fact_books.price_euros, fact_books.star_rating FROM fact_books INNER JOIN dim_title ON fact_books.title_id = dim_title.title_id INNER JOIN dim_product_status ON fact_books.product_status_id = dim_product_status.product_status_id', engine)
    
    return df