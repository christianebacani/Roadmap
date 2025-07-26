# Question: Power of two
# Categories: 7 Kyu

def power_of_two(x: int) -> bool:
    for n in range(5001):
        if (2 ** n) == x:
            return True
    
    return False