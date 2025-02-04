from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine




# Extract
def extract(url : str, tableAttrs : list) -> pd.DataFrame:
    # Request to extract the information from the website
    response = requests.get(url=url)


    # Convert extracted website data to Beautiful Soup Object
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody  = soup.find_all('tbody')
    rows = tbody[0].find_all('tr')


    # Initialize a dictionary to store extracted website data
    banksDataDict = {tableAttrs[0] : [], tableAttrs[1] : []}


    # Map extrated website data to dictionary
    for row in rows:
        bankData = row.find_all('td')
        
        if len(bankData) >= 3:
            bankName = bankData[1].find_all('a')[1].text
            marketCapUsdBillion = float(str(bankData[2].text)[:-1])

            banksDataDict[tableAttrs[0]].append(bankName)
            banksDataDict[tableAttrs[1]].append(marketCapUsdBillion)    


    # Convert dictionary to dataframe
    banksDataDf = pd.DataFrame(banksDataDict)

    return banksDataDf




# Transform
def transform(df : pd.DataFrame, csvFilepath : str) -> pd.DataFrame:
    # Initialize a dictionary to map dataframe from the paratemeters
    transformedBanksDataDict = {'Name' : [], 'MC_USD_Billion' : [], 'MC_GBP_Billion' : [], 
                                'MC_EUR_Billion' : [], 'MC_INR_Billion' : []}
    

    # Extract exchange rates data from the csv filapath
    exchangeRateDf = pd.read_csv(csvFilepath)
    exchangeRateDict = {}

    for _, row in exchangeRateDf.iterrows():
        exchangeRateDict[row.get('Currency')] = float(row.get('Rate'))


    # Transform values of dataframe from the parameter
    for _, row in df.iterrows():
        bankName = row.get('Name')
        marketCapUsdBillion = row.get('MC_USD_Billion')

        # Map transformed values to dictionary
        exchangeRateCurrencies = ['GBP', 'EUR', 'INR']
        transformedBanksDataDict['Name'].append(bankName)
        transformedBanksDataDict['MC_USD_Billion'].append(marketCapUsdBillion)

        for currency in exchangeRateCurrencies:
            transformedBanksDataDict[f'MC_{currency}_Billion'].append(round(marketCapUsdBillion * exchangeRateDict[currency], 2))


    # Convert dictionary to dataframe
    transformedBanksDataDf = pd.DataFrame(transformedBanksDataDict)

    return transformedBanksDataDf




# Load to Different Flat Filepath Formats
def load_to_files(df : pd.DataFrame, filepaths : dict) -> None:
    df.to_csv(filepaths['CSV Filepath'], index=False)
    
    with open(filepaths['JSON Filepath'], 'w') as f:
        f.write(df.to_json(orient='records'))
    f.close()

    df.to_xml(path_or_buffer=filepaths['XML Filepath'], root_name='Largest_Banks_Data', row_name='Bank', index=False, parser='lxml')




# Load to Local MySQL Database Instance
def load_to_db(df : pd.DataFrame, engine : str, tableName : str) -> None:
    df.to_sql(tableName, engine, if_exists='replace', index=False)




# Run Query in MySQL Database
def run_query(queryStatement : list, engine : str) -> None:
    for query in queryStatement:
        print(pd.read_sql(query, engine), end='\n\n')




# Logs
def log_progress(message : str) -> None:
    format = '%Y-%m-%d'
    now = datetime.now()
    timestamp = now.strftime(format)

    logfile  = 'code_log.txt'
    
    with open(logfile, 'a') as f:
        f.write(f'{timestamp} : {message}\n')


log_progress('Preliminaries complete. Initiating ETL Process')


# Extract
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
tableAttributes = ['Name', 'MC_USD_Billion']
df = extract(url, tableAttributes)
log_progress('Data Extraction Complete. Initiating Transformation process')


# Transform
currencyExchangeCsvFilepath = 'Source Data Files\\Largest Banks Data\\exchange_rate.csv'
transformedDf = transform(df, currencyExchangeCsvFilepath)
log_progress('Data Transformation Complete. Initiating Loading process')


# Load to Target Data Sources
filepathsDict = {'CSV Filepath' : 'Target Data Files\\Largest Bank Data\\CSV Files\\Largest_banks_data.csv',
                 'JSON Filepath' : 'Target Data Files\\Largest Bank Data\\JSON Files\\Largest_banks_data.json',
                 'XML Filepath' : 'Target Data Files\\Largest Bank Data\\XML Files\\Largest_banks_data.xml'}
load_to_files(transformedDf, filepathsDict)
log_progress('Data saved to different Flat Filepaths Format')


# Load to Local MySQL Database Instance
log_progress('SQL Connection Initiated')
username = '<YOUR_USERNAME>'
password = '<YOUR_PASSWORD>'
hostname = '<YOUR_HOSTNAME>'
dbName = 'banks'
tableName = 'largest_banks'
engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{dbName}')
load_to_db(transformedDf, engine, tableName)
log_progress('Data loaded to as a table, Executing queries')


# Run Query in MySQL Database
queryStatements = ['SELECT * FROM largest_banks', 'SELECT AVG(MC_GBP_Billion) AS Average_MC_GBP_Billion FROM largest_banks', 'SELECT Name FROM largest_banks LIMIT 5']
run_query(queryStatements, engine)
log_progress('Process complete')

log_progress('Server Connection closed')


