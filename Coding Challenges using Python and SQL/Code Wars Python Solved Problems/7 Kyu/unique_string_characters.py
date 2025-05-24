# Question: Unique string characters
# Categories: 7 Kyu

def solve(a: str, b: str) -> str:
    result = ''

    for i in range(len(a)):
        if a[i] not in b:
            result += a[i]
    
    for i in range(len(b)):
        if b[i] not in a:
            result += b[i]
    
    return result