# Question: Simple validation of a username with regex
# Categories: 8 Kyu

def validate_usr(username: list[str]) -> bool:
    if len(username) < 4 or len(username) > 16:
        return False
    
    for i in range(len(username)):
        if username[i].isupper():
            return False
        
        if username[i].isalnum():
            continue

        if username[i] == '_':
            continue

        return False

    return True