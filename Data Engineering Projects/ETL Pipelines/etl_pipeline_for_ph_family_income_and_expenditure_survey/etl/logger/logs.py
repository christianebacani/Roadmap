'''
    Log Module
'''
import sys
sys.path.append('etl')
from datetime import datetime
from extract.extract import extract_raw_datasets
from transform.data_processing import processing_staged_datasets
from load.load import load_processed_datasets_to_postgresql_db
from test_sql_query.test_sql_query import run_sql_query

def log_progress(message: str) -> None:
    '''
        Log function to log the
        entire process/jobs throughout
        the ETL Pipeline
    '''
    timestamp_format = '%Y-%m-%d'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    
    logfile = 'etl/logger/logs.txt'
    
    with open(logfile, 'a') as f:
        f.write(f'{timestamp}: {message}\n')
    
    f.close()

log_progress('Initiating ETL Pipeline. Initiating extraction process')

raw_datasets_directory_path = 'data/raw'
extract_raw_datasets(raw_datasets_directory_path)
log_progress('Extraction process completed. Initiating transformation process')

stage_datasets_directory_path = 'data/stage'
processing_staged_datasets(stage_datasets_directory_path)
log_progress('Transformation process completed. Initiating loading process')

log_progress('Initiating PostgreSQL Database Server Connection')
processed_datasets_directory_path = 'data/processed'
load_processed_datasets_to_postgresql_db(processed_datasets_directory_path)
log_progress('Starting PostgreSQL Query from PostgreSQL Database Server')

run_sql_query()
log_progress('PostgreSQL Database Server Connection Removed')


