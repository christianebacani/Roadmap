import Extract
import Transform
import Load 
from datetime import datetime


# Logs
def logs(message):

    timestamp_format = '%Y:%m%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    logfile = 'logfile.txt'
    
    with open(logfile, 'a') as f:
        f.write(f"{timestamp} : {message}\n")


logs('(PROD) : ETL Pipeline Started')


# Extract Phase
logs('(PROD) : Extract Phase Started')
extracted_stock_history_df, extracted_stock_info_df = Extract.extract()
print("Extracted Data:")
print(extracted_stock_history_df, extracted_stock_info_df)


# Transform Phase
logs('(PROD) : Transforming Phase Started')
transformed_stock_history_df, transformed_stock_info_df = Transform.transform(extracted_stock_history_df, extracted_stock_info_df)
print("\nTransformed Data:")
print(transformed_stock_history_df, transformed_stock_info_df)

# Load Phase
logs('(PROD) : Load Phase Started')
loaded_transformed_stock_history_df, loaded_transformed_stock_info_df = Load.load(transformed_stock_history_df, transformed_stock_info_df)
logs('(PROD) : Load Phase Ended')
print("\nLoaded Phase:")
print(loaded_transformed_stock_history_df, loaded_transformed_stock_info_df)


logs('(PROD) : ETL Pipeline Ended')