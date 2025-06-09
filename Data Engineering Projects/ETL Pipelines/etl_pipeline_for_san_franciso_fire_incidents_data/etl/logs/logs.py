'''
    Data Pipeline Logs Module
'''
import sys
sys.path.append('etl')
from datetime import datetime
from ingest.ingest import ingest_raw_data
from extract.extract import extract_ingested_data
from transform.data_processing import processing_extracted_data
from data_integration.data_integration import integrate_processed_datasets
from data_schema_enforcement.data_schema_enforcement import enforce_data_schema

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
log_messages('Extraction/Staging Phase Ended')

# Transformation Phase
log_messages('Initiating Transformation Phase')
processing_extracted_data('data/stage/san_francisco_fire_incidents_data')
log_messages('Transformation Phase Ended')

# Data Integration Phase
log_messages('Initiating Data Integration Phase')
integrate_processed_datasets()
log_messages('Data Integration Phase Ended')

# Data Schema Enforcement Phase
log_messages('Initiating Data Schema Enforcement Phase')
enforce_data_schema()
log_messages('Data Schema Enforcement Phase Ended')

log_messages('ETL Pipeline for San Francisco Fire Incidents Data Ended')