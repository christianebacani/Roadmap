# Question: String reverse slicing 101
# Categories: 7 Kyu

def reverse_slice(s: str) -> list[str]:
    s = s[::-1]
    result = [s]
    
    while len(s) > 1:
        result.append(s[1:])
        s = s[1:]
    
    return result