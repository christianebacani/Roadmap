# 236A - Boy or Girl

def detect_gender(username: str) -> str:
    number_of_distinct_letters = len(set(username))

    if number_of_distinct_letters % 2 != 0:
        return 'IGNORE HIM!'
    
    return 'CHAT WITH HER!'

print(detect_gender(input().strip()))