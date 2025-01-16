import Extract
import Transform
import Load
from datetime import datetime
import asyncio


# Logs Function
def logs(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now() # Datetime
    timestamp = now.strftime(timestamp_format)

    logfile = 'logfile.txt'
    with open(logfile, 'a') as f:
        f.write(f"{timestamp} : {message}\n")


logs('(PROD) Extracting Data Job Started')
asyncio.run(Extract.get_text_content())
logs('(PROD) Extracting Data Job Ended')

logs('(PROD) Transforming Data Job Started')
transformed_data = Transform.transform_data()
logs('(PROD) Transforming Data Job Ended')

logs('(PROD) Loading Data Job Started')
Load.load(transformed_data)
logs('(PROD) Loading Data Job Ended')
