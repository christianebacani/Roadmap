import requests

# Extract

def extract():
    # API Endpoints
    firstPageURL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=PH&maxResults=50&pageToken=<PAGE_TOKEN>&key=<YOUR_API_KEY>'

    secondPageURL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=PH&maxResults=50&pageToken=<PAGE_TOKEN>&key=<YOUR_API_KEY>'

    firstPageResponse, secondPageResponse = requests.get(firstPageURL), requests.get(secondPageURL)

    if (firstPageResponse.status_code == 200) and (secondPageResponse.status_code == 200):
        firstPageResponseJSON, secondPageResponseJSON = firstPageResponse.json(), secondPageResponse.json()
        firstPageMostPopularVideosData, secondPageMostPopularVideosData = firstPageResponseJSON['items'], secondPageResponseJSON['items']
        
        return firstPageMostPopularVideosData, secondPageMostPopularVideosData

    else:
        return None, None
