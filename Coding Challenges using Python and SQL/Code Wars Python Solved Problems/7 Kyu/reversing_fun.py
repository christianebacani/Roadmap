# Question: Reversing Fun
# Categories: 7 Kyu

def reverse_fun(strng: str) -> str:
    strng = list(strng[::-1])

    for i in range(len(strng)):
        strng[i + 1:] = strng[i + 1:][::-1]
    
    return ''.join(strng)