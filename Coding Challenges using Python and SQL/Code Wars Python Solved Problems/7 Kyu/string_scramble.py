# Question: String Scramble
# Categories: 7 Kyu

def scramble(strng: str, array: list[int]) -> str:
    result = []

    for _ in range(len(strng)):
        result.append(' ')
    
    for i in range(len(strng)):
        result[array[i]] = strng[i]
    
    result = ''.join(result)
    return result