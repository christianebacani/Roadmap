import Extract
import Transform
import Load 
import RunQuery
from datetime import datetime
import os
import sqlite3

# Logs

def logs(message):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(format)

    logfile = 'logfile.txt'

    with open(logfile, 'a') as f:
        f.write(f'{timestamp} : {message}\n')

        
logs('[PROD] ETL Pipeline for Earthquakes Data from 1900-2023 Started')


# Extract
logs('[PROD] Extract Phase Started')
zipfilepath = 'Source Data Files\\Earthquake Dataset 1900-2023\\Earthquake Zipfile.zip'
df = Extract.extract(zipfilepath)
logs('[PROD] Extract Phase Ended')


# Transform
logs('[PROD] Transform Phase Started')
earthquakeDf = Transform.transform(df)
logs('[PROD] Transform Phase Ended')


# Load to CSV Filepath
logs('[PROD] Loading to CSV Filepath Started')
csvFilepath = 'Target Data Files\\Earthquake Datasets from 1900-2023\\CSV Files\\earthquake_data.csv'
Load.load_to_csv(earthquakeDf, csvFilepath)
logs('[PROD] Loading to CSV Filepath Ended')


# Load to JSON Filepath
logs('[PROD] Loading to JSON Filepath Started')
jsonFilepath = 'Target Data Files\\Earthquake Datasets from 1900-2023\\JSON Files\\earthquake_data.json'
Load.load_to_json(earthquakeDf, jsonFilepath)
logs('[PROD] Loading to JSON Filepath Ended')


# Load to XML Filepath
logs('[PROD] Loading to XML Filepath Started')
xmlFilepath = 'Target Data Files\\Earthquake Datasets from 1900-2023\\XML Files\\earthquake_data.xml'
Load.load_to_xml(earthquakeDf, xmlFilepath)
logs('[PROD] Loading to XML Filepath End')


# Load to Local SQLite Database
logs('[PROD] Loading to Local SQLite Database Started')
conn = sqlite3.connect('Target Data Files\\Earthquake Datasets from 1900-2023\\Database File\\earthquakes_data.db')
tableName = 'earthquake_data'
Load.load_to_sqlite_db(earthquakeDf, conn, tableName)
logs('[PROD] Loading to Local SQLite Database Ended')


# Run Query at Local SQLite Database
logs('[PROD] Running Query at Local SQLite Database Started')
query = 'SELECT time, place, latitude, longitude, magnitude FROM earthquake_data WHERE magnitude >= 5.0 ORDER BY magnitude DESC'
query = RunQuery.run_query(query, conn)
print(query)
logs('[PROD] Running Query at Local SQLite Database Started')


os.remove('earthquake_data.csv')


logs('[PROD] ETL Pipeline for Earthquakes Data from 1900-2023 Ended')