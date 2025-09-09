import requests
from bs4 import BeautifulSoup

url = 'https://www.pagasa.dost.gov.ph/weather#daily-weather-forecast'

try:    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    row_weather_page = soup.find_all('div', attrs={'class': 'row weather-page'})
    print(row_weather_page)

except Exception as error_message:
    print(f'Error fetching URL: {error_message}')