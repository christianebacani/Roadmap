from datetime import datetime
import pandas as pd 
import glob


# Extraction Job
def extract():
    def extract_from_csv(csvfile):
        df = pd.read_csv(csvfile)
        return df 

    accenture_stock_history_source_filepath = 'Accenture Stock Prices\\Accenture_stock_history.csv'
    accenture_stock_info_source_filepath = 'Accenture Stock Prices\\Accenture_stock_info.csv'
    
    # Dataframe to store the extracted data from csv files
    stock_history_df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'])
    stock_info_df = pd.DataFrame(columns=['zip', '2'])


    # Extract Accenture Stock History CSV File
    for stock_history_csv in glob.glob(accenture_stock_history_source_filepath):
        stock_history_df = pd.concat([stock_history_df, extract_from_csv(stock_history_csv)], ignore_index=True)
    
    # Extract Accenture Stock Info CSV File
    for stock_info_csv in glob.glob(accenture_stock_info_source_filepath):
        stock_info_df = pd.concat([stock_info_df, extract_from_csv(stock_info_csv)], ignore_index=True)
    
    return stock_history_df, stock_info_df






