# Question: Bouncy Numbers
# Categories: 7 Kyu

def is_bouncy(number: int) -> bool:
    number = str(number)
    list_of_digits = [int(digit) for digit in number]
    
    if sorted(list_of_digits) == list_of_digits or sorted(list_of_digits, reverse=True) == list_of_digits:
        return False
    
    return True