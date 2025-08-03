# Question: Split in Parts
# Categories: 7 Kyu

def split_in_parts(s: str, part_length: int) -> str: 
    result = []

    for i in range(0, len(s), part_length):
        splitted_word = s[i:i + part_length]
        result.append(splitted_word)
    
    result = ' '.join(result)
    return result