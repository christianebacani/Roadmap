from datetime import datetime
import Extract
import Transform
import Load

# Logs

def logs(message):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(format)

    logfile = 'logfile.txt'

    with open(logfile, 'a') as f:
        f.write(f'{message} : {timestamp}\n')

logs('(PROD) : ETL Pipeline using Youtube Data API Started')


# Extract
logs('(PROD) : Extract Phase Started')
firstPageMostPopularVideosData, secondPageMostPopularVideosData = Extract.extract()

print('Extracted Data of Most Popular Youtube Videos in Philippines (First Page) :\n')
print(firstPageMostPopularVideosData)

print('\nExtracted Data of Most Popular Youtube Videos in Philippines (Second Page) :\n')
print(secondPageMostPopularVideosData)

logs('(PROD) : Extract Phase Ended')


# Transform
logs('(PROD) : Transform Phase Started')
transformedMostPopularVideosData = Transform.transform(firstPageMostPopularVideosData, secondPageMostPopularVideosData)

print('\nTransformed Data of Most Popular Youtube Videos in Philippines :\n')
print(transformedMostPopularVideosData)

logs('(PROD) : Transform Phase Ended')


# Load
logs('(PROD) : Load Phase Started')
loadedMostPopularVideosData = Load.load(transformedMostPopularVideosData)

print('\nLoaded Data of Most Popular Youtube Vides in Philippines :\n')
print(loadedMostPopularVideosData)

logs('(PROD) : Load Phase Ended')


logs('(PROD) : ETL Pipeline using Youtube Data API Ended')