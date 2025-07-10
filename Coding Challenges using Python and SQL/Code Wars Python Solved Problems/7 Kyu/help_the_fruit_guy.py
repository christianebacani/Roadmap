# Question: Help the Fruit Guy
# Categories: 7 Kyu

def remove_rotten(bag_of_fruits: list[str]) -> list[str]:
    if bag_of_fruits == []:
        return []
    
    if bag_of_fruits is None:
        return []
    
    result = []

    for i in range(len(bag_of_fruits)):
        if 'rotten' in bag_of_fruits[i]:
            bag_of_fruits[i] = bag_of_fruits[i].replace('rotten', '')
            bag_of_fruits[i] = bag_of_fruits[i].lower()

        else:
            bag_of_fruits[i] = bag_of_fruits[i].lower()

        result.append(bag_of_fruits[i])

    return result