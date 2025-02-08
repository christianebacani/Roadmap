# 1757.) Recyclable and Low Fat Products
# Category : Pandas

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    recyclableAndLowFatProducts = pd.DataFrame(columns=['product_id'])
    
    for _, row in products.iterrows():
        lowFats = row.get('low_fats')
        recyclable = row.get('recyclable')
        
        if lowFats == 'Y' and recyclable == 'Y':
            recyclableAndLowFatProducts = pd.concat([recyclableAndLowFatProducts, pd.DataFrame({'product_id' : [row.get('product_id')]})], ignore_index=True)
    
    return recyclableAndLowFatProducts