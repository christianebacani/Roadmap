'''
    Logs Module
'''
import sys
sys.path.append('etl')
from datetime import datetime
from ingest.ingest import ingest_data_using_api
from extract.extract import extract_ingested_data
from transform.data_processing import processing_staged_datasets

def log_progress(message: str) -> None:
    '''
        Log function to record a log
        for different ETL Pipeline Phases
    '''
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    # Logs entire process to a text file
    logfile = 'etl/logs/logs.txt'

    with open(logfile, 'a') as f:
        f.write(f'{timestamp}: {message}\n')
    
    f.close()

log_progress('Initiating ETL Pipeline for Processing Registered/Active Business Locations from San Francisco USA')

# Ingestion Phase
log_progress('Initiating Ingestion Phase')
ingest_data_using_api('registered_business_locs_in_san_francisco', 'https://data.sfgov.org/resource/g8m3-pdis.csv', 340940)
ingest_data_using_api('active_business_locs_in_san_francisco', 'https://data.sfgov.org/resource/kvj8-g7jh.csv', 125996)
log_progress('Ingestion Phase Ended')

# Extraction Phase
log_progress('Initiating Extraction Phase')
extract_ingested_data('data/raw/active_business_locs_in_san_francisco')
extract_ingested_data('data/raw/registered_business_locs_in_san_francisco')
log_progress('Extraction Phase Ended')

# Transformation Phase
log_progress('Initiating Transformation Phase')
processing_staged_datasets('data/stage/active_business_locs_in_san_francisco')
log_progress('Transformation Phase Ended')