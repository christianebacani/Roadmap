# Question: ASCII Total
# Categories: 8 Kyu

def uni_total(s: str) -> int:
    total = 0
    
    for i in range(len(s)):
        total += ord(s[i])
    
    return total