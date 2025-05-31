# Question: Neutralisation
# Categories: 8 Kyu

def neutralise(s1: str, s2: str) -> str:
    total_length = len(s1)
    result = ''

    for i in range(total_length):
        if s1[i] == s2[i]:
            result += s1[i]
        
        else:
            result += '0'
    
    return result