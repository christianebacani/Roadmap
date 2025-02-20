# 1393.) Capital Gain/Loss
# Categories : Pandas

import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['stock_name', 'capital_gain_loss'])
    distinct_stock_names = list(set(stocks['stock_name']))
    
    for distinct_stock_name in distinct_stock_names:
        total_buy_price = 0
        total_sell_price = 0

        for _, row in stocks.iterrows():
            stock_name = row.get('stock_name')
            operation = row.get('operation')
            price = row.get('price')
            
            if (distinct_stock_name == stock_name) and (operation == 'Buy'):
                total_buy_price += price
            
            elif (distinct_stock_name == stock_name) and (operation == 'Sell'):
                total_sell_price += price
        
        capital_gain_loss = total_sell_price - total_buy_price
        output_df = pd.concat([output_df, pd.DataFrame({'stock_name' : distinct_stock_name, 'capital_gain_loss' : capital_gain_loss}, index=[0])], ignore_index=True)
    
    return output_df
