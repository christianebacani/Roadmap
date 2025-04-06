'''
    Extract Module
'''
from glob import glob
import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_web_data() -> pd.DataFrame:
    '''
        Extract function to extract website data
        from bookstoscrape.com website
    '''    
    stage_datasets_dir_path = 'data/stage'

    if len(glob(f'{stage_datasets_dir_path}/*.csv')) > 0:
        books_dataframe = pd.read_csv(f'{stage_datasets_dir_path}/books.csv')
        return books_dataframe

    books_dict = {
        'title': [],
        'product_price': [],
        'star_rating': [],
        'product_availability': []
    }

    for i in range(1, 50 + 1):
        response = requests.get(url=f'https://books.toscrape.com/catalogue/page-{i}.html', timeout=250)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        ol_tags = soup.find_all('ol', attrs={'class': 'row'})
        li_tags = ol_tags[0].find_all('li', attrs={'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
        
        for j in range(len(li_tags)):
            product_pod = li_tags[j].find('article', attrs={'class': 'product_pod'})
            
            books_dict['title'].append(product_pod.find('h3').find('a').attrs['title'])
            books_dict['product_price'].append(str(product_pod.find('div', attrs={'class': 'product_price'}).find('p', attrs={'class': 'price_color'}).text).replace('Â', ''))
            books_dict['star_rating'].append(product_pod.find('p').attrs['class'][1])
            books_dict['product_availability'].append(str(product_pod.find('div', attrs={'class': 'product_price'}).find('p', attrs={'class': 'instock availability'}).text).strip())
    
    books_dataframe = pd.DataFrame(books_dict)
    books_dataframe.to_csv(f'{stage_datasets_dir_path}/books.csv', index=False)
    
    return books_dataframe

        
