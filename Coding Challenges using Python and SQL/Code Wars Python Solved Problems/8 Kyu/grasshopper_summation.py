# Question: Grasshopper - Summation
# Categories: 8 Kyu

def summation(num: int) -> int:
    total = 0

    for i in range(1, num + 1):
        total += i
    
    return total