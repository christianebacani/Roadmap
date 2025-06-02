# Question: Round up to the next multiple of 5
# Categories: 7 Kyu

def round_to_next5(number: int) -> int:
    if number % 5 == 0:
        return number
    
    while number % 5 != 0:
        number += 1
    
    return number