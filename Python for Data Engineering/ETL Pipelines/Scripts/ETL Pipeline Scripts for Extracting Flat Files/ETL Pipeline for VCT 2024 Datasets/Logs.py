import Extract
import Transform
import Load
from datetime import datetime

# Logs

def logs(message):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(format)
    logfile = 'logfile.txt'

    with open(logfile, 'a') as f:
        f.write(f'{timestamp} : {message}\n')

logs('(PROD) ETL Pipeline for VCT 2024 Datasets Started')

# Extract
logs('(PROD) Extract Phase Started')
extracted_data = Extract.extract()
print("Extracted Data:")
print(extracted_data)
logs('(PROD) Extract Phase Ended')

# Transform
logs('(PROD) : Transform Phase Started')
transformed_data = Transform.transform(extracted_data)
print("\nTransformed Data:")
print(transformed_data)
logs('(PROD) : Transform Phase Ended')

# Load
logs('(PROD) : Load Phase Started')
loaded_data = Load.load(transformed_data)
print("\nLoaded Data:")
print(loaded_data)
logs('(PROD) : Load Phase Ended')

logs('(PROD) ETL Pipeline for VCT 2024 Datasets Ended')