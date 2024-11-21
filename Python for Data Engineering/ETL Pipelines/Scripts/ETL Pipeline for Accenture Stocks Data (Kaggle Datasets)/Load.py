# Load Job
def load(tranformed_stock_history_df, transformed_stock_info_df):
    transformed_stock_history_target_filepath = 'Target Data Files\\Accenture Stock Data\\transformed_stock_history.csv'
    transformed_stock_info_target_filepath  = 'Target Data Files\\Accenture Stock Data\\transformed_stock_info.csv'

    tranformed_stock_history_df.to_csv(transformed_stock_history_target_filepath, index=False)
    transformed_stock_info_df.to_csv(transformed_stock_info_target_filepath, index=False)
    
    return tranformed_stock_history_df, transformed_stock_info_df

