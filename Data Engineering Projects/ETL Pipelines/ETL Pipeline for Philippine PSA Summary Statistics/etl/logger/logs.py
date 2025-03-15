'''
    Logs the entire process of ETL Pipeline
'''
import sys
sys.path.append('etl')
from datetime import datetime
from extract.extract_raw_data import extract
from transform.process_staged_datasets import process
from load.load_processed_datasets import load
from run_queries.run_queries import queries

def log_progress(message: str) -> None:
    '''
        Log function for the entire processes/jobs
        of ETL Pipeline 
    '''
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open('etl_pipeline_logs.txt', 'a', encoding='utf-8') as f:
        f.write(f'{timestamp} : {message}\n')

log_progress('Initiating etl pipeline process. Initiating extraction process')

# Extract
raw_datasets_directory = 'ETL Pipeline for Philippine PSA Summary Statistics/data/raw'
extract(raw_datasets_directory)
log_progress('Extraction process completed. Initiating transformation process')

# Transform
stage_datasets_directory = 'ETL Pipeline for Philippine PSA Summary Statistics/data/stage'
process(stage_datasets_directory)
log_progress('Transformation process completed. Initiating loading process')

# Load
processed_directory = 'ETL Pipeline for Philippine PSA Summary Statistics/data/processed'
load(processed_directory)
log_progress('Loading process completed. Running queries')

# Run queries
queries()
log_progress('Running queries completed. Database connection closed')
