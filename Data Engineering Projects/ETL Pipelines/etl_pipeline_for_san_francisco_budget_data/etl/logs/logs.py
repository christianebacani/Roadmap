'''
    Log Module
'''
import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath('etl'))
from datetime import datetime
from ingest.ingest import ingest_raw_data
from extract.extract import extract_ingested_datasets
from transform.transform import transform_extracted_datasets
from load.data_schema_revision import revise_schema

def log_progress(message: str) -> None:
    '''
        Log function
    '''
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('etl/logs/logs.txt', 'a') as f:
        f.write(f'[{timestamp}]: {message}\n')
        
    f.close()

if __name__ == '__main__':
    log_progress('Initiating ETL Pipeline for San Francisco Budget Data')
    
    # Ingestion Phase
    log_progress('Initiating Ingestion Phase')
    ingest_raw_data('https://data.sfgov.org/resource/xdgd-c79v.csv', 360531)
    log_progress('Ingestion Phase Ended')

    # Extraction Phase
    log_progress('Initiating Extraction Phase')
    extract_ingested_datasets('data/raw/san_francisco_budget_data')
    log_progress('Extraction Phase Ended')

    # Transformation Phase
    log_progress('Initiating Transformation Phase')
    transform_extracted_datasets('data/staged/san_francisco_budget_data')
    log_progress('Transformation Phase Ended')
    
    # Loading Phase
    log_progress('Initiating Loading Phase')
    revise_schema(pd.read_csv('data/processed/san_francisco_budget_data/san_francisco_integrated_budget_data.csv'))
    log_progress('Loading Phase Ended')