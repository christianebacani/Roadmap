# 183.) Customers Who Never Order
# Categories : Pandas

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customerWhoNeverOrder = pd.DataFrame(columns=['name'])
    customerWhoOrders = []

    for _, row in orders.iterrows():
        customerWhoOrders.append(row.get('customerId'))
    
    for _, row in customers.iterrows():
        id = row.get('id')
        
        if id not in customerWhoOrders:
            customerWhoNeverOrder = pd.concat([customerWhoNeverOrder, pd.DataFrame({'name' : [row.get('name')]})], ignore_index=True)
    
    customerWhoNeverOrder.rename(columns={'name' : 'Customers'}, inplace=True)

    return customerWhoNeverOrder