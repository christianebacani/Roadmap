from bs4 import BeautifulSoup
import requests

# Extract

def extract(url):
    response = requests.get(url=url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('tbody')
        rows = table.find_all('tr')
    
        return rows
    
    return response.status_code

