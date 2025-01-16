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
    
    with open(logfile ,'a') as f:
        f.write(f'{message} : {timestamp}\n')

logs('(PROD) : ETL Pipeline for Web Scraping of Most High Ranked Films Started')

# Extract
logs('(PROD) : Extract Phase Started')
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
extractedFilmsData = Extract.extract(url)
print(extractedFilmsData)
logs('(PROD) : Extract Phase Ended')

print()

# Transform
logs('(PROD) : Transform Phase Started')
transformedFilmsData = Transform.transform(extractedFilmsData)
print(transformedFilmsData)
logs('(PROD) : Transform Phase Ended')

print()

# Load
logs('(PROD) : Load Phase Started')
filmsData = Load.load(transformedFilmsData)
print(filmsData)
logs('(PROD) : Load Phase Ended')

logs('(PROD) : ETL Pipeline for Web Scraping of Most High Ranked Films Ended')