import requests

# Extract

def extract():
    # API Endpoint
    url = '<API_ENDPOINT>'

    # Requests to access data to the API Endpoint
    response = requests.get(url=url)

    if response.status_code == 200:
        responseJSON = response.json()
        dailyWeatherDataFrom2024 = responseJSON
        
        return dailyWeatherDataFrom2024
    
    else:
        return None
    