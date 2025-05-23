# Question: They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?
# Categories: 8 Kyu

def is_opposite(s1: str,s2: str) -> bool:
    if s1 == '' or s2 == '':
        return False

    for i in range(len(s1)):
        if s1[i].lower() != s2[i].lower():
            return False
    
        if s1[i].isupper() == s2[i].isupper():
            return False
        
        if s1[i].islower() == s2[i].islower():
            return False
    
    return True