'''
    Logs Module
'''
import sys
sys.path.append('etl')
from datetime import datetime
from ingest.ingest import ingest_data_using_rest_api
from extract.extract import extract_raw_datasets
from transform.data_processing import processing_staged_datasets
from load.load import load_processed_datasets_to_postgresql_db

def log_progress(message: str) -> None:
    '''
        Log function to log all the progress
        from the Data Pipeline
    '''
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    logfile = 'etl/logs/logs.txt'

    with open(logfile, 'a') as f:
        f.write(f'{timestamp}: {message}\n')

log_progress('Initiating ETL Pipeline for San Francisco Police Department Crime Data. Initiating Ingestion Process')

# Ingestion Phase
ingest_data_using_rest_api('police_dept_inci_reports_2003_to_may_2018', 'https://data.sfgov.org/resource/tmnf-yvry.csv', 2129525)
ingest_data_using_rest_api('police_dept_inci_reports_2018_to_present', 'https://data.sfgov.org/resource/wg3w-h783.csv', 950318)
ingest_data_using_rest_api('summary_of_inci_reports', 'https://data.sfgov.org/resource/e3si-785i.csv', 677159)
log_progress('Ingestion Process Completed. Initiating Extraction Process')

# Extraction Phase
extract_raw_datasets('data/raw/police_dept_inci_reports_2003_to_may_2018')
extract_raw_datasets('data/raw/police_dept_inci_reports_2018_to_present')
extract_raw_datasets('data/raw/summary_of_inci_reports')
log_progress('Extraction Process Completed. Initiating Transformation Process')

# Transformation Phase
processing_staged_datasets('data/stage/police_dept_inci_reports_2003_to_may_2018')
processing_staged_datasets('data/stage/police_dept_inci_reports_2018_to_present')
processing_staged_datasets('data/stage/summary_of_inci_reports')
log_progress('Transformation Process Completed. Initiating PostgreSQL Database Connection')

# Loading Phase
log_progress('Initiating Loading Process')
load_processed_datasets_to_postgresql_db('data/processed/police_dept_inci_reports_2003_to_may_2018')
load_processed_datasets_to_postgresql_db('data/processed/police_dept_inci_reports_2018_to_present')
load_processed_datasets_to_postgresql_db('data/processed/summary_of_inci_reports')
log_progress('Loading Process Completed. PostgreSQL Database Connection Ended')