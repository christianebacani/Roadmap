# Question: Which string is worth more?
# Categories: 7 Kyu

def highest_value(a: str, b: str) -> str:
    total_ascii_value_of_a, total_ascii_value_of_b = 0, 0

    for i in range(len(a)):
        total_ascii_value_of_a += ord(a[i])
    
    for i in range(len(b)):
        total_ascii_value_of_b += ord(b[i])
    
    if total_ascii_value_of_a >= total_ascii_value_of_b:
        return a
    
    return b