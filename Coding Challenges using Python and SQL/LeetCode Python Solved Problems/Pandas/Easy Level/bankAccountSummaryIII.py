# 1587.) Bank Account Summary III
# Categories : Pandas

import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['name', 'balance'])

    for _, row in users.iterrows():
        account = row.get('account')
        name = row.get('name')
        total_amount = 0
        
        for _, inner_row in transactions.iterrows():
            inner_row_account = inner_row.get('account')
            inner_row_amount = int(inner_row.get('amount'))

            if (account == inner_row_account):
                total_amount += inner_row_amount
    
        if total_amount > 10000:
            output_df = pd.concat([output_df, pd.DataFrame({'name' : name, 'balance' : total_amount}, index=[0])], ignore_index=True)        
    
    return output_df
