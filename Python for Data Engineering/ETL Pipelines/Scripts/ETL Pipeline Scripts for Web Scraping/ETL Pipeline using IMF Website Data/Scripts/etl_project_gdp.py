from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import sqlite3 
from sqlalchemy import create_engine




# Extract
def extract(url, tableAttributes):
    response = requests.get(url=url)


    # Parsing Response Content into Beautiful Soup Object
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.find_all('tbody')
    rows = body[2].find_all('tr')


    # Initializing dictionary to map Beautiful Soup Object
    gdpPerCountryDict = {tableAttributes[0] : [], tableAttributes[1] : []}


    # Mapping Soup Object to Dictionary    
    for row in rows:
        tdTable = row.find_all('td')
        
        for index, data in enumerate(tdTable):
            if index == 0:
                gdpPerCountryDict[tableAttributes[0]].append(str(data.text).strip())
                
            elif index == 2:
                gdpPerCountryDict[tableAttributes[1]].append(str(data.text).strip())


    # Convert Dictionary to Dataframe
    gdpPerCountryDf = pd.DataFrame(gdpPerCountryDict)

    return gdpPerCountryDf




# Transform
def transform(df):
    # Initialize a dictionary that will be map from the current dataframe
    transformedDict = {'Country' : [], 'GDP_USD_billion' : []}
    

    # Transform values in the current dataframe and map to the dictionary
    for _, row in df.iterrows():
        country = row.get('Country')
        gdpNominal = row.get('GDP_USD_millions')
        
        if (country == 'World') or (gdpNominal == '—'):
            continue 

        gdpNominal = f'{float(str(gdpNominal).replace(',', '')) / 1000:.2f}'

        transformedDict['Country'].append(country)
        transformedDict['GDP_USD_billion'].append(gdpNominal)
    

    # Convert dictionary to dataframe
    transformedDf = pd.DataFrame(transformedDict)

    return transformedDf




# Load To CSV 
def load_to_csv(df, csvFilepath):
    df.to_csv(csvFilepath, index=False)




# Load to JSON
def load_to_json(df, jsonFilepath):
    with open(jsonFilepath, 'w') as f:
        f.write(df.to_json(orient='records'))    
    
    f.close()




# Load to XML
def load_to_xml(df, xmlFilepath):
    with open(xmlFilepath, 'w') as f:
        f.write(df.to_xml(index=False, parser='lxml'))

    f.close()




# Load To SQLite Database
def load_to_sqlite_db(df, conn, tableName):
    df.to_sql(tableName, conn, if_exists='replace', index=False)




# Load to MySQL Database
def load_to_mysql_db(df, engine, tableName):
    df.to_sql(tableName, engine, if_exists='replace', index=False)




# Run Query to the Database
def run_query(queryStatement, conn):
    queryResult = pd.read_sql(queryStatement, conn)
    print(queryResult)




# Log Progress
def log_progress(message):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(format)
    
    logfile = 'etl_project_log.txt'

    with open(logfile, 'a') as f:
        f.write(f'{timestamp} : {message}\n')




# Terminal Log Job Progress
def terminalLogJobProgress(message):
    for seconds in range(3, 0, -1):
        print(f'{message} in {seconds}...', end='')
        time.sleep(1)
        print()




log_progress('[PROD] ETL Pipeline for Practice Project using IMF Website Data Started')


# Extract
log_progress('[PROD] Extract Phase Started')
terminalLogJobProgress('Extracting Website Data')
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29#Table'
tableAttributes = ['Country', 'GDP_USD_millions']
earthquakeDf = extract(url, tableAttributes)
print('Successfully Extracted Website Data.', end='')
time.sleep(1)
print('\n')
log_progress('[PROD] Extract Phase Ended')


# Transform
log_progress('[PROD] Transform Phase Started')
terminalLogJobProgress('Transforming GDP Per Countries Data')
transformedEarthquakeDf = transform(earthquakeDf)
print('Successfully Transformed Data.', end='')
time.sleep(1)
print('\n')
log_progress('[PROD] Transform Phase Ended')


# Load To CSV
log_progress('[PROD] Loading To CSV File Phase Started')
terminalLogJobProgress('Loading to CSV Filepath')
csvFilepath = 'Target Data Files\\GDP Per Country Data\\Filepaths\\CSV File\\Countries_by_GDP.csv'
load_to_csv(transformedEarthquakeDf, csvFilepath)
print('Successfully Loaded to CSV Filepath.', end='')
time.sleep(1)
print('\n')
log_progress('[PROD] Loading To CSV File Phase Ended')


# Load to JSON
log_progress('[PROD] Loading to JSON File Phase Started')
terminalLogJobProgress('Loading to JSON Filepath')

jsonFilepath = 'Target Data Files\\GDP Per Country Data\\Filepaths\\JSON File\\Countries_by_GDP.json'
load_to_json(transformedEarthquakeDf, jsonFilepath)
print('Successfully Loaded to JSON Filepath.', end='')
time.sleep(1)
print('\n')
log_progress('[PROD] Loading to JSON File Phase Ended')


# Load to XML
log_progress('[PROD] Loading to XML File Phase Started')
terminalLogJobProgress('Loading to XML Filepath')
xmlFilepath = 'Target Data Files\\GDP Per Country Data\\Filepaths\\XML File\\Countries_by_GDP.xml'
load_to_xml(transformedEarthquakeDf, xmlFilepath)
print('Successfully Loaded to XML Filepath.', end='')
time.sleep(1)
print('\n')
log_progress('[PROD] Loading to XML File Phase Ended')


# Load To Local SQLite Database
log_progress('[PROD] Loading to Local SQLite Database Started')
terminalLogJobProgress('Loading to Local SQLite Database')
conn = sqlite3.connect('Target Data Files\\GDP Per Country Data\\Database File\\World_Economies.db')
tableName = 'Countries_By_GDP'
load_to_sqlite_db(transformedEarthquakeDf, conn, tableName)
print('Successfully Loaded to the Local SQLite Database.', end='')
time.sleep(1)
print('\n')
log_progress('[PROD] Loading to Local SQLite Database Ended')


# Load to Local MySQL Database
log_progress('[PROD] Loading to Local MySQL Database Started')
terminalLogJobProgress('Loading to Local MySQL Database')
username = '<YOUR_USERNAME>'
password = '<YOUR_PASSWORD>'
hostname = '<HOSTNAME>'
dbName = 'world_economies'
tableName = 'countries_by_gdp'
engine = f'mysql+pymysql://{username}:{password}@{hostname}/{dbName}'
load_to_mysql_db(transformedEarthquakeDf, engine, tableName)
print('Successfully Loaded to Local MySQL Database.', end='')
time.sleep(1)
print('\n')
log_progress('[PROD] Loading to Local MySQL Database Ended')


# Run Query in Local SQLite Database
log_progress('[PROD] Running Query from the SQLite Database Started')
terminalLogJobProgress('Running Query in the Local SQLite Database')
queryStatement = 'SELECT * FROM Countries_by_GDP WHERE GDP_USD_billion >= 1000000000'
run_query(queryStatement, conn)
print('Successfully Run a Query from the Local SQLite Database.', end='')
time.sleep(1)
print()
log_progress('[PROD] Running Query from the SQLite Database Ended')


log_progress('[PROD] ETL Pipeline for Practice Project using IMF Website Data Ended')