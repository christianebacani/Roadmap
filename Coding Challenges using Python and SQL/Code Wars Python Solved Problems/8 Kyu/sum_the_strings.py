# Question: Sum The Strings
# Categories: 8 Kyu

def sum_str(a: str, b: str) -> str:
    if a == '' and b == '':
        return '0'
    
    if a != '' and b == '':
        return a
    
    if a == '' and b != '':
        return b

    return str(int(a) + int(b))