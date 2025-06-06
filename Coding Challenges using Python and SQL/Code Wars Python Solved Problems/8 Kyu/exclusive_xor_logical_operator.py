# Question: Exclusive "or" (xor) Logical Operator
# Categories: 8 Kyu

def xor(a: bool, b: bool) -> bool:
    if (a is True and b is False) or (a is False and b is True):
        return True
    
    return False