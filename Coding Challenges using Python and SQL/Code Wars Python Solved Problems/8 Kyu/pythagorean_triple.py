# Question: Pythagorean Triple
# Categories: 8 Kyu

def pythagorean_triple(integers: list[int]) -> bool:
    if (integers[0] ** 2) + (integers[1] ** 2) == (integers[2] ** 2):
        return True
    
    if (integers[0] ** 2) + (integers[2] ** 2) == (integers[1] ** 2):
        return True
    
    if (integers[1] ** 2) + (integers[2] ** 2) == (integers[0] ** 2):
        return True
    
    return False