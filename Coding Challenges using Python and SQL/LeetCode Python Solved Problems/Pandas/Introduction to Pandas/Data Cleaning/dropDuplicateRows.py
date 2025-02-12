# 2882. Drop Duplicate Rows
# Category : Pandas

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset='email', keep='first', inplace=False)

    return customers