# 1795.) Rearrange Products Table
# Categorries : Pandas

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    arranged_products = pd.melt(products, id_vars='product_id', value_vars=['store1', 'store2', 'store3'], var_name='store', value_name='price')
    arranged_products.dropna(subset='price', inplace=True)

    return arranged_products
