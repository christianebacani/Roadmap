# Question: Fix string case
# Categories: 7 Kyu

def solve(s: str) -> str:
    uppercase_frequency, lowercase_frequency = 0, 0

    for i in range(len(s)):
        if s[i].isupper():
            uppercase_frequency += 1
        
        else:
            lowercase_frequency += 1

    if uppercase_frequency > lowercase_frequency:
        return s.upper()
    
    else:
        return s.lower()