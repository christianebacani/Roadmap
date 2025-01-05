import requests
from bs4 import BeautifulSoup
import pandas as pd

# Extract Module

def extract(laptopsWebURL, tabletsWebURL, phonesWebURL):
    requestLaptopsDataResponse, requestsTabletsDataResponse, requestsPhonesDataResponse = requests.get(laptopsWebURL), requests.get(tabletsWebURL), requests.get(phonesWebURL)
    
    if (requestLaptopsDataResponse.status_code == 200) and (requestsTabletsDataResponse.status_code == 200) and (requestsPhonesDataResponse.status_code == 200):
        laptopsDataSoup, tabletsDataSoup, phonesDataSoup = BeautifulSoup(requestLaptopsDataResponse.text, 'html5lib'), BeautifulSoup(requestsTabletsDataResponse.text, 'html5lib'), BeautifulSoup(requestsPhonesDataResponse.text, 'html5lib')

    else:
        print('You can\'t scrape this website')


    laptopsDataDiv, tabletsDataDiv, phonesDataDiv = laptopsDataSoup.find_all('div', {'class' : 'col-md-4 col-xl-4 col-lg-4'}), tabletsDataSoup.find_all('div', {'class' : 'col-md-4 col-xl-4 col-lg-4'}), phonesDataSoup.find_all('div', {'class' : 'col-md-4 col-xl-4 col-lg-4'})
    gadgetsDataDict = {'Device Name' : [], 'Price' : [], 'Description' : [], 'Device Type' : [], 'Review Count' : []}
    
    
    for element in laptopsDataDiv:
        caption = element.find('div', {'class' : 'caption'})
        ratings = element.find('div', {'class' : 'ratings'})
        
        gadgetsDataDict['Device Name'].append(str(caption.find('a', {'class' : 'title'}).text).strip())
        gadgetsDataDict['Price'].append(str(caption.find('h4', {'class' : 'price float-end card-title pull-right'}).text).strip())
        gadgetsDataDict['Description'].append(str(caption.find('p', {'class' : 'description card-text'}).text).strip())
        gadgetsDataDict['Device Type'].append('Laptop')
        gadgetsDataDict['Review Count'].append(str(ratings.find('p', {'class' : 'review-count float-end'}).text).strip())
        

    for element in tabletsDataDiv:
        caption = element.find('div', {'class' : 'caption'})
        ratings = element.find('div', {'class' : 'ratings'})

        gadgetsDataDict['Device Name'].append(str(caption.find('a', {'class' : 'title'}).text).strip())
        gadgetsDataDict['Price'].append(str(caption.find('h4', {'class' : 'price float-end card-title pull-right'}).text).strip())
        gadgetsDataDict['Description'].append(str(caption.find('p', {'class' : 'description card-text'}).text).strip())
        gadgetsDataDict['Device Type'].append('Tablet')
        gadgetsDataDict['Review Count'].append(str(ratings.find('p', {'class' : 'review-count float-end'}).text).strip())


    for element in phonesDataDiv:
        caption = element.find('div', {'class' : 'caption'})
        ratings = element.find('div', {'class' : 'ratings'})
    
        gadgetsDataDict['Device Name'].append(str(caption.find('a', {'class' : 'title'}).text).strip())
        gadgetsDataDict['Price'].append(str(caption.find('h4', {'class' : 'price float-end card-title pull-right'}).text).strip())
        gadgetsDataDict['Description'].append(str(caption.find('p', {'class' : 'description card-text'}).text).strip())
        gadgetsDataDict['Device Type'].append('Phone')
        gadgetsDataDict['Review Count'].append(str(ratings.find('p', {'class' : 'review-count float-end'}).text).strip())

    gadgetsDF = pd.DataFrame(gadgetsDataDict)
    
    return gadgetsDF