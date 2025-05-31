# Question: Responsible Drinking
# Categories: 7 Kyu

def hydrate(drink_string: str) -> str: 
    drink_string = drink_string.split()
    total = 0

    for i in range(len(drink_string)):
        drink = drink_string[i]
        
        if drink.isdigit():
            total += int(drink)
    
    if total == 1:
        return f'{total} glass of water'

    return f'{total} glasses of water'