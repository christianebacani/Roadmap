# Question: Beginner Series #3: Sum of Numbers
# Categories: 7 Kyu

def get_sum(a: int, b: int) -> int:
    if a == b:
        return a
    
    total = 0
    
    if a < b:
        for i in range(a, b + 1):
            total += i

    else:
        for i in range(a, b - 1, -1):
            total += i
    
    return total