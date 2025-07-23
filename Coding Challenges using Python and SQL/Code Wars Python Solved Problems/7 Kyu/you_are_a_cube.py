# Question: You are a Cube!
# Categories: 7 Kyu

def you_are_a_cube(cube: int) -> bool:
    for i in range(1, 1001):
        if (i * i * i) == cube:
            return True
    
    return False