'''
    Logs Module
'''
import sys
sys.path.append('etl')

from datetime import datetime
from extract.extract import extract_web_data
from transform.transform import transform_extracted_data
from load.load import load_transformed_data
from run_query.run_query import run_sql_query

def log_progress(message: str) -> None:
    '''
        Log function to log the entire 
        processes/jobs of the pipeline
    '''
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    logfile = 'etl/logger/logs.txt'
    
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(f'{timestamp}: {message}\n')

log_progress('Initiating ETL Pipeline. Initiating extraction process')

extracted_dataframe = extract_web_data()
log_progress('Extraction process completed. Initiating transformation process')

transformed_dataframe = transform_extracted_data(extracted_dataframe)
log_progress('Transformation process completed. Initiating loading process and Initiating PostgreSQL Server Connection')

engine = load_transformed_data(transformed_dataframe)
log_progress('Loading process completed. Running SQL Query')

query = run_sql_query(engine)
print(query)
log_progress('PostgreSQL Server Connection Removed')





