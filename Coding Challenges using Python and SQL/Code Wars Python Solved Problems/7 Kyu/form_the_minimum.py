# Question: Form The Minimum
# Categories: 7 Kyu

def min_value(digits: list[int]) -> int:
    digits = sorted(list(set(digits)))

    for i in range(len(digits)):
        digits[i] = str(digits[i])
    
    return int(''.join(digits))