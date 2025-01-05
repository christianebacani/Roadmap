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
    
logs('(DEV) : ETL Pipeline for Web Scraping Started')

# Extract
logs('(DEV) : Extract Phase Started')
laptopsWebURL, tabletsWebURL, phonesWebURL = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops', 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets', 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
gadgetsDF = Extract.extract(laptopsWebURL, tabletsWebURL, phonesWebURL)
print('Extracted Gadgets Data:')
print(gadgetsDF)
logs('(DEV) : Extract Phase Ended')

# Transform
logs('(DEV) : Transform Phase Started')
transformedGadgetsDF = Transform.transform(gadgetsDF)
print('\nTransformed Gadgets Data:')
print(transformedGadgetsDF)
logs('(DEV) : Transform Phase Ended')

# Load
logs('(DEV) : Load Phase Started')
loadedGadgetsDF = Load.load(transformedGadgetsDF)
print('\nLoaded Gadgets Data:')
print(loadedGadgetsDF)
logs('(DEV) : Load Phase Ended')

logs('(DEV) : ETL Pipeline for Web Scraping Started')
