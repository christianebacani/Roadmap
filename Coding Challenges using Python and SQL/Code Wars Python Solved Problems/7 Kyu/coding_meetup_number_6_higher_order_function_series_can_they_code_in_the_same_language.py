# Question: Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language?
# Categories: 7 Kyu

def is_same_language(lst: list[dict[str, str]]) -> bool: 
    attendees_programming_language = []

    for i in range(len(lst)):
        attendees_programming_language.append(lst[i]['language'])
    
    if len(set(attendees_programming_language)) == 1:
        return True
    
    return False