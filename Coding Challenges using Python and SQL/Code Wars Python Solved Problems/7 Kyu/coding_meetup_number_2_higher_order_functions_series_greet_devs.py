# Question: Coding Meetup #2 - Higher-Order Functions Series - Greet developers
# Categories: 7 Kyu

def greet_developers(lst: list[dict[str, str]]) -> list[dict[str, str]]:
    for i in range(len(lst)):
        firstName = lst[i]['firstName']
        language = lst[i]['language']
        lst[i]['greeting'] = f'Hi {firstName}, what do you like the most about {language}?'
    
    return lst