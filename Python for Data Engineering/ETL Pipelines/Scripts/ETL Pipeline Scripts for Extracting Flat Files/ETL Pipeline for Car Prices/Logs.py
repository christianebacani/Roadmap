import Extract
import Transform
import Load
from datetime import datetime

# Logs

def logs(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    logfile = 'logfile.txt'

    with open(logfile, 'a') as f:
        f.write(f"{timestamp} : {message}\n")


# Executing the ETL Pipeline
logs('(PROD) : ETL Pipeline Started')

# Extract Phase
logs('(PROD) : Extracting Job Started')
extracted_data = Extract.extract()
print("Extracted Data:")
print(extracted_data)
logs('(PROD) : Extracting Job Ended')

# Transform Phase
logs("(PROD) : Transforming Job Started")
transformed_data = Transform.transform(extracted_data)
print("\nTransformed Data:")
print(transformed_data)
logs('(PROD) : Transforming Job Ended')


# Load Phase
logs('(PROD) : Loading Job Started')
loaded_data = Load.load(transformed_data)
print("\nLoaded Data:")
print(loaded_data)
logs('(PROD) : Loading Job Ended')

# ETL Pipeline Ended
logs('(PROD) : ETL Pipeline Ended')