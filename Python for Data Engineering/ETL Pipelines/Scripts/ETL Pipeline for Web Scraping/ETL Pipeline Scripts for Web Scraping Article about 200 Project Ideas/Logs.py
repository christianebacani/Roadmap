import Extract
import Transform
import Load
from datetime import datetime

# Logs Job

def logs(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    
    logfile = 'logfile.txt'
    
    with open(logfile, 'a') as f:
        f.write(f"{timestamp} : {message}\n")


# Extract
logs('(PROD) : Extracting Job Started')
extracted_data = Extract.extract()
print(extracted_data)
logs('(PROD) : Extracting Job Ended')


# Transform
logs('(PROD) : Transforming Job Started')
transformed_data = Transform.transform(extracted_data)
print(transformed_data)
logs('(PROD) : Transforming Job Ended')


# Load
logs('(PROD) : Loading Job Started')
loaded_data = Load.load(transformed_data)
print(loaded_data)
logs('(PROD) : Loading Job Ended')