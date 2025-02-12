# 2887.) Fill Missing Data
# Category : Pandas

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products[['quantity']] = products[['quantity']].fillna(0)

    return products