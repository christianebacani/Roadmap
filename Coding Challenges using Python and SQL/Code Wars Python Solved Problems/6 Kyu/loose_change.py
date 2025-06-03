# Question: Loose Change
# Categories: 6 Kyu
import math

def loose_change(cents: int) -> dict[str, int]:
    changes = {
        'Nickels': 0, 
        'Pennies': 0, 
        'Dimes': 0, 
        'Quarters': 0
    }
    
    if cents <= 0:
        return changes
    
    if isinstance(cents, float):
        cents = math.floor(cents)

    while cents != 0:
        if cents >= 25:
            cents -= 25
            changes['Quarters'] += 1

        elif cents >= 10:
            cents -= 10
            changes['Dimes'] += 1

        elif cents >= 5:
            cents -= 5
            changes['Nickels'] += 1

        else:
            cents -= 1
            changes['Pennies'] += 1
    
    return changes