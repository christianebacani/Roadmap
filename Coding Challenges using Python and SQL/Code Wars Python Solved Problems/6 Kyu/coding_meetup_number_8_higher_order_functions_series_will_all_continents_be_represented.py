# Question: Coding Meetup #8 - Higher-Order Functions Series - Will all continents be represented?
# Categories: 6 Kyu

def all_continents(lst: list[dict[str, str]]) -> bool: 
    continents = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']

    for i in range(len(continents)):
        continents_of_developers_who_will_attend = []

        for j in range(len(lst)):
            continents_of_developers_who_will_attend.append(lst[j]['continent'])
        
        if continents[i] not in continents_of_developers_who_will_attend:
            return False
    
    return True