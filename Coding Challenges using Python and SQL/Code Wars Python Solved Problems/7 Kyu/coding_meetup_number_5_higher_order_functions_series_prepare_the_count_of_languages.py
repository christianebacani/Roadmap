# Question: Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages
# Categories: 7 Kyu

def count_languages(lst: list[dict[str, str]]) -> dict[str, str]: 
    programming_languages_and_count = {}

    for i in range(len(lst)):
        language = lst[i]['language']

        if language not in list(programming_languages_and_count.keys()):
            programming_languages_and_count[language] = 0
    
    for i in range(len(lst)):
        language = lst[i]['language']
        
        programming_languages_and_count[language] += 1
    
    return programming_languages_and_count