# Question: Exes and Ohs
# Categories: 7 Kyu

def xo(s: str) -> bool:
    s = s.lower()
    frequency_of_x = s.count('x')
    frequency_of_o = s.count('o')

    if frequency_of_x == frequency_of_o:
        return True
    
    return False