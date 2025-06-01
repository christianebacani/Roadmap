# Question: They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?
# Categories: 8 Kyu

def is_opposite(first_string: str, second_string: str) -> bool:
    if first_string == '' or second_string == '':
        return False
    
    total_length = len(first_string)

    for i in range(total_length):
        if first_string[i].lower() != second_string[i].lower():
            return False
        
        if first_string[i].isupper() and second_string[i].isupper():
            return False
        
        if first_string[i].islower() and second_string[i].islower():
            return False
    
    return True