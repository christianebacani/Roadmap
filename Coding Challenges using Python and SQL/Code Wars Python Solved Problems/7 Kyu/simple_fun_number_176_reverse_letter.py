# Question: Simple Fun #176: Reverse Letter
# Categories: 7 Kyu

def reverse_letter(st: str) -> str:
    result = ''

    for i in range(len(st)):
        if st[i].isalpha():
            result += st[i]
    
    return result[::-1]