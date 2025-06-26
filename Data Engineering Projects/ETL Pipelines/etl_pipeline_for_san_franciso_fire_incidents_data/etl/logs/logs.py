'''
    Data Pipeline Logs Module
'''
import sys
sys.path.append('etl')
import pandas as pd
from datetime import datetime
from ingest.ingest import ingest_raw_data
from extract.extract import extract_ingested_data
from transform.data_transformation import transform_staged_dataset
from load.data_schema_revision import revise_schema
from load.load import load_to_postgresql_db
from sql_query.sql_query import query

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

# Extraction Phase
log_messages('Initiating Extraction Phase')
extract_ingested_data('data/raw/san_francisco_fire_incidents_data')
log_messages('Extraction Phase Ended')

# Transformation Phase
log_messages('Initiating Transformation Phase')
transform_staged_dataset(pd.read_csv('data/stage/san_francisco_fire_incidents_data/san_francisco_fire_incidents_integrated_data.csv', low_memory=False))
log_messages('Transformation Phase Ended')

# Loading Phase
log_messages('Initiating Loading Phase')
revise_schema(pd.read_csv('data/processed/san_francisco_fire_incidents_data/san_francisco_fire_incidents_processed_data.csv', low_memory=False))
load_to_postgresql_db('data/processed/san_francisco_fire_incidents_data')
log_messages('Loading Phase Ended')

# SQL Query
log_messages('Initiating SQL Query Phase')
query('SELECT * FROM facts_fire_incidents_data')
query('SELECT * FROM dim_incident_number')
query('SELECT * FROM dim_id')
log_messages('SQL Query Phase Ended')

log_messages('ETL Pipeline for San Francisco Fire Incidents Data Ended')