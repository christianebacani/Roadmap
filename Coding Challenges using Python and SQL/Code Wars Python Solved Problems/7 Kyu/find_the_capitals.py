# Question: Find the Capitals
# Categories: 7 Kyu

def capital(capitals: list[dict[str, str]]) -> list[str]: 
    result = []

    for i in range(len(capitals)):
        try:
            country_or_state = capitals[i]['country']

        except KeyError:
            country_or_state = capitals[i]['state']

        capital = capitals[i]['capital']

        result.append(f'The capital of {country_or_state} is {capital}')
    
    return result