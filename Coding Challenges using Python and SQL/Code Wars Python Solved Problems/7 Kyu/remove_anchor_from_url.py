# Question: Remove anchor from URL
# Categories: 7 Kyu

def remove_url_anchor(url: str) -> str:
    return url.split('#')[0]