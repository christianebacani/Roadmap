import requests

# Extract

def extract():
    # API Endpoint
    url = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/2025'
    response = requests.get(url=url)
    
    if response.status_code == 200:
        return response.json()
    
    else:
        print(response.status_code)

