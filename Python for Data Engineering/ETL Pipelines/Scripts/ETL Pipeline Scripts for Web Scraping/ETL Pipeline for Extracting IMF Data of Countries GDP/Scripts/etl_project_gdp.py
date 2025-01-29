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

    # Extracting Website Data and parsing into a soup object    
    soup = BeautifulSoup(response.text, 'html.parser')
    body = soup.find_all('tbody')
    rows = body[2].find_all('tr')


    # Intialize a dictionary to store extracted soup object
    gdpPerCountryDict = {}

    for tableAttribute in tableAttributes:
        gdpPerCountryDict[tableAttribute] = []


    # Map the soup object data to dictionary
    for row in rows:
        tdTable = row.find_all('td', None)
        currentRowData = []

        if (tdTable is not None) and (len(tdTable) >= 7):
            for i in range(7):
                currentRowData.append(str(tdTable[i].text).strip())
        
        if len(currentRowData) == 7:
            for i in range(len(currentRowData)):
                gdpPerCountryDict[tableAttributes[i]].append(currentRowData[i])
    

    # Convert dictionary to dataframe
    gdpPerCountryDf = pd.DataFrame(gdpPerCountryDict)
    
    return gdpPerCountryDf




# Transform
def transform(df):
    # Initialize a dictionary to be mapped from the current dataframe
    transformDict = {}
    
    for column in list(df.keys()):
        transformDict[column] = []

    
    # List consist of column names
    gdpColumns = ['IMF_GDP_USD_millions', 'World_Bank_GDP_USD_millions', 'United_Nations_GDP_USD_millions']
    yearEstimateColumns = ['IMF_Year_Estimate', 'World_Bank_Year_Estimate', 'UN_Year_Estimate']


    # Transform every row of the dataframe by converting GDP millions to billions and remove unnecessary data from the year estimates column
    for _, row in df.iterrows():
        for column in list(df.keys()):
            value = str(row.get(column))
            
            if value == 'World':
                break

            elif column in gdpColumns:
                value = f'{float(value.replace(',', '')) / 1000:.2f}'
            
            elif (column in yearEstimateColumns) and (len(value) != 4):
                value = value[5:].replace(']', '')
            
            
            # Map the cleaned/transformed data from the dataframe to dictionary
            transformDict[column].append(value)
    

    # Convert dictionary to dataframe
    transformDf = pd.DataFrame(transformDict)

    # Rename columns
    transformDf.rename(columns={'IMF_GDP_USD_millions' : 'IMF_GDP_USD_billions',
                                'World_Bank_GDP_USD_millions' : 'World_Bank_GDP_USD_billions',
                                'United_Nations_GDP_USD_millions' : 'United_Nations_GDP_USD_billions'}, inplace=True)
    return transformDf




# Load to CSV Filepath
def load_to_csv(df, csvFilepath):
    df.to_csv(csvFilepath, index=False)




# Load to JSON Filepath
def load_to_json(df, jsonFilepath):
    with open(jsonFilepath, 'w') as f:
        f.write(df.to_json(orient='records'))
    f.close()




# Load to XML Filepath
def load_to_xml(df, xmlFilepath):
    with open(xmlFilepath, 'w') as f:
        f.write(df.to_xml(index=False, parser='lxml'))
    f.close()




# Load to Local MySQL Database
def load_to_mysql_db(df, engine, tableName):
    df.to_sql(tableName, engine, if_exists='replace', index=False)




# Run Query in Local MySQL Database
def run_query(query, engine):
    queryDf = pd.read_sql(query, engine)
    return queryDf




# Log Progress
def log_progress(message):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(format)

    logfile = 'etl_project_log.txt'

    with open(logfile, 'a') as f:
        f.write(f'{timestamp} : {message}\n')




log_progress('[PROD] ETL Pipeline for Extracting GDP Per Countries Data from the Wikipedia Ended')


# Extract
log_progress('[PROD] Extract Phase Started')
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29#Table'
tableAttributes = ['Country', 'IMF_GDP_USD_millions', 'IMF_Year_Estimate', 'World_Bank_GDP_USD_millions', 'World_Bank_Year_Estimate', 'United_Nations_GDP_USD_millions', 'UN_Year_Estimate']
df = extract(url, tableAttributes)
log_progress('[PROD] Extract Phase Ended')


# Transform
log_progress('[PROD] Transform Phase Started')
transformedDf = transform(df)
log_progress('[PROD] Transform Phase Ended')


# Load to CSV Filepath
log_progress('[PROD] Load Phase to CSV Filepath Started')
csvFilepath = 'Target Data Files\\GDP Per Country Data\\Filepaths\\CSV File\\Countries_by_GDP.csv'
load_to_csv(transformedDf, csvFilepath)
log_progress('[PROD] Load Phase to CSV Filepath Ended')


# Load to JSON Filepath
log_progress('[PROD] Load Phase to JSON Filepath Started')
jsonFilepath = 'Target Data Files\\GDP Per Country Data\\Filepaths\\JSON File\\Countries_by_GDP.json'
load_to_json(transformedDf, jsonFilepath)
log_progress('[PROD] Load Phase to JSON Filepath Ended')


# Load to XML Filepath
log_progress('[PROD] Load Phase to XML Filepath Started')
xmlFilepath = 'Target Data Files\\GDP Per Country Data\\Filepaths\\XML File\\Countries_by_GDP.xml'
load_to_xml(transformedDf, xmlFilepath)
log_progress('[PROD] Load Phase to XML Filepath Ended')


# Load to Local MySQL Database
log_progress('[PROD] Load Phase to Local MySQL Database Started')
username = '<YOUR_USERNAME>'
password = '<YOUR_PASSWORD>'
hostname = '<YOUR_HOSTNAME>'
dbName = 'world_economies'
tableName = 'countries_by_gdp'
engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{dbName}')
load_to_mysql_db(transformedDf, engine, tableName)
log_progress('[PROD] Load Phase to Local MySQL Database Ended')


# Run MySQL Query
log_progress('[PROD] Runing MySQL Database Query Started')
query = 'SELECT * FROM countries_by_gdp WHERE IMF_GDP_USD_billions >= 1.0 AND World_Bank_GDP_USD_billions >= 1.0 AND United_Nations_GDP_USD_billions >= 1.0'
queryDf = run_query(query, engine)
print(queryDf)
log_progress('[PROD] Runing MySQL Database Query Ended')


log_progress('[PROD] ETL Pipeline for Extracting GDP Per Countries Data from the Wikipedia Ended')