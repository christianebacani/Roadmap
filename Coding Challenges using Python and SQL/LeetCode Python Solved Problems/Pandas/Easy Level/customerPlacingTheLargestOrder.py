# 586.) Customer Placing the Largest Number of Orders
# Categories : Pandas

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['customer_number'])
    customer_number_order_counts = {}


    for _, row in orders.iterrows():
        customer_number = row.get('customer_number')
        
        order_count = 0
        for _, inner_row in orders.iterrows():
            inner_row_customer_number = inner_row.get('customer_number')

            if (customer_number == inner_row_customer_number):
                order_count += 1
           
        customer_number_order_counts[customer_number] = order_count
    
    maximum_order_count = max(list(customer_number_order_counts.values()), default=0)

    for customer_number, order_count in customer_number_order_counts.items():
        if order_count == maximum_order_count:
            output_df = pd.concat([output_df, pd.DataFrame({'customer_number' : customer_number}, index=[0])], ignore_index=True)
    
    return output_df