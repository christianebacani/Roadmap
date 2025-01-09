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
    
logs('(DEV) : ETL Pipeline for Extracting Historical Weather Data from Historial Weather API Started')

# Extract
logs('(DEV) : Extract Phase Started')
extractedDailyWeatherDataFrom2024 = Extract.extract()
print('Extracted Daily Weather Data from Year 2024 : ')
print(extractedDailyWeatherDataFrom2024)
logs('(DEV) : Extract Phase Ended')

# Transform
logs('(DEV) : Transform Phase Started')
transformedDailyWeatherDataFrom2024, dailyWeatherParameterData, dailyWeatherMetaData = Transform.transform(extractedDailyWeatherDataFrom2024)
print('\nTransformed Daily Weather Data From 2024 : ')
print(transformedDailyWeatherDataFrom2024)

print('\nDaily Weather Parameter Data : ')
print(dailyWeatherParameterData)

print('\nDaily Weather MetaData : ')
print(dailyWeatherMetaData)
logs('(DEV) : Transform Phase Ended')

# Load
logs('(DEV) : Load Phase Started')
loadedDailyWeatherDataFrom2024, laodedWeatherParameterData, loadedDailyWeatherMetaData = Load.load(transformedDailyWeatherDataFrom2024, dailyWeatherParameterData, dailyWeatherMetaData)
print('\nLoaded Dailly Weather Data from 2024 : ')
print(loadedDailyWeatherDataFrom2024)

print('\nLoaded Weather Parameter Data : ')
print(laodedWeatherParameterData)

print('\nLoaded Weather Metadata : ')
print(loadedDailyWeatherMetaData)
logs('(DEV) : Load Phase Started')

logs('(DEV) : ETL Pipeline for Extracting Historical Weather Data from Historial Weather API Ended')
