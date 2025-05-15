# Question: Extract the domain name from a URL
# Categories: 5 Kyu

def domain_name(url: str) -> str:
    if url.startswith('https://www.'):
        url = url.replace('https://www.', '')
    
    elif url.startswith('http://www.'):
        url = url.replace('http://www.', '')
    
    elif url.startswith('https://'):
        url = url.replace('https://', '')
    
    elif url.startswith('http://'):
        url = url.replace('http://', '')

    elif url.startswith('www.'):
        url = url.replace('www.', '')
    
    url = url.split('.')
    
    return url[0]