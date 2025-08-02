# Question: UEFA EURO 2016
# Categories: 8 Kyu

def uefa_euro_2016(teams: list[str], scores: list[int]) -> str:
    result = f'At match {teams[0]} - {teams[1]}'
    
    if scores[0] > scores[1]:
        result += f', {teams[0]} won!'
    
    elif scores[1] > scores[0]:
        result += f', {teams[1]} won!'
    
    else:
        result += ', teams played draw.'
    
    return result