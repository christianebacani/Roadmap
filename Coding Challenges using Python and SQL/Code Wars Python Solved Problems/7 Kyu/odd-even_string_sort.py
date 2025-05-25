# Question: Odd-Even String Sort
# Categories: 7 Kyu

def sort_my_string(s: str) -> str:
    result = ''

    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i]

    result += ' '

    for i in range(len(s)):
        if i % 2 != 0:
            result += s[i]
    
    return result