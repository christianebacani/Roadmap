'''
    Data Pipeline Logs Module
'''
from datetime import datetime

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

log_messages('ETL Pipeline for San Francisco Fire Incidents Data Ended')