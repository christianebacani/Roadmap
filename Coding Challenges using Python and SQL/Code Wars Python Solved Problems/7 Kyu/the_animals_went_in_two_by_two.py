# Question: The animals went in two by two
# Categories: 7 Kyu

def two_by_two(animals: list[str]) -> dict[str, int] | bool:
    if animals == []:
        return False

    distinct_animals = list(set(animals))
    result = {}

    for i in range(len(distinct_animals)):
        if animals.count(distinct_animals[i]) >= 2:
            result[distinct_animals[i]] = 2
    
    return result