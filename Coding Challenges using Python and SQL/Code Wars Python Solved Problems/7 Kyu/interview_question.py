# Question: Interview Question(easy)
# Categories: 7 Kyu

def get_strings(city: str) -> str:
    city = city.lower()
    letters = []

    for i in range(len(city)):
        if city[i] == ' ':
            continue

        if city[i] not in letters:
            letters.append(city[i])
    
    result = []

    for i in range(len(letters)):
        result.append(letters[i] + ':' + (city.count(letters[i]) * '*'))
    
    result = ','.join(result)
    return result