# Question: Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?
# Categories: 7 Kyu

def is_ruby_coming(lst: list[dict[str, str]]) -> bool: 
    for i in range(len(lst)):
        if lst[i]['language'] == 'Ruby':
            return True
    
    return False