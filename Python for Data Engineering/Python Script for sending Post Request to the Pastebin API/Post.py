import requests

# Post

def post():
    # API Endpoint
    url = 'https://pastebin.com/api/api_post.php'
    text = 'No matter what happens, I will become a Data Engineer!\nWritten By : Christiane Rhely Joselle A. Bacani'
    payload = {'api_dev_key' : '<API_KEY>', 'api_option' : 'paste', 'api_paste_code' : text}

    response = requests.post(url=url, data=payload)

    if response.status_code == 200 or response.status_code == 201:
        print(response.text)
    
    else:
        print(response.status_code)


if __name__ == "__main__":
    post()