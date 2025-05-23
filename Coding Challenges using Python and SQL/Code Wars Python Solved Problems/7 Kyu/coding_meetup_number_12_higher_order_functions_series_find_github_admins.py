# Question: Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins
# Categories: 7 Kyu

def find_admin(lst: list[dict[str, str]], language: str) -> list[dict[str, str]]: 
    result = []

    for i in range(len(lst)):
        if lst[i]['githubAdmin'] == 'no':
            continue

        if lst[i]['language'] == language:
            result.append(lst[i])
    
    return result