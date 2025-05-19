# Question: Reverse or rotate?
# Categories: 6 Kyu

def rev_rot(characters: str, size: int) -> str:
    if size <= 0 or characters == '' or size > len(characters):
        return ''

    result = []

    for i in range(0, len(characters), size):
        substring = characters[i : i + size]

        if len(substring) != size:
            continue

        sum_of_its_digits = 0

        for j in range(len(substring)):
            sum_of_its_digits += int(substring[j])
        
        if sum_of_its_digits % 2 == 0:
            result.append(substring[::-1])
        
        else:
            result.append(substring[1:] + substring[0])
    
    return ''.join(result)