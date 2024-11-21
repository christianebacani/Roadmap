import pandas as pd
import re 


# Transform Job
def transform(stock_history_df, stock_info_df):
    transformed_stock_history_df= pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'])
    stock_info_columns = []
    stock_info = {}
    transformed_stock_info = {}


    # Transforming rows for stock_history dataframe
    for _, row in stock_history_df.iterrows():
        date = row.get('Date')
        open = round(float(row.get('Open')), 1)
        high = round(float(row.get('High')), 1)
        low = round(float(row.get('Low')), 1)
        close = round(float(row.get('Close')), 1)
        volume = round(float(row.get('Volume')), 1)
        dividends = round(float(row.get('Dividends')), 1)
        stock_splits = round(float(row.get('Stock Splits')), 1)
        
        parsed_df = pd.DataFrame({'Date' : date, 'Open' : open, 'High' : high, 'Low' : low, 'Close' : close, 'Volume' : volume, 'Dividends' : dividends, 'Stock Splits' : stock_splits}, index=[0])

        transformed_stock_history_df = pd.concat([transformed_stock_history_df, parsed_df], ignore_index=True)
        
    
    # Pivoting stock_info_df
    for _, row in stock_info_df.iterrows():
        zip = row.get('zip')
        stock_info_columns.append(zip)

        two = row.get('2')
        stock_info[zip] = two
    
    pivoted_stock_info_df = pd.DataFrame(stock_info, index=[0])


    # Cleaning values for pivoted_stock_info dataframe
    for column in stock_info_columns:
        pivoted_stock_info_df[f'{column}'] = pivoted_stock_info_df[f'{column}'].fillna('No Data')
        pivoted_stock_info_df[f'{column}'] = pivoted_stock_info_df[f'{column}'].replace('none', 'No Data')
        pivoted_stock_info_df[f'{column}'] = pivoted_stock_info_df[f'{column}'].replace('[]', 'No Data')
    

    # Transform values of pivoted_stock_info dataframe
    for column in stock_info_columns:
        for _, row in pivoted_stock_info_df.iterrows():
            stock_info_row = str(row.get(column))

            contains_decimal_values = re.search(r'^\-?[0-9]+[\.]+[0-9]+$', stock_info_row) or re.search(r'^[0-9]+[\.]+[0-9]+$', stock_info_row)
            contains_int_values = re.search(r'^[0-9]+$', stock_info_row)
            
            if contains_decimal_values:
                stock_info_row = float(f'{float(stock_info_row):.1f}')

            elif contains_int_values:
                stock_info_row = float(f'{float(stock_info_row):.1f}')

            transformed_stock_info[column] = stock_info_row
            break
            
    transformed_stock_info_df = pd.DataFrame(transformed_stock_info, index=[0])

    return transformed_stock_history_df, transformed_stock_info_df

