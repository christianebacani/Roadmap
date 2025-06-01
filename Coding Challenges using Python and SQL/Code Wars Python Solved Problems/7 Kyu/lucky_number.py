# Question: lucky number
# Categories: 7 Kyu

def is_lucky(number: int) -> bool:
    digits = str(number)
    total = 0

    for i in range(len(digits)):
        total += int(digits[i])
    
    if total == 0 or total % 9 == 0:
        return True
    
    return False