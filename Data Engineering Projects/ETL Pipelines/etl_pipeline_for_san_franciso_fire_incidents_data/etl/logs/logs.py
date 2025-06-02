'''
    Data Pipeline Logs Module
'''
import sys
sys.path.append('etl')
from datetime import datetime
from ingest.ingest import ingest_raw_data
from extract.extract import extract_ingested_data
from transform.data_processing import processing_extracted_data

def log_messages(message: str) -> None:
    '''
        Log message function
    '''
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(format)
    
    with open('etl/logs/logs.txt', 'a') as f:
        f.write(f'{timestamp}: {message}\n')
    
    f.close()

# Execution of the Pipeline
log_messages('Initiating ETL Pipeline for San Francisco Fire Incidents Data')

# Ingestion Phase
log_messages('Initiating Ingestion Phase')
ingest_raw_data("https://data.sfgov.org/resource/wr8u-xric.csv", 705908)
log_messages('Ingestion Phase Ended')

# Extraction/Staging Phase
log_messages('Initiating Extraction/Staging Phase')
extract_ingested_data('data/raw/san_francisco_fire_incidents_data')
log_messages('Extraction/Staging Phase')

# Transformation Phase
log_messages('Initiating Transformation Phase')
processing_extracted_data('data/stage/san_francisco_fire_incidents_data')
log_messages('Transformation Phase Ended')

log_messages('ETL Pipeline for San Francisco Fire Incidents Data Ended')