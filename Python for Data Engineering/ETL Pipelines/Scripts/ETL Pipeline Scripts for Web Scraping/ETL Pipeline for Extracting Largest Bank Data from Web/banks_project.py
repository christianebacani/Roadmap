from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine




# Extract
def extract(url, tableAttr):
    response = requests.get(url)
    
    # Extract the data using request library and parse the response into a soup object
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody = soup.find_all('tbody')
    rows = tbody[2].find_all('tr')
    
    
    # Initialize a dictionary to store extracted data
    largestBankDict = {tableAttr[0] : [], tableAttr[1] : []}


    # Extracte necessary data from soup object to dictionary
    for rowNumber, row in enumerate(rows):
        rowNumber += 1
        tdTable = row.find_all('td')
    
        if len(tdTable) >= 4:
            largestBankDict[tableAttr[0]].append(str(tdTable[0].text).strip())
            largestBankDict[tableAttr[1]].append(str(tdTable[2].text).replace('\n', '').strip())
    
    
    # Convert dictionary to dataframe
    largestBankDf = pd.DataFrame(largestBankDict)

    return largestBankDf




# Transform
def transform(df, csvFilepath):
    # Initialize a dictionary to store transformed data
    transformedDict = {'Name' : [], 'MC_USD_Billion' : [],
                       'MC_GBP_Billion' : [], 'MC_EUR_Billion' : [], 
                       'MC_INR_Billion' : []}
    

    # Extract Exchanges Rates Data from CSV File to a Exchange Rates Dictionary for exchange rate conversion
    exchangeRatesDf = pd.read_csv(csvFilepath)
    exchangeRatesDict = {}
    
    for _, row in exchangeRatesDf.iterrows():
        exchangeRatesDict[row.get('Currency')] = float(row.get('Rate'))
    
        
    # Transform data from the dataframe and store in dictionary
    for index, row in df.iterrows():
        if index <= 9:
            transformedDict['Name'].append(row.get('Name'))
            

            # Initialize a dictionary to store market cap of different exchange rates
            marketCapDict = {'MC_USD_Billion' : None, 'MC_GBP_Billion' : None,
                             'MC_EUR_Billion' : None, 'MC_INR_Billion' : None}
            

            # Convert usd billion market cap to different market cap exchanges rates (GBP, EUR, and INR)
            marketCapDict['MC_USD_Billion'] = float(row.get('MC_USD_Billion'))
            
            marketCapDict['MC_GBP_Billion'] = marketCapDict['MC_USD_Billion'] * exchangeRatesDict['GBP']
            marketCapDict['MC_EUR_Billion'] = marketCapDict['MC_USD_Billion'] * exchangeRatesDict['EUR']
            marketCapDict['MC_INR_Billion'] = marketCapDict['MC_USD_Billion'] * exchangeRatesDict['INR']


            # Map different market cap dictionaries to the main dictionary (transformedDict)
            for column, value in marketCapDict.items():
                transformedDict[column].append(f'{value:.2f}')
    

    # Convert transformedDict to dataframe
    transformedDf = pd.DataFrame(transformedDict)

    return transformedDf




# Load to CSV Filepath
def load_to_csv(df, csvFilepath):
    df.to_csv(csvFilepath, index=False)




# Load to Local MySQL Database Instance
def load_to_db(df, engine, tableName):
    df.to_sql(tableName, engine, if_exists='replace', index=False)




# Run Query in Local MySQL Database Instance
def run_query(query, engine):
    print(pd.read_sql(query[0], engine), '\n\n')
    print(pd.read_sql(query[1], engine), '\n\n')
    print(pd.read_sql(query[2], engine))




# Logs
def log_progress(message):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(format)

    logfile = 'code_log.txt'

    with open(logfile, 'a') as f:
        f.write(f'{timestamp} : {message}\n')


log_progress('Preliminaries complete. Initiating ETL Process')

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks#By_market_capitalization'
tableAttributes = ['Name', 'MC_USD_Billion']
df = extract(url, tableAttributes)
log_progress('Data Extraction complete. Initiating Transformation Process')

exchangeRatesCsvFilepath = 'Source Data Files\\Largest Banks Data\\exchange_rate.csv'
transformedDf = transform(df, exchangeRatesCsvFilepath)
log_progress('Data Transformation complete. Initiating Loading Process')

targetCsvFilepath = 'Target Data Files\\Largest Bank Data\\CSV Files\\Largest_banks_data.csv'
load_to_csv(transformedDf, targetCsvFilepath)
log_progress('Data saved to CSV file')

log_progress('SQL Connection Initiated')
username = '<YOUR_USERNAME>'
password = '<YOUR_PASSWORD>'
hostname = '<YOUR_HOSTNAME>'
dbName = 'Banks'
tableName = 'largest_banks'
engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{dbName}')
load_to_db(transformedDf, engine, tableName)
log_progress('Data loaded to Database as a table, Executing queries')


displayContentsQuery = 'SELECT * FROM largest_banks'
avgMarketCapUsdQuery = 'SELECT ROUND(AVG(MC_USD_Billion), 2) AS Avearge_Market_Cap_USD_Billion FROM largest_banks'
top5BankNames = 'SELECT Name FROM largest_banks LIMIT 5'
queryStatements = [displayContentsQuery, avgMarketCapUsdQuery, top5BankNames]
run_query(queryStatements, engine)
log_progress('Process Complete')

log_progress('Server Connection closed')


