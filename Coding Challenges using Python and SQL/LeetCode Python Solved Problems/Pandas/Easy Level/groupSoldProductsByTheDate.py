# 1484.) Group Sold Products by The Date
# Categories : Pandas

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['sell_date', 'num_sold', 'products'])
    sell_dates = list(set(activities['sell_date']))
    output_dict = {}
    
    for sell_date in sell_dates:
        output_dict[sell_date] = []
        
        for _, inner_row in activities.iterrows():
            inner_row_sell_date = inner_row.get('sell_date')
            inner_row_product = inner_row.get('product')

            if (sell_date == inner_row_sell_date) and (inner_row_product not in output_dict[sell_date]):
                output_dict[sell_date].append(inner_row_product)
        
        nums_sold = len(output_dict[sell_date])
        sorted_products_sold = sorted(output_dict[sell_date])
        sorted_products_sold = ','.join(sorted_products_sold)

        output_df = pd.concat([output_df, pd.DataFrame({'sell_date' : sell_date, 'num_sold' : nums_sold, 'products' : sorted_products_sold}, index=[0])], ignore_index=True)
    
    output_df.sort_values(by=['sell_date'], ascending=[True], inplace=True)

    return output_df