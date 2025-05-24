# Question: What comes after?
# Categories: 7 Kyu

def comes_after(st: str, l: str) -> str: 
    result = ''

    for i in range(1, len(st)):
        if st[i - 1].lower() != l.lower():
            continue
        
        if st[i].isalpha():
            result += st[i]

    return result