# Question: Triple trouble
# Categoties: 6 Kyu

def triple_double(num1: int, num2: int) -> int:
    num1 = str(num1)
    num2 = str(num2)
    digits = '0123456789'
    
    
    for i in range(len(digits)):
        if (digits[i] * 3) in num1 and (digits[i] * 2) in num2:
            return 1
    
    return 0