from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from sqlalchemy import create_engine




# Extract
def extract(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    return soup.find('tbody').find_all('tr')
        



# Transform
def transform(rows):
    gdpPerCountryDict = {'Country' : [], 'GDP_USD_billion' : []}
    outdatedGdpCountries = {'Cuba' : '$107,352,000,000', 'Turkmenistan' : '$45,610,571,429', 'Lebanon' : '$23,131,941,557',
                            'Afghanistan' : '$14,583,135,237', 'Guam' : '$6,123,000,000', 'Aruba' : '$3,126,019,385',
                            'Bhutan' : '$2,539,551,327', 'San Marino' : '$1,855,382,833', 'Northern Mariana Islands' : '858,000,000',
                            'Northern Mariana Islands' : '858,000,000', 'American Samoa' : '$709,000,000', 'Tonga' : '$469,228,124',
                            'Palau' : '$217,800,000'}
    
    for row in rows:
        tdList = row.find_all('td')
        
        gdpPerCountryDict['Country'].append(tdList[1].text)
        gdpPerCountryDict['GDP_USD_billion'].append(f'{float(str(tdList[2].text).replace('$', '').replace(',', '')):.2f}')
    
    
    for key, value in outdatedGdpCountries.items():
        gdpPerCountryDict['Country'].append(key)
        gdpPerCountryDict['GDP_USD_billion'].append(f'{float(str(value).replace('$', '').replace(',', '')):.2f}')


    gdpPerCountryDf = pd.DataFrame(gdpPerCountryDict)

    return gdpPerCountryDf    




# Load
def load(df):
    username = '<YOUR_USERNAME>'
    password = '<YOUR_PASSWORD>'
    hostname = '<HOST_NAME>'
    dbName = 'World_Economies'
    
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{dbName}')
    df.to_sql('countries_by_gdp', engine, if_exists='replace', index=False)
    
    jsonFilepath = 'Target Data Files\\GDP Per Country Data\\JSON File\\Countries_by_GDP.json'
    jsonDf = df.to_json(orient='records')
    
    with open(jsonFilepath, 'w') as f:
        f.write(jsonDf)

    f.close()
   



# Time Log Per Job
def executeLogsPerJob(message):
    for seconds in range(3, 0, -1):
        print(f'{message} in {seconds}...', end='')
        time.sleep(1)
        print()




# Logs
def logs(message):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(format)

    logfile = 'etl_project_log.txt'

    with open(logfile, 'a') as f:
        f.write(f'{timestamp} : {message}\n')




logs('[PROD] ETL Pipeline for Web Scraping GDP Per Country of Yera 2022 Started')


# Extract
logs('[PROD] Extract Phase Started')
executeLogsPerJob('Extracting Country and GDP Data from Website')
url = 'https://www.worldometers.info/gdp/gdp-by-country/'
rows = extract(url)
print('Successfully Extracted Country and GDP Data.', end='')
time.sleep(1)
print('\n')
logs('[PROD] Extract Phase Ended')


# Transform
logs('[PROD] Transform Phase Started')
executeLogsPerJob('Transforming Extracted GDP and Country Data')
df = transform(rows)
print('Successfully Converted into Pandas Dataframe.', end='')
time.sleep(1)
print('\n')
logs('[PROD] Transform Phase Ended')


# Load
logs('[PROD] Load Phase Started')
executeLogsPerJob('Loading Data')
load(df)
print('Successfully Loaded to the Local MySQL Database and JSON File.', end='')
print()
logs('[PROD] Load Phase Ended')


logs('[PROD] ETL Pipeline for Web Scraping GDP Per Country of Yera 2022 Ended')